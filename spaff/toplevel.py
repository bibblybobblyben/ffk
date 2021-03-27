import numpy as np
from spaff import hypothesis, evaluation




class SphereFit():
    def __init__(self,
                 n_samples = 10,
                 initial_state = None,
                 hyp_function = hypothesis.make_kappa,
                 eval_function = evaluation.shear_chi2,
                 acc_function = evaluation.MetropolisHastings):
        self.n_samples = n_samples
        self.hyp_function = hyp_function
        self.eval_function = eval_function
        self.acceptance_function = acc_function

    def run(self):

        for i in range(self.n_samples):
            self.hypothesise()
            self.evaluate()
            self.acc_rej()
            self.save_state()

        return
    def hypothesise(self):
        self.hypothesis_function(self)
        return
    def evaluate(self):
        self.eval_function(self)
        return
    def acc_rej(self):
        self.acceptance_function(self)
        return
    def save_state(self):
        self.state_output(self)
        return



