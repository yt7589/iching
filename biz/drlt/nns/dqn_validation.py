#
import numpy as np
import torch
#
from biz.drlt.envs.asset_actions import AssetActions

class DqnValidation(object):
    METRICS = (
        'episode_reward',
        'episode_steps',
        'order_profits',
        'order_steps',
    )

    @staticmethod
    def validation_run(env, net, episodes=100, device="cpu", epsilon=0.02, comission=0.1):
        stats = { metric: [] for metric in DqnValidation.METRICS }

        for episode in range(episodes):
            obs = env.reset()

            total_reward = 0.0
            position = None
            position_steps = None
            episode_steps = 0

            while True:
                obs_v = torch.tensor([obs]).to(device)
                out_v = net(obs_v)

                action_idx = out_v.max(dim=1)[1].item()
                if np.random.random() < epsilon:
                    action_idx = env.action_space.sample()
                action = AssetActions(action_idx)

                close_price = env._state._cur_close()

                if action == AssetActions.Buy and position is None:
                    position = close_price
                    position_steps = 0
                elif action == AssetActions.Sell and position is not None:
                    profit = close_price - position - (close_price + position) * comission / 100
                    profit = 100.0 * profit / position
                    stats['order_profits'].append(profit)
                    stats['order_steps'].append(position_steps)
                    position = None
                    position_steps = None

                obs, reward, done, _ = env.step(action_idx)
                total_reward += reward
                episode_steps += 1
                if position_steps is not None:
                    position_steps += 1
                if done:
                    if position is not None:
                        profit = close_price - position - (close_price + position) * comission / 100
                        profit = 100.0 * profit / position
                        stats['order_profits'].append(profit)
                        stats['order_steps'].append(position_steps)
                    break

            stats['episode_reward'].append(total_reward)
            stats['episode_steps'].append(episode_steps)

        return { key: np.mean(vals) for key, vals in stats.items() }
