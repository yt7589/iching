#
import numpy as np
import torch

class A3cCommon(object):
    @staticmethod
    def unpack_batch(batch, net, last_val_gamma, device='cpu'):
        """
        Convert batch into training tensors
        :param batch:
        :param net:
        :return: states variable, actions tensor, reference values variable
        """
        states = []
        actions = []
        rewards = []
        not_done_idx = []
        last_states = []
        for idx, exp in enumerate(batch):
            states.append(np.array(exp.state, copy=False))
            actions.append(int(exp.action))
            rewards.append(exp.reward)
            if exp.last_state is not None:
                not_done_idx.append(idx)
                last_states.append(np.array(exp.last_state, copy=False))
        states_v = torch.FloatTensor(np.array(states, copy=False)).to(device)
        actions_t = torch.LongTensor(actions).to(device)

        # handle rewards
        rewards_np = np.array(rewards, dtype=np.float32)
        if not_done_idx:
            last_states_v = torch.FloatTensor(np.array(last_states, copy=False)).to(device)
            last_vals_v = net(last_states_v)[1]
            last_vals_np = last_vals_v.data.cpu().numpy()[:, 0]
            rewards_np[not_done_idx] += last_val_gamma * last_vals_np

        ref_vals_v = torch.FloatTensor(rewards_np).to(device)
        return states_v, actions_t, ref_vals_v
