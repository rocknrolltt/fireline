import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from osgeo import ogr

import matplotlib.pyplot as plt
import rasterio
import cartopy.crs as ccrs

import geopandas
from geopandas import *



MediumApple=(85.00,255.00,0.00)
Cantaloupe=(255.00,167.00,127.00)
Marsred=(255.00,0.00,0.00)
crs = ccrs.UTM(zone=10)
ax = plt.axes(projection=crs)



CAcountylist=["ala","alp","ama","bte","cal","cco","col","del","eld","fre","gln","hmb","imp","iny","kng","krn","lag","lak","las","mad",
			  "mar","men","mer","mnt","mod","mon","mrp","nap","nev","org","pla","plu","riv","sac","sbb","sbn","sbr","scl","sdg","sfr",
			  "sha","sir","sis","sjq","slo","smt","snc","sol","son","sta","sut","teh","tlm","trn","tul","ven","yol","yub"]
ABcountylist=["a10","a11","a12","a13","a14","a15","a16","a17","a18","a19","a20","a21","a22","a23","ab1","ab2","ab3","ab4","ab5","ab6","ab7","ab8","ab9"]
BCcountylist=["alb","boo","bun","cap","cko","cov","csh","ctc","cto","eko","ffg","frv","grv","kob","kts","mox","mtw","nan","nro","nto","oks","pcr","pll","sqc","squ","ssc","sth","sti","tpn"]

#fig, ax = plt.subplots()
for county in CAcountylist:
	with rasterio.drivers():
		with rasterio.open(r"V:\FireLine\FireRing\Hartford2015\CA\%s\%s.tif"%(county,county),"r") as src:
			meta = src.meta
			im=src.read().astype('f')
			im=np.transpose(im,[1,2,0])
			print im.shape
			print im.min(),im.max()
			im[im==0]=np.nan
			im=im.squeeze()
			xmin = src.transform[0]
			xmax = src.transform[0] + src.transform[1]*src.width
			print src.width,src.height
			ymin = src.transform[3] + src.transform[5]*src.height
			ymax = src.transform[3]
			
			
			#ax.imshow(im)
			print xmin,xmax,ymin,ymax
			
			

			ax.imshow(im, origin='upper', extent=[xmin,xmax,ymin,ymax], transform=crs, interpolation='nearest')
					
df=GeoDataFrame.from_file(r"V:\FireLine\Access\2014\CA\CACounty.shp")
df=df.to_crs(epsg=26910)
df.plot(axes=ax,alpha=0)
bounds = df.geometry.bounds
ax.set_xlim(bounds.minx.min(),
            bounds.maxx.max())
ax.set_ylim(bounds.miny.min(),
			bounds.maxy.max())
			
ax.margins(1,1)

			
plt.show()
	