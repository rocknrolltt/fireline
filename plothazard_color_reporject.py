import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from osgeo import ogr

import matplotlib.pyplot as plt
import matplotlib as mpl
import rasterio
import cartopy.crs as ccrs

import geopandas
from geopandas import *
import os

from matplotlib import colors
import matplotlib.patches as mpatches


MediumApple='#55FF00'
Cantaloupe='#FFaa00'
Marsred='#FF0000'
#crs = ccrs.UTM(zone=10)
crs= ccrs.PlateCarree(globe=ccrs.Globe(datum='WGS84',ellipse='WGS84'))
ax = plt.axes(projection=crs)


#CAcountylist=["ala","alp","ama","bte","cal","cco","col","del","eld","fre","gln","hmb","imp","iny","kng","krn","lag","lak","las","mad",
			  #"mar","men","mer","mnt","mod","mon","mrp","nap","nev","org","pla","plu","riv","sac","sbb","sbn","sbr","scl","sdg","sfr",
			 #"sha","sir","sis","sjq","slo","smt","snc","sol","son","sta","sut","teh","tlm","trn","tul","ven","yol","yub"]
ABcountylist=["a10","a11","a12","a13","a14","a15","a16","a17","a18","a19","a20","a21","a22","a23","ab1","ab2","ab3","ab4","ab5","ab6","ab7","ab8","ab9","a24","a25"]
#BCcountylist=["pcr","kts","sti","pll","ssc","sth","tpn","alb","boo","bun","cap","cko","cov","csh","ctc","cto","eko","ffg","frv","grv","kob","mox","mtw","nan","nro","nto","oks","sqc","squ"]

#plt.show()



#fig, ax = plt.subplots()
for county in ABcountylist:
	try:
		os.remove("V:/FireLine/FireRing/Hartford2015/AB/%s/%s_reprojected.tif"%(county,county))
	except OSError:
		pass
	os.system('gdalwarp V:/FireLine/FireRing/Hartford2015/AB/%s/%s.tiff V:/FireLine/FireRing/Hartford2015/AB/%s/%s_reprojected.tif -t_srs "+proj=longlat +ellps=WGS84"'%(county,county,county,county))
	print "ok"
	with rasterio.drivers():
		with rasterio.open(r"V:\FireLine\FireRing\Hartford2015\AB\%s\%s_reprojected.tif"%(county,county),"r") as src:
			meta = src.meta
			im=src.read().astype('f')
			im=np.transpose(im,[1,2,0])
			print im.shape
			print im.min(),im.max()
			im[im==0]=np.nan
			im[im==255]=np.nan
			im=im.squeeze()
			xmin = src.transform[0]
			xmax = src.transform[0] + src.transform[1]*src.width
			print src.width,src.height
			ymin = src.transform[3] + src.transform[5]*src.height
			ymax = src.transform[3]
			colors=[MediumApple,Cantaloupe,Marsred]
			cmap=mpl.colors.ListedColormap([MediumApple,Cantaloupe,Marsred])
			bounds_color=[1,1,2,2,3,3]
			#ax.imshow(im)
			norm=mpl.colors.BoundaryNorm(bounds_color,cmap.N)
			print xmin,xmax,ymin,ymax
			ax.imshow(im, origin='upper', extent=[xmin,xmax,ymin,ymax], transform=crs, interpolation='nearest',cmap=cmap,norm=norm)
					

#bounds = df.geometry.bounds
#xmin = bounds.minx.min()
#xmax = bounds.maxx.max()
#ymin = bounds.miny.min()
#ymax = bounds.maxy.max()

####CA extent#####
#ax.set_xlim(-125,
            #-113)
#ax.set_ylim(32,
			#43)
			
####AB extent#####
ax.set_xlim(-121,
            -109)
ax.set_ylim(48,
			62)	
	
##BC extent#####
# ax.set_xlim(-141,
            # -112)
# ax.set_ylim(47,
			# 63)

#CA Shapefile##
#df=GeoDataFrame.from_file(r"V:\FireLine\Access\2014\CA\CACounty.shp")

##AB Shapefile##
df=GeoDataFrame.from_file(r"F:\ArcFireLine\Access\AB\ABCounty.shp")
#df=df.to_crs(epsg=26910)


#BC shapefile
#df=GeoDataFrame.from_file(r"F:\ArcFireLine\Access\BC\BCCounty.shp")
df.plot(axes=ax,alpha=0)
# df=df.to_crs(epsg=26910)

low_patch = mpatches.Patch(color='#55FF00', label='Low')
Moderate_patch = mpatches.Patch(color='#FFaa00', label='Moderate')
High_patch = mpatches.Patch(color='#FF0000', label='High')

plt.legend(handles=[low_patch,Moderate_patch,High_patch],loc=3)
	
#plot_margin = 0.1
#ax.set_extent((xmin, xmax, ymin, ymax))
#x0, x1, y0, y1 = plt.axis()
#plt.axis((x0 + plot_margin,
         #x1 + plot_margin,
         #y0 + plot_margin,
         # y1 + plot_margin))	

#plt.subplots_adjust(left=0.1, right=100, top=0.9, bottom=0.1)		
plt.show()
	