import numpy as np
from spaff import hypothesis, evaluation
from spaff import logging
import healpy as hp


class SphereFit():
    def __init__(self,
                 n_samples = 10,
                 initial_state = None,
                 hyp_function = hypothesis.make_simple_hypothesis,
                 eval_function = evaluation.evaluate_chi2,
                 acc_function = evaluation.MetropolisHastings,
                 logging = logging.save_healpy_at_intervals):
        self.n_samples = n_samples
        self.hypothesis_function = hyp_function
        self.eval_function = eval_function
        self.acceptance_function = acc_function
        self.save_state = logging

    def run(self):
        self.nside = hp.npix2nside(len(self.data))
        self.iter = 0
        self.distance=1000


        for i in range(self.n_samples):
            self.hypothesise()
            #print("oplevelhyp", self.emodes)
            self.evaluate()
            self.acc_rej()
            if self.accept is True:
                self.current_state = self.emodes
                self.distance = self.hyp_distance
                print("accepted", i, self.delta_hyp, self.distance)
            #self.save_state(self)
            self.iter +=1

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



