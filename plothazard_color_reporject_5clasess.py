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

nonzone='#000000'
zone_1='#267300'
zone_2='#FFFF00'
zone_3='#FFAA00'
#zone_4='#FF5500'
zone_4='#A80000'
#crs = ccrs.UTM(zone=10)
crs= ccrs.PlateCarree(globe=ccrs.Globe(datum='WGS84',ellipse='WGS84'))
ax = plt.axes(projection=crs)


#CAcountylist=["ala","alp","ama","bte","cal","cco","col","del","eld","fre","gln","hmb","imp","iny","kng","krn","lag","lak","las","mad",
			 # "mar","men","mer","mnt","mod","mon","mrp","nap","nev","org","pla","plu","riv","sac","sbb","sbn","sbr","scl","sdg","sfr",
			 #"sha","sir","sis","sjq","slo","smt","snc","sol","son","sta","sut","teh","tlm","trn","tul","ven","yol","yub"]
COcountylist=["ads","alm","ara","arc","bac","bld","bmf","bnt","cek","cha","chy","cnj","cos","cus","cwl","den","det","dol","dug",
			"eag","elb","fem","gaf","glp","gra","gun","hin","hue","jak","jfe","kit","kiw","laa","lap","lar","lgn","lke","lnk","mes","mff","min","mor","mot","mtz","ote","our","pas","php",
			"pky","prw","ptk","pub","rib","rig","rtt","saj","sam","sau","sed","smm","tll","uma","wel","wtn"]
WAcountylist=["ams","aso","ben","che","clm","cak","clu","cow","dog","fer","fra","gar","gnt","grh","isl","jef","kin","ksp","ktt","kli","lew","lkn","mas","oka","pac","peo","prc","sjn","ska","skm","sno","spk","ste","thu","wkk","wal","whc","whm","yak"]
#ABcountylist=["a10","a11","a12","a13","a14","a15","a16","a17","a18","a19","a20","a21","a22","a23","ab1","ab2","ab3","ab4","ab5","ab6","ab7","ab8","ab9","a24","a25"]
#BCcountylist=["pcr","kts","sti","pll","ssc","sth","tpn","alb","boo","bun","cap","cko","cov","csh","ctc","cto","eko","ffg","frv","grv","kob","mox","mtw","nan","nro","nto","oks","sqc","squ"]

#plt.show()



#fig, ax = plt.subplots()
for county in COcountylist:
	# try:
		# os.remove('V:/FireLine/FireRing/Hartford2015/CA/%s/%s_reprojected_5classes.tif')
	# except OSError:
		# pass
    if not os.path.exists('O:/travellers_testing_2/ArcFireLine/CO/%s/%sfrshiag'%(county,county)):
        os.makedirs('O:/travellers_testing_2/ArcFireLine/CO/%s/%sfrshiag'%(county,county))
	os.system('gdalwarp O:/travellers_testing_2/ArcFireLine/FireRing/GRID/CO/%s/%sfrshiag/w001001.adf O:/travellers_testing_2/ArcFireLine/CO/%s/%sfrshiag/w001001.adf -t_srs "+proj=longlat +ellps=WGS84"'%(county,county,county,county))
	print "ok"
	with rasterio.drivers():
		with rasterio.open(r"O:/travellers_testing_2/ArcFireLine/CO/%s/%sfrshiag/w001001.adf"%(county,county),"r") as src:
			meta = src.meta
			im=src.read().astype('f')
			im=np.transpose(im,[1,2,0])
			print im.shape
			print im.min(),im.max()
			#im[im==0]=np.nan
			im[im==255]=np.nan
			im=im.squeeze()
			xmin = src.transform[0]
			xmax = src.transform[0] + src.transform[1]*src.width
			print src.width,src.height
			ymin = src.transform[3] + src.transform[5]*src.height
			ymax = src.transform[3]
			colors=[nonzone,zone_1,zone_2,zone_3,zone_4]
			cmap=mpl.colors.ListedColormap([nonzone,zone_1,zone_2,zone_3,zone_4])
			bounds_color=[0,5,100,105,200,205,300,305,400,405]
			#ax.imshow(im)
			norm=mpl.colors.BoundaryNorm(bounds_color,cmap.N)
			print xmin,xmax,ymin,ymax
			ax.imshow(im, origin='upper', extent=[xmin,xmax,ymin,ymax], transform=crs, interpolation='nearest',cmap=cmap,norm=norm)
					

#bounds = df.geometry.bounds
#xmin = bounds.minx.min()
#xmax = bounds.maxx.max()
#ymin = bounds.miny.min()
#ymax = bounds.maxy.max()

####WA extent#####
#ax.set_xlim(-126,
            #-113)
#ax.set_ylim(42,
			 #49)
             
####CO extent#####
ax.set_xlim(-109,
            -100)
ax.set_ylim(34,
			41)			
####AB extent#####
#ax.set_xlim(-121,
            #-109)
#ax.set_ylim(48,
			#62)	
	
##BC extent#####
#ax.set_xlim(-141,
            #-112)
#ax.set_ylim(47,
			#63)

#CA Shapefile##
df=GeoDataFrame.from_file(r"O:\Inferno\F\ArcFireLine\Access\CO\COCounty.shp")

##AB Shapefile##
#df=GeoDataFrame.from_file(r"F:\ArcFireLine\Access\AB\ABCounty.shp")
#df=df.to_crs(epsg=26910)


#BC shapefile
#df=GeoDataFrame.from_file(r"F:\ArcFireLine\Access\BC\BCCounty.shp")
df.plot(axes=ax,alpha=0)
# df=df.to_crs(epsg=26910)

nonzone_patch=mpatches.Patch(color=nonzone, label='-')
zone1_patch = mpatches.Patch(color=zone_1, label='shia zone 1')
zone2_patch = mpatches.Patch(color=zone_2, label='shia zone 2')
zone3_patch = mpatches.Patch(color=zone_3, label='shia zone 3')
zone4_patch=mpatches.Patch(color=zone_4, label='shia zone 4')

plt.legend(handles=[nonzone_patch,zone1_patch,zone2_patch,zone3_patch,zone4_patch],loc=3)
	
#plot_margin = 0.1
#ax.set_extent((xmin, xmax, ymin, ymax))
#x0, x1, y0, y1 = plt.axis()
#plt.axis((x0 + plot_margin,
         #x1 + plot_margin,
         #y0 + plot_margin,
         # y1 + plot_margin))	

#plt.subplots_adjust(left=0.1, right=100, top=0.9, bottom=0.1)		
plt.show()
	