from osgeo import gdal
import sys,os
import numpy




#CAcountylist=["ala","alp","ama","bte","cal","cco","col","del","eld","fre","gln","hmb","imp","iny","kng","krn","lag","lak","las","mad",
			 # "mar","men","mer","mnt","mod","mon","mrp","nap","nev","org","pla","plu","riv","sac","sbb","sbn","sbr","scl","sdg","sfr",
			 # "sha","sir","sis","sjq","slo","smt","snc","sol","son","sta","sut","teh","tlm","trn","tul","ven","yol","yub"]
ABcountylist=["a10","a11","a12","a13","a14","a15","a16","a17","a18","a19","a20","a21","a22","a23","ab1","ab2","ab3","ab4","ab5","ab6","ab7","ab8","ab9","a24","a25"]
BCcountylist=["sti"]#["kts","pcr"]##["alb","boo","bun","cap","cko","cov","csh","ctc","cto","eko","ffg","frv","grv","kob",,"mox","mtw","nan","nro","nto","oks",,"pll","sqc","squ","ssc","sth",,"tpn"]

for county in ABcountylist:
	ds=gdal.Open("V:/FireLine/FireRing/Hartford2015/AB/%s/%scounty.tiff"%(county,county))
	if ds is None:
		sys.exit("Error:can't open raster")

	gt=ds.GetGeoTransform()

	raster=ds.ReadAsArray()
	print raster.shape

	raster[(raster>=0) & (raster<= 1)]=1
	raster[(raster>=2) & (raster< 3)]=2
	raster[(raster>=4) & (raster<30)]=3

	driver=gdal.GetDriverByName('gtiff')
	try:
		os.remove("V:/FireLine/FireRing/Hartford2015/AB/%s/%s.tiff"%(county,county))
	except OSError:
		pass
	outDs=driver.Create("V:/FireLine/FireRing/Hartford2015/AB/%s/%s.tiff"%(county,county),raster.shape[1],raster.shape[0],1,gdal.GDT_Int32)
	outDs.SetProjection(ds.GetProjection())
	outDs.SetGeoTransform(gt)
	outDs.GetRasterBand(1).WriteArray(raster)




	ds=None
	outDs=None


