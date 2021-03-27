import numpy as np


def make_kappa(SphereFit):
    '''
    Simple function to add a random amplitude to all harmonic coefficients.
    Updates the hyp parameter for the SphereFit class.
    :param SphereFit: SphereFit class defining current state
    :return:
    '''
    current_state = SphereFit.state