""" Comparison of luminsoity distances obtained from a
Cosmological calculator and the astropy module.

Note: This project did not use redshift above 0.3. 
"""

from Cosmological_calculator_scale_distance import lum_distance
from astropy.cosmology import FlatLambdaCDM
from astropy import units as u
cosmo = FlatLambdaCDM(H0=70, Om0=0.3)

import matplotlib.pyplot as plt
import numpy as np

for redshift in np.arange(0.0, 0.3, 0.05):
	cosmo_cal_pc = float(lum_distance(redshift))
	astropy_pc = cosmo.luminosity_distance(redshift) / u.Mpc
	#~ print cosmo_cal_pc, astropy_pc
	plt.plot(cosmo_cal_pc, astropy_pc, marker = "o")
	plt.plot(astropy_pc, astropy_pc, marker = ".", color = "b")
#~ percentage_diff = 100.0 * abs(cosmo_cal_pc -astropy_pc)/astropy_pc
#~ print '%1.2f' % percentage_diff + "% difference"
plt.xlabel("Mpcs, from Cosmological_calculator")
plt.ylabel("Mpcs, from astropy")
plt.show()
