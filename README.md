# Chandra_Stacking_Analysis

Currently contains: 
- **Cosmological_calculator_scale_distance.py**: 
Edited Python file of the cosmological calculator obtained from: http://www.astro.ucla.edu/~wright/CosmoCalc.html It has been edited to return the luminsoity distance, Mpc, and the "scale factor" relation, kpc/", (between arcseconds in the sky and the coresponding kpc) of objects at a given redshift. 
- **compare_lum_distances.py**:
Comparison of luminsoity distances obtained from **Cosmological_calculator_scale_distance.py** and the astropy module. The largest difference of 0.84% is at the largest redshift used in this project, z = 0.3.  
