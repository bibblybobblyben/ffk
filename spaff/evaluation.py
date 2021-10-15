import numpy as np

def nfield_diag_chi2(field1, field2, error, depth=1, amp=None):
    '''
    Calculates chi-squared between two observations, according to errors in each pixel.
    Errors are assumed to be diagonal - total chi2 is just the sum of the individual difference
    in each pixel, weighted by an error, and does not account for any inter-pixel
    dependences which can affect the chi2.

    The function can take multiple fields - for example, gamma1 and gamma2 in shear analyses
    as a single input.

    :param field1: The first field to be evaluated
    :param field2: The second field, against which field1 is evaluated
    :param depth: The number of fields present in a single field
    :param amp:
    :return:
    '''
    # calculates chi2, field =0 means comparing kappa,phi maps, field=2 means shear maps
    if np.any([error<0]):
        raise ValueError("Negative values in error array.")
    eval_region = np.where(error != 0.0)
    chi2 = 0
    for i in range(depth):
        diffs = field1[i][eval_region] - field2[i][eval_region]
        chi2 += np.sum(diffs**2/error[eval_region]**2)
    return chi2

def chi2_score(field1, field2, efield):
    return np.sum((field1-field2)**2/efield**2)

def evaluate_chi2(SphereFit):
    SphereFit.hyp_distance = chi2_score(SphereFit.data_hyp, SphereFit.data, SphereFit.error_map)
    SphereFit.delta_hyp = (SphereFit.distance-SphereFit.hyp_distance)
def shear_chi2(SphereFit):
    '''
    Function to evaluate the chi2 (diagonally) of a hypothesised shear field
    relative to a reference dataset with know error. Uses the SphereFit class
    :param SphereFit:
    :return:
    '''
    chi2 = nfield_diag_chi2(SphereFit.shear_hyp, SphereFit.shear_data)
    SphereFit.distance = chi2
    SphereFit.delta_hyp = chi2 # TODO Correct this for likelihood
    return


def MetropolisHastings(SphereFit):
    '''
    Function to apply the Metropolis-Hastings sampling technique using the current state of the SphereFit
    object.
    :param SphereFit:
    :return:
    '''
    sample = np.random.uniform(0,1)
    if sample <= SphereFit.delta_hyp:
        SphereFit.accept = True
        return
    SphereFit.accept = False
    return