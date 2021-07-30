import numpy as np
import xarray as xr
import metpy.calc as mp
from conform_dim import conform_dim
from obtain_coords_dict import obtain_coords_dict

def specific_humidity_from_relative_humidity(rh, p, tk):
	mixing_ratio = mp.mixing_ratio_from_relative_humidity(p, tk, rh)
	sp = mp.specific_humidity_from_mixing_ratio(mixing_ratio)
	if "time" in sp.coords and np.shape(sp['time'])!=(): sp = sp.transpose("time",...)

	return  sp


def water_vapor_flux_div_column(sp, uwnd, vwnd, lat, lon, level):
	uq = sp * uwnd
	vq = sp * vwnd

	uq_int = vertical_integration(uq, level) / 9.8
	vq_int = vertical_integration(vq, level) / 9.8

	div = uv2div_cfd(uq_int, vq_int, lat, lon)

	coords = obtain_coords_dict(sp[:,0,:,:])

	uq_int = xr.DataArray(uq_int, coords=coords)
	vq_int = xr.DataArray(vq_int, coords=coords)
	div = xr.DataArray(div, coords=coords)

	return uq_int, vq_int, div


def vertical_integration(var, level):
	nz = np.shape(level)[0]
	dp = level.values[0:nz-2] - level.values[1:nz-1]

	var_new = (var.values[:,0:nz-2,:,:] + var.values[:,1:nz-1,:,:]) / 2.0
	dpp = conform_dim(dp, var_new, (0,2,3))

	var_int = np.sum(var_new*dpp, axis=1)

	return var_int


def uv2div_cfd(uwnd, vwnd, lat, lon):
	lat = np.array(lat * np.pi / 180.0) 
	lon = np.array(lon * np.pi / 180.0 )

	xx, yy = np.meshgrid(lon, lat)

	dx = np.cos(yy) * np.gradient(xx, axis=1) * 6378388.0
	dy = np.gradient(yy,axis=0) * 6378388.0

	du_dx = np.gradient(uwnd, axis=2)/dx.reshape(1,np.shape(lat)[0],np.shape(lon)[0])
	dv_dy = np.gradient(vwnd, axis=1)/dy.reshape(1,np.shape(lat)[0],np.shape(lon)[0])

	div = du_dx + dv_dy - vwnd/6378388.0*(np.tan(yy).reshape(1,np.shape(lat)[0],np.shape(lon)[0]))

	return div

