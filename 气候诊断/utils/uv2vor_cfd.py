import numpy as np

def uv2vor_cfd(uwnd, vwnd, lat, lon):
	lat = np.array(lat * np.pi / 180.0) 
	lon = np.array(lon * np.pi / 180.0 )

	xx, yy = np.meshgrid(lon, lat)

	dx = np.cos(yy) * np.gradient(xx, axis=1) * 6378388.0
	dy = np.gradient(yy,axis=0) * 6378388.0

	dv_dx = np.gradient(vwnd, axis=2)/dx.reshape(1,np.shape(lat)[0],np.shape(lon)[0])
	du_dy = np.gradient(uwnd, axis=1)/dy.reshape(1,np.shape(lat)[0],np.shape(lon)[0])

	vr = dv_dx - du_dy + uwnd/6378388.0*(np.tan(yy).reshape(1,np.shape(lat)[0],np.shape(lon)[0]))

	return div