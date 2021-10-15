import numpy as np
import healpy as hp

def perturb_one_mode(emodes, amp = 0.2):
    chosen_int = np.random.randint(0, len(emodes))
    change_r = np.random.normal(0.0, amp)
    change_i = np.random.normal(0.0, amp)
    real = np.real(emodes[chosen_int])
    im = np.imag(emodes[chosen_int])
    emodes[chosen_int] = real+change_r +1j*(change_i+im)
    return emodes


def make_simple_hypothesis(SphereFit):
    '''
    Simple function to add a random amplitude to all harmonic coefficients.
    Updates the hyp parameter for the SphereFit class.
    :param SphereFit: SphereFit class defining current state
    :return:
    '''
    current_state = SphereFit.current_state
    newhyp = perturb_one_mode(current_state)
    SphereFit.emodes = newhyp
    SphereFit.data_hyp = hp.alm2map(newhyp, nside=SphereFit.nside)
    #print(newhyp)

