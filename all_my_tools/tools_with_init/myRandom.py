import numpy as np




class MyRandom:

    _seed=15

    def set_seed(self,seed):
        np.random.seed(seed)

    def randint(self,low,high):
        return np.random.randint(low=low,high=high)