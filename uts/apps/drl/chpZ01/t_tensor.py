#
import sys,random,math
from collections import Counter
import numpy as np
import unittest
from apps.drl.chpZ01.tensor import Tensor
from apps.drl.chpZ01.optim_sgd import OptimSgd
from apps.drl.chpZ01.linear import Linear
from apps.drl.chpZ01.sequential import Sequential
from apps.drl.chpZ01.loss_mse import LossMse
from apps.drl.chpZ01.af_tanh import AfTanh
from apps.drl.chpZ01.af_sigmoid import AfSigmoid
from apps.drl.chpZ01.af_relu import AfRelu
from apps.drl.chpZ01.embedding import Embedding
from apps.drl.chpZ01.loss_cross_entropy import LossCrossEntropy
from apps.drl.chpZ01.linear import Linear
from apps.drl.chpZ01.rnn_cell import RnnCell

class TTensor(unittest.TestCase):
    @classmethod
    def setUp(cls):
        pass

    @classmethod
    def tearDown(cls):
        pass

    def test_init_001(self):
        a = Tensor(np.array([1, 2, 3, 4, 5]), autograd=True)
        b = Tensor(np.array([10, 10, 10, 10, 10]), autograd=True)
        c = Tensor(np.array([5, 4, 3, 2, 1]), autograd=True)
        d = a + b
        e = b + c
        f = d + e
        print('f: {0};'.format(f.to_string()))
        print('d: {0};'.format(d.to_string()))
        print('e: {0};'.format(e.to_string()))
        print('a: {0};'.format(a.to_string()))
        print('b: {0};'.format(b.to_string()))
        print('c: {0};'.format(c.to_string()))

    def test_add_backward_001(self):
        a = Tensor(np.array([1, 2, 3, 4, 5]), autograd=True)
        b = Tensor(np.array([10, 10, 10, 10, 10]), autograd=True)
        c = Tensor(np.array([5, 4, 3, 2, 1]), autograd=True)
        d = a + b
        e = b + c
        f = d + e
        f.backward(Tensor(np.array([1, 1, 1, 1, 1])))
        print('f: {0};'.format(f.to_string()))
        print('d: {0};'.format(d.to_string()))
        print('e: {0};'.format(e.to_string()))
        print('a: {0};'.format(a.to_string()))
        print('b: {0};'.format(b.to_string()))
        print('c: {0};'.format(c.to_string()))

    def test_neg_backward_001(self):
        a = Tensor(np.array([1, 2, 3, 4, 5]), autograd=True)
        b = Tensor(np.array([10, 10, 10, 10, 10]), autograd=True)
        c = Tensor(np.array([5, 4, 3, 2, 1]), autograd=True)
        d = a + (-b)
        e = (-b) + c
        f = d + e
        f.backward(Tensor(np.array([1, 1, 1, 1, 1])))
        print('f: {0};'.format(f.to_string()))
        print('d: {0};'.format(d.to_string()))
        print('e: {0};'.format(e.to_string()))
        print('a: {0};'.format(a.to_string()))
        print('b: {0};'.format(b.to_string()))
        print('c: {0};'.format(c.to_string()))

    def test_sub_backward_001(self):
        a = Tensor(np.array([1, 2, 3, 4, 5]), autograd=True)
        b = Tensor(np.array([10, 10, 10, 10, 10]), autograd=True)
        c = Tensor(np.array([5, 4, 3, 2, 1]), autograd=True)
        d = a + b
        e = b - c
        f = d + e
        f.backward(Tensor(np.array([1, 1, 1, 1, 1])))
        print('f: {0};'.format(f.to_string()))
        print('d: {0};'.format(d.to_string()))
        print('e: {0};'.format(e.to_string()))
        print('a: {0};'.format(a.to_string()))
        print('b: {0};'.format(b.to_string()))
        print('c: {0};'.format(c.to_string()))

    def test_mul_backward_001(self):
        a = Tensor(np.array([1, 2, 3, 4, 5]), autograd=True)
        b = Tensor(np.array([10, 10, 10, 10, 10]), autograd=True)
        c = Tensor(np.array([5, 4, 3, 2, 1]), autograd=True)
        d = a + b
        e = b - c
        f = d * e
        f.backward(Tensor(np.array([1, 1, 1, 1, 1])))
        print('f: {0};'.format(f.to_string()))
        print('d: {0};'.format(d.to_string()))
        print('e: {0};'.format(e.to_string()))
        print('a: {0};'.format(a.to_string()))
        print('b: {0};'.format(b.to_string()))
        print('c: {0};'.format(c.to_string()))

    def test_sum_001(self):
        v = Tensor(np.array([
            [1, 2, 3],
            [4, 5, 6]
        ]))
        print(v.sum(0))
        print(v.sum(1))

    def test_expand_001(self):
        v = Tensor(np.array([
            [1, 2, 3],
            [4, 5, 6]
        ]))
        print('v.expand: {0}'.format(v.expand(0, 4)))

    def test_expand_002(self):
        v = Tensor(np.array([
            [1, 2, 3],
            [4, 5, 6]
        ]))
        print('v.expand: {0}'.format(v.expand(1, 4)))

    def test_sum_grad_001(self):
        v = Tensor(np.array([
            [1, 2, 3],
            [4, 5, 6]
        ]), autograd=True)
        u = v.sum(0)
        u.backward(Tensor(np.array([1, 1, 1])))
        print('grad: {0};'.format(v.to_string()))

    def test_transpose_001(self):
        v = Tensor(np.array([
            [1, 2, 3],
            [4, 5, 6]
        ]), autograd=True)
        v_t = v.transpose()
        print('v_t: \r\n{0};'.format(v_t))
        v_t.backward(Tensor(np.array([[1, 1], [1, 1], [1, 1]])))
        print('grad v: \r\n{0};'.format(v.grad))

    def test_mm_001(self):
        a1 = Tensor(np.array([[1.0], [2.0], [3.0]]), autograd=True)
        w_2 = Tensor(np.array([
            [11.0, 21.0, 31.0],
            [12.0, 22.0, 32.0],
            [13.0, 23.0, 33.0],
            [14.0, 24.0, 34.0]
        ]), autograd=True)
        z2 = w_2.mm(a1)
        print('z2: {0};\r\n{1}'.format(z2.data.shape, z2))
        z2.backward(Tensor(np.ones_like(z2.data)))
        print('a1.grad: {0};'.format(a1.grad))
        print('w_2.grad: {0};'.format(w_2.grad))

    def test_train_nn_001(self):
        np.random.seed(0)
        data = Tensor(np.array([[0,0],[0,1],[1,0],[1,1]]), autograd=True)
        target = Tensor(np.array([[0],[1],[0],[1]]), autograd=True)
        w = list()
        w.append(Tensor(np.random.rand(2,3), autograd=True))
        w.append(Tensor(np.random.rand(3,1), autograd=True))
        for i in range(10):
            pred = data.mm(w[0]).mm(w[1])
            loss = ((pred - target)*(pred - target)).sum(0)
            loss.backward(Tensor(np.ones_like(loss.data)))
            for w_ in w:
                w_.data -= w_.grad.data * 0.1
                w_.grad.data *= 0
            print('epoch_{0}: loss={1};'.format(i, loss))
        print(loss)

    def test_train_nn_002(self):
        np.random.seed(0)
        data = Tensor(np.array([[0,0],[0,1],[1,0],[1,1]]), autograd=True)
        target = Tensor(np.array([[0],[1],[0],[1]]), autograd=True)
        w = list()
        w.append(Tensor(np.random.rand(2,3), autograd=True))
        w.append(Tensor(np.random.rand(3,1), autograd=True))
        optim = OptimSgd(parameters=w, alpha=0.1)
        for i in range(10):
            pred = data.mm(w[0]).mm(w[1])
            loss = ((pred - target)*(pred - target)).sum(0)
            loss.backward(Tensor(np.ones_like(loss.data)))
            optim.step()
            print('epoch_{0}: loss={1};'.format(i, loss))
        print(loss)

    def test_train_nn_003(self):
        np.random.seed(0)
        data = Tensor(np.array([[0,0],[0,1],[1,0],[1,1]]), autograd=True)
        target = Tensor(np.array([[0],[1],[0],[1]]), autograd=True)
        model = Sequential([Linear(2,3), Linear(3,1)])
        optim = OptimSgd(parameters=model.get_parameters(), alpha=0.05)
        for i in range(10):
            pred = model.forward(data)
            loss = ((pred - target)*(pred - target)).sum(0)
            loss.backward(Tensor(np.ones_like(loss.data)))
            optim.step()
            print('epoch_{0}: loss={1};'.format(i, loss))
        print(loss)

    def test_train_nn_004(self):
        np.random.seed(0)
        data = Tensor(np.array([[0,0],[0,1],[1,0],[1,1]]), autograd=True)
        target = Tensor(np.array([[0],[1],[0],[1]]), autograd=True)
        model = Sequential([Linear(2,3), Linear(3,1)])
        criterion = LossMse()
        optim = OptimSgd(parameters=model.get_parameters(), alpha=0.05)
        for i in range(10):
            pred = model.forward(data)
            loss = criterion.forward(pred, target)
            loss.backward(Tensor(np.ones_like(loss.data)))
            optim.step()
            print('epoch_{0}: loss={1};'.format(i, loss))
        print(loss)

    def test_train_nn_005(self):
        np.random.seed(0)
        data = Tensor(np.array([[0,0],[0,1],[1,0],[1,1]]), autograd=True)
        target = Tensor(np.array([[0],[1],[0],[1]]), autograd=True)
        model = Sequential([Linear(2,3), AfTanh(), Linear(3,1), AfSigmoid()])
        criterion = LossMse()
        optim = OptimSgd(parameters=model.get_parameters(), alpha=1)
        for i in range(10):
            pred = model.forward(data)
            loss = criterion.forward(pred, target)
            loss.backward(Tensor(np.ones_like(loss.data)))
            optim.step()
            print('epoch_{0}: loss={1};'.format(i, loss))
        print(loss)

    def test_train_nn_006(self):
        np.random.seed(0)
        data = Tensor(np.array([[0,0],[0,1],[1,0],[1,1]]), autograd=True)
        target = Tensor(np.array([[0],[1],[0],[1]]), autograd=True)
        model = Sequential([Linear(2,3), AfRelu(), Linear(3,1), AfSigmoid()])
        criterion = LossMse()
        optim = OptimSgd(parameters=model.get_parameters(), alpha=0.8)
        for i in range(10):
            pred = model.forward(data)
            loss = criterion.forward(pred, target)
            loss.backward(Tensor(np.ones_like(loss.data)))
            optim.step()
            print('epoch_{0}: loss={1};'.format(i, loss))
        print(loss)

    def test_embedding_001(self):
        np.random.seed(0)
        data = Tensor(np.array([1,2,1,2]), autograd=True)
        target = Tensor(np.array([[0],[1],[0],[1]]), autograd=True)
        embed = Embedding(5,3)
        model = Sequential([embed, AfTanh(), Linear(3,1), AfSigmoid()])
        criterion = LossMse()
        optim = OptimSgd(parameters=model.get_parameters(), alpha=0.5)
        for i in range(10):
            # Predict
            pred = model.forward(data)
            # Compare
            loss = criterion.forward(pred, target)
            # Learn
            loss.backward(Tensor(np.ones_like(loss.data)))
            optim.step()
            print('epoch_{0}: loss={1};'.format(i, loss))

    def test_cross_entropy_001(self):
        np.random.seed(0)
        # data indices
        data = Tensor(np.array([1,2,1,2]), autograd=True)
        # target indices
        target = Tensor(np.array([0,1,0,1]), autograd=True)
        model = Sequential([Embedding(3,3), AfTanh(), Linear(3,4)])
        criterion = LossCrossEntropy()
        optim = OptimSgd(parameters=model.get_parameters(), alpha=0.1)
        for i in range(10):
            # Predict
            pred = model.forward(data)
            # Compare
            loss = criterion.forward(pred, target)
            # Learn
            loss.backward(Tensor(np.ones_like(loss.data)))
            optim.step()
            print('epoch_{0}: loss={1};'.format(i, loss))

    def test_rnn_cell_001(self):
        f = open('apps/drl/chpZ01/qa1_single-supporting-fact_train.txt','r')
        raw = f.readlines()
        f.close()
        tokens = list()
        for line in raw[0:1000]:
            tokens.append(line.lower().replace("\n","").split(" ")[1:])
        new_tokens = list()
        for line in tokens:
            new_tokens.append(['-'] * (6 - len(line)) + line)
        tokens = new_tokens
        vocab = set()
        for sent in tokens:
            for word in sent:
                vocab.add(word)
        vocab = list(vocab)
        word2index = {}
        for i,word in enumerate(vocab):
            word2index[word]=i
        indices = list()
        for line in tokens:
            idx = list()
            for w in line:
                idx.append(word2index[w])
            indices.append(idx)
        data = np.array(indices)
        # train process
        embed = Embedding(vocab_size=len(vocab),dim=16)
        model = RnnCell(n_inputs=16, n_hidden=16, n_output=len(vocab))
        criterion = LossCrossEntropy()
        optim = OptimSgd(parameters=model.get_parameters() + embed.get_parameters(), alpha=0.05)
        for iter in range(1000):
            batch_size = 100
            total_loss = 0
            hidden = model.init_hidden(batch_size=batch_size)
            for t in range(5):
                input = Tensor(data[0:batch_size,t], autograd=True)
                rnn_input = embed.forward(input=input)
                output, hidden = model.forward(input=rnn_input, hidden=hidden)
            target = Tensor(data[0:batch_size,t+1], autograd=True)    
            loss = criterion.forward(output, target)
            loss.backward()
            optim.step()
            total_loss += loss.data
            if(iter % 200 == 0):
                p_correct = (target.data == np.argmax(output.data,axis=1)).mean()
                print("Loss:",total_loss / (len(data)/batch_size),"% Correct:",p_correct)
        # test process
        batch_size = 1
        hidden = model.init_hidden(batch_size=batch_size)
        for t in range(5):
            input = Tensor(data[0:batch_size,t], autograd=True)
            rnn_input = embed.forward(input=input)
            output, hidden = model.forward(input=rnn_input, hidden=hidden)
        target = Tensor(data[0:batch_size,t+1], autograd=True)    
        loss = criterion.forward(output, target)
        ctx = ""
        for idx in data[0:batch_size][0][0:-1]:
            ctx += vocab[idx] + " "
        print("Context:",ctx)
        print("True:",vocab[target.data[0]])
        print("Pred:", vocab[output.data.argmax()])




