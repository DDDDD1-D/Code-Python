import numpy as np
import xarray as xr
from obtain_coords_dict import obtain_coords_dict

def Q1(dswrf_ntat, prate, shtfl, ulwrf_ntat, uswrf_ntat, nswrs, nlwrs):
	q1 = dswrf_ntat.values - ulwrf_ntat.values - uswrf_ntat.values + nswrs.values + nlwrs.values + shtfl.values + prate.values*2510600.832

	coords = obtain_coords_dict(dswrf_ntat)

	q1 = xr.DataArray(q1, coords=coords)

	return q1