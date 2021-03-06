#
import sys
import numpy as np
import gym
from gym import spaces
from ann.fme.fme_env import FmeEnv
from apps.common.cna_stock import CnaStock

class AsdkEnv(FmeEnv):

    def __init__(self, ds, 
                lookback_window_size=5, initial_balance=2000.0):
        self.name = 'ann.envs.AsdkEnv'
        self.ds = ds 
        self.lookback_window_size = lookback_window_size
        self.initial_balance = initial_balance
        self.balance = None
        self.net_worth = None
        self.position = None
        self.rlw = None
        self.action_space = spaces.MultiDiscrete([3, 3])
        self.observation_space = spaces.Box(
            low=0.0, high=10000.0, shape=(28, 1), dtype=np.float64
        )

    def reset(self):
        self.balance = np.array([self.initial_balance])
        self.net_worth = np.array([self.initial_balance])
        self.position = np.array([0])
        self.trades = np.array([])
        self.rlw = np.array([])
        self._reset_session()
        return self._next_observation()

    def _reset_session(self):
        self.current_step = 0
        self.step_left = len(self.ds)

    def _next_observation(self):
        obs = np.array(
            self.ds[self.current_step]
        )
        obs = np.append(obs, [
            self.position[self.current_step],
            self.balance[self.current_step], 
            self.net_worth[self.current_step]
        ])
        return obs

    def get_last_observation(self, daily_tick):
        ds_len = len(self.ds)
        obs = np.array(
            self.ds[ds_len - 1]
        )
        obs = np.append(obs, [daily_tick])
        obs = np.append(obs, [
            self.position[ds_len - 1],
            self.balance[ds_len - 1], 
            self.net_worth[ds_len - 1]
        ])
        return obs

    def step(self, action):
        info = self._take_action(action)
        self.current_step += 1
        self.step_left -=1
        done = self.net_worth[self.current_step] < 0
        if 0 >= self.step_left:
            print('回测结束......')
            reward = 1.0
            done = True
            return None, reward, done, {}
        obs = self._next_observation()
        reward = (self.net_worth[-1] / self.net_worth[-2]) ** 10
        self.rlw = np.append(self.rlw, [reward])
        return obs, reward, done, info

    def get_last_observation(self):
        self.current_step -= 1
        obs = np.array(
            self.ds[self.current_step]
        )
        obs = np.append(obs, [
            self.position[-1],
            self.balance[-1], self.net_worth[-1]
        ])
        self.current_step += 1
        return obs

    def _take_action(self, action):
        action_type = action[0]
        action_percent = action[1]
        current_idx = (self.lookback_window_size - 1)*5
        price = self.ds[self.current_step][3 + (self.lookback_window_size - 1)*5]
        quant = 0
        cost = 0.0
        if 0 == action_type:
            action[0], quant, amount, cost = self._do_hold_action(current_idx, price)
        elif 1 == action_type:
            action[0], quant, amount, cost = self._do_sell_action(current_idx, price)
        elif 2 == action_type:
            action[0], quant, amount, cost = self._do_buy_action(current_idx, price)
        return {'price': price, 'quant': quant, 'cost': cost}

    def _do_hold_action(self, current_idx, price):
        self.position = np.append(self.position, [self.position[-1]])
        self.balance = np.append(self.balance, [self.balance[-1]])
        net_worth = self.balance[-1] + self.position[-1] * price
        net_worth = int(net_worth * 100) / 100
        self.net_worth = np.append(self.net_worth, [net_worth])
        self.trades = np.append(self.trades, [{
            'date': '', 
            'open': self.ds[self.current_step][0 + current_idx],
            'high': self.ds[self.current_step][1 + current_idx],
            'low': self.ds[self.current_step][2 + current_idx],
            'close': self.ds[self.current_step][3 + current_idx],
            'volume': self.ds[self.current_step][4 + current_idx],
            'type': 0, 'quant': 0, 'position': self.position[-1],
            'balance': self.balance[-1], 'net_worth': self.net_worth[-1]
        }])
        return 0, 0, 0.0, 0.0

    def _do_sell_action(self, current_idx, price):
        quant = self.position[-1]
        amount = quant * price
        cost = CnaStock.sell_stock_cost(amount)
        balance = self.balance[-1] + amount - cost
        balance = int(balance * 100) / 100.0
        net_worth = balance
        self.position = np.append(self.position, [0])
        self.balance = np.append(self.balance, [balance])
        self.net_worth = np.append(self.net_worth, [net_worth])
        self.trades = np.append(self.trades, [{
            'date': '', 
            'open': self.ds[self.current_step][0 + current_idx],
            'high': self.ds[self.current_step][1 + current_idx],
            'low': self.ds[self.current_step][2 + current_idx],
            'close': self.ds[self.current_step][3 + current_idx],
            'volume': self.ds[self.current_step][4 + current_idx],
            'type': 1, 'quant': quant, 'position': self.position[-1],
            'balance': self.balance[-1], 'net_worth': self.net_worth[-1]
        }])
        return 1, quant, amount, cost

    def _do_buy_action(self, current_idx, price):           
        quant = int(self.balance[-1] / price)
        if quant < 1:
            return self._do_hold_action(current_idx, price)
        amount = quant * price
        cost = CnaStock.buy_stock_cost(amount)
        while self.balance[-1] - amount - cost < 0:
            quant -= 1
            amount = quant * price
            cost = CnaStock.buy_stock_cost(amount)
        balance = self.balance[-1] - amount - cost
        balance = int(balance * 100) / 100.0
        position = self.position[-1] + quant
        net_worth = balance + amount
        net_worth = int(net_worth * 100) / 100.0
        self.position = np.append(self.position, [position])
        self.balance = np.append(self.balance, [balance])
        self.net_worth = np.append(self.net_worth, [net_worth])
        self.trades = np.append(self.trades, [{
            'date': '', 
            'open': self.ds[self.current_step][0 + current_idx],
            'high': self.ds[self.current_step][1 + current_idx],
            'low': self.ds[self.current_step][2 + current_idx],
            'close': self.ds[self.current_step][3 + current_idx],
            'volume': self.ds[self.current_step][4 + current_idx],
            'type': 2, 'quant': quant, 'position': self.position[-1],
            'balance': self.balance[-1], 'net_worth': self.net_worth[-1]
        }])
        return 2, quant, amount, cost