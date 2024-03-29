#
import torch
from torch import nn
import torch.nn.functional as F
#from biz.dmrl.iqtt.iqtt_config import IqttConfig
#from biz.dmrl.iqtt.iqtt_util import IqttUtil
#from biz.dmrl.iqtt.transformer_block import TransformerBlock
from apps.fmts.conf.app_config import AppConfig
from apps.fmts.ann.fmts_transformer_block import FmtsTransformerBlock
from apps.fmts.ann.fmts_ann_util import FmtsAnnUtil

class FmtsTransformer(nn.Module):
    """
    Transformer for classifying sequences
    """

    def __init__(self, emb, heads, depth, seq_length, num_tokens, num_classes, max_pool=True, dropout=0.0, wide=False):
        """
        :param emb: Embedding dimension
        :param heads: nr. of attention heads
        :param depth: Number of transformer blocks
        :param seq_length: Expected maximum sequence length
        :param num_tokens: Number of tokens (usually words) in the vocabulary
        :param num_classes: Number of classes.
        :param max_pool: If true, use global max pooling in the last layer. If false, use global
                         average pooling.
        """
        super().__init__()
        self.num_tokens, self.max_pool = num_tokens, max_pool
        self.token_embedding = nn.Embedding(embedding_dim=emb, num_embeddings=num_tokens)
        self.pos_embedding = nn.Embedding(embedding_dim=emb, num_embeddings=seq_length)
        tblocks = []
        for i in range(depth):
            tblocks.append(
                FmtsTransformerBlock(emb=emb, heads=heads, seq_length=seq_length, mask=False, dropout=dropout))
        self.tblocks = nn.Sequential(*tblocks)
        self.toprobs = nn.Linear(emb, num_classes)
        self.do = nn.Dropout(dropout)

    def forward(self, x):
        """
        :param x: A batch by sequence length integer tensor of token indices.
        :return: predicted log-probability vectors for each token based on the preceding tokens.
        """
        x = self.do(x)
        x = self.tblocks(x)
        x = x.max(dim=1)[0] if self.max_pool else x.mean(dim=1) # pool over the time dimension
        x = self.toprobs(x)
        return F.log_softmax(x, dim=1)