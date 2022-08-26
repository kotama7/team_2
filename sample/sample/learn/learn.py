import os
import sys
import numpy as np

class learning:

    def __init__(self,alpha,gamma):
        self.alpha = alpha
        self.gamma = gamma
        if os.path.exists('./sample/learn/model.npy'):
            while True:
                self.ans = input('Do you recreate machine model (y/n)')
                if self.ans == 'y':
                    self.model_create()
                    break
                elif self.ans == 'n':
                    break
        else:
            self.model_create()

    def model_create(self,env,opt_ls):
        q_value = np.zeros_like(env)
        q_change = []
        while not (q_change == np.zeros_like(env)):
            for opt in opt_ls:
                self.computer_reward(opt,env)


    def computer_reward(self,opt,env):
