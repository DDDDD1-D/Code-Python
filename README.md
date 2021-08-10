# Code-Python-ClimDiag

util目录下：

| 文件名                   | 备忘                                                         |
| ------------------------ | ------------------------------------------------------------ |
| conform_dim              | 用于扩展数组，conform_dim(a,b,(0,2,3))是把a扩展成b的维度，(0,2,3)表示b的这三维是a没有的 |
| draw_PlateCarree         | 画平面图的底图                                               |
| draw_polar_steoro        | 画极射赤面投影图的底图                                       |
| fourier_filter_high_pass | 对时间序列做high pass傅立叶滤波                              |
| Linear_Regression_dim    | 线性回归                                                     |
| lonFlip                  | 转换lon坐标，-180～180和0～360转换                           |
| mon2season               | 月数据转换为三个月季节平均                                   |
| obtain_coords_dict       | 获得xarray变量的坐标信息                                     |
| standardization          | 标准化                                                       |
| tibet_shp_load           | 加载青藏高原轮廓                                             |
| tnflux                   | 计算TN Wave Activity Flux                                    |
| water_vapor_flux         | 计算水汽通量和水汽通量散度，以及它们的垂直积分               |
| composite                | 合成分析                                                     |
| load_ncl_colormap        | 加载ncl的colormap                                            |
| Q1                       | 计算Q1                                                       |
| draw_ts                  | 画时间序列                                                   |
| epflux                   | 计算EP flux                                                  |
| vertical_integration     | 垂直积分                                                     |
| uv2div_cfd               | ncl中的uv2div_cfd计算                                        |
| ck                       | 计算正压能量转换CK                                           |

example目录下是应用utils进行计算的结果，与ncl完全一致
