import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from osgeo import ogr

import matplotlib.pyplot as plt
import matplotlib as mpl
import rasterio
from rasterio.merge import merge
import cartopy.crs as ccrs

import geopandas
from geopandas import *
import os

from matplotlib import colors
import matplotlib.patches as mpatches




CAcountylist=["ala","alp","ama","bte","cal","cco","col","del","eld","fre","gln","hmb","imp","iny","kng","krn","lag","lak","las","mad",
			 "mar","men","mer","mnt","mod","mon","mrp","nap","nev","org","pla","plu","riv","sac","sbb","sbn","sbr","scl","sdg","sfr",
			 "sha","sir","sis","sjq","slo","smt","snc","sol","son","sta","sut","teh","tlm","trn","tul","ven","yol","yub"]
#COcountylist=["ads","alm","ara","arc","bac","bld","bmf","bnt","cek","cha","chy","cnj","cos","cus","cwl","den","det","dol","dug",
			#"eag","elb","fem","gaf","glp","gra","gun","hin","hue","jak","jfe","kit","kiw","laa","lap","lar","lgn","lke","lnk","mes","mff","min","mor","mot","mtz","ote","our","pas","php",
			#"pky","prw","ptk","pub","rib","rig","rtt","saj","sam","sau","sed","smm","tll","uma","wel","wtn"]
#WAcountylist=["ams","aso","ben","che","clm","cak","clu","cow","dog","fer","fra","gar","gnt","grh","isl","jef","kin","ksp","ktt","kli","lew","lkn","mas","oka","pac","peo","prc","sjn","ska","skm","sno","spk","ste","thu","wkk","wal","whc","whm","yak"]
#ABcountylist=["a10","a11","a12","a13","a14","a15","a16","a17","a18","a19","a20","a21","a22","a23","ab1","ab2","ab3","ab4","ab5","ab6","ab7","ab8","ab9","a24","a25"]
#BCcountylist=["pcr","kts","sti","pll","ssc","sth","tpn","alb","boo","bun","cap","cko","cov","csh","ctc","cto","eko","ffg","frv","grv","kob","mox","mtw","nan","nro","nto","oks","sqc","squ"]

#plt.show()


src_files_to_mosaic=[]
outfp=r"O:\travellers_testing\fireringmosaic.tiff"
#fig, ax = plt.subplots()
for county in CAcountylist:

	with rasterio.drivers():
		src=rasterio.open(r"O:/travellers_testing/ArcFireLine/FireRing/FRoldSHIA/CA/%s/%sfroshia.img"%(county,county),"r")

		src_files_to_mosaic.append(src)



mosaic,out_trans=merge(src_files_to_mosaic)
mosaic=mosaic.astype(np.uint16)
with rasterio.drivers():
	with rasterio.open(outfp,"w",driver="GTiff",count=1,dtype="uint16",nodata=0,compress="lzw",height=mosaic.shape[1],width=mosaic.shape[2],transform=out_trans,crs="EPSG:26910") as dest:
		dest.write(mosaic)
	