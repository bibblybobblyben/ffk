import numpy as np
import healpy as hp


def save_healpy_at_intervals(SphereFit, interval = 10**3):
    if SphereFit.iter % interval:
        hp.fitsfunc.write_map(SphereFit.output_loc + f"Step{SphereFit.iter}.fits", SphereFit.hyp)