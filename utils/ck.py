import numpy as np
from vertical_integration import vertical_integration

def ck(ua, va, dudx, dvdy, dudy, dvdx):
	ck = (va*va - ua*ua) / 2.0 * (dudx - dvdy) - ua * va * (dudy + dvdx)
	return ck


def ke(ua, va):
	ke = (ua*ua + va*va) / 2.0
	return ke