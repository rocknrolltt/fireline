import os,subprocess
import gdal,gdalconst,numpy,ogr,osgeo
from osgeo import gdal
import sys
import numpy

#countylist=["apa"]#,"cno"]#,"coc","cuz","gee","ghm","gla","moh","mrc","nav","paz","pin","pma","yav","yma"]
CAcountylist=["ala","alp","ama","bte","cal","cco","col","del","eld","fre","gln","hmb","imp","iny","kng","krn","lag","lak","las","mad",
			  "mar","men","mer","mnt","mod","mon","mrp","nap","nev","org","pla","plu","riv","sac","sbb","sbn","sbr","scl","sdg","sfr",
			  "sha","sir","sis","sjq","slo","smt","snc","sol","son","sta","sut","teh","tlm","trn","tul","ven","yol","yub"]
ABcountylist=["a10","a11","a12","a13","a14","a15","a16","a17","a18","a19","a20","a21","a22","a23","ab1","ab2","ab3","ab4","ab5","ab6","ab7","ab8","ab9","a24","a25"]
BCcountylist=["alb","boo","bun","cap","cko","cov","csh","ctc","cto","eko","ffg","frv","grv","kob","kts","mox","mtw","nan","nro","nto","oks","pcr","pll","sqc","squ","ssc","sth","sti","tpn"]
# for county in CAcountylist:
	# inpath="F:/ArcFireLine/FireRing/Hartford/CA/%s" %county
	# # infile="%sloc.shp" %county
	# os.chdir(inpath)
	
	# if not os.path.exists("V:/FireLine/FireRing/Hartford2015/CA/%s"%(county)):
		# os.makedirs("V:/FireLine/FireRing/Hartford2015/CA/%s"%(county))
	# # outpath="C:/ting/fireline/wildfire/CA/%s"%(county)
	# # file_nc="%scounty.tiff"%(county)
	# # outputf=os.path.join(outpath,file_nc)
	# os.system("gdal_rasterize -a AREASCORE -ot Byte -tr 30 30 -a_nodata 255 -of GTiff -l %sloc %sloc.shp V:/FireLine/FireRing/Hartford2015/CA/%s/%scounty.tiff" %(county,county,county,county))
	

for county in ABcountylist:
	inpath=r"C:\ting\fireline\AB\%s" %county
	#inpath="F:/ArcFireLine/FireRing/Hartford2014/AB/%s" %county
	os.chdir(inpath)
	print inpath
	# if not os.path.exists("V:/FireLine/FireRing/Hartford2015/AB/%s"%(county)):
		# os.makedirs("V:/FireLine/FireRing/Hartford2015/AB/%s"%(county))
	try:
		os.remove("C:/ting/fireline/AB/%s/%sloc_dis.shp"%(county,county))
	except OSError:
		pass
	os.system('ogr2ogr %sloc_dis.shp %sloc.shp  -dialect sqlite -sql "SELECT ST_Union(geometry),AREASCORE FROM %sloc GROUP BY AREASCORE"' %(county,county,county))
	
# for county in BCcountylist:
	# inpath="F:/ArcFireLine/FireRing/Hartford/BC/%s" %county
	# os.chdir(inpath)
	
	# if not os.path.exists("V:/FireLine/FireRing/Hartford2015/BC/%s"%(county)):
		# os.makedirs("V:/FireLine/FireRing/Hartford2015/BC/%s"%(county))
	# os.system("gdal_rasterize -a AREASCORE -ot Byte -tr 30 30 -a_nodata 255 -of GTiff -l %sloc %sloc.shp V:/FireLine/FireRing/Hartford2015/BC/%s/%scounty.tiff" %(county,county,county,county))