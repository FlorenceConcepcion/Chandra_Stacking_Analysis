from Cosmological_calculator_scale_distance \
	import lum_distance 

def Galaxy_SDSS_uz_mass(redshift, u_obs_mag, z_obs_mag, M_sun_abs_z = 4.51):
	"""#total mass of the galaxy using sdss magnitude data
	inputs:
	redshift	redshift
	u_obs_mag	observed magnitude in SDSS u band
	z_obs_mag	observed magnitude in SDSS z band
	"""
	#~ distance in pc
	distance_parsecs = float(lum_distance(redshift)) * (10**6)		 
	m_obs_z = z_obs_mag
	luminosity_z =  ((distance_parsecs **2.0)/100.0) * \
					(10**((2.0/5.0)*(M_sun_abs_z - m_obs_z)))
	color_index = u_obs_mag - z_obs_mag
	a_z = -0.179; b_z=0.151
	M_L_ratio = 10**(a_z+ (b_z*color_index))
	mass_z = luminosity_z * M_L_ratio
	return mass_z	

