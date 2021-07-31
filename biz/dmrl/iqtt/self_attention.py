#
import math
import torch
from torch import nn
import torch.nn.functional as F
from biz.dmrl.iqtt.iqtt_util import IqttUtil

class SelfAttention(nn.Module):
    def __init__(self, emb, heads=2, mask=False):
        '''
        参数：
            emb 输入向量维度
            heads 多头注意力的头数
            mask
        '''
        super().__init__()
        self.emb = emb
        self.heads = heads
        self.mask = mask
        self.tokeys = nn.Linear(emb, emb * heads, bias=False)
        self.toqueries = nn.Linear(emb, emb * heads, bias=False)
        self.tovalues = nn.Linear(emb, emb * heads, bias=False)
        self.unifyheads = nn.Linear(heads * emb, emb)

    def forward(self, x):
        b, t, e = x.size()
        h = self.heads
        assert e == self.emb, f'Input embedding dim ({e}) should match layer embedding dim ({self.emb})'
        keys    = self.tokeys(x)   .view(b, t, h, e)
        queries = self.toqueries(x).view(b, t, h, e)
        values  = self.tovalues(x) .view(b, t, h, e)
        # compute scaled dot-product self-attention
        # - fold heads into the batch dimension
        keys = keys.transpose(1, 2).contiguous().view(b * h, t, e)
        queries = queries.transpose(1, 2).contiguous().view(b * h, t, e)
        values = values.transpose(1, 2).contiguous().view(b * h, t, e)
        # - get dot product of queries and keys, and scale
        dot = torch.bmm(queries, keys.transpose(1, 2))
        dot = dot / math.sqrt(e) # dot contains b*h  t-by-t matrices with raw self-attention logits
        assert dot.size() == (b*h, t, t), f'Matrix has size {dot.size()}, expected {(b*h, t, t)}.'
        if self.mask: # mask out the lower half of the dot matrix,including the diagonal
            IqttUtil.mask_(dot, maskval=float('-inf'), mask_diagonal=False)

        dot = F.softmax(dot, dim=2) # dot now has row-wise self-attention probabilities
        assert not IqttUtil.contains_nan(dot[:, 1:, :]) # only the forst row may contain nan
        if self.mask == 'first':
            dot = dot.clone()
            dot[:, :1, :] = 0.0
            # - The first row of the first attention matrix is entirely masked out, so the softmax operation results
            #   in a division by zero. We set this row to zero by hand to get rid of the NaNs
        # apply the self attention to the values
        out = torch.bmm(dot, values).view(b, h, t, e)
        # swap h, t back, unify heads
        out = out.transpose(1, 2).contiguous().view(b, t, h * e)
        return self.unifyheads(out)