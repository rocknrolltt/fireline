import os,subprocess,osr
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


for county in BCcountylist:
	inpath=r"V:\FireLine\FireRing\Hartford2015\BC\%s" %county
	#inpath="F:/ArcFireLine/FireRing/Hartford2014/AB/%s" %county
	os.chdir(inpath)
	sourceRaster=gdal.Open('%s_5classes.tiff'%county)
	band=sourceRaster.GetRasterBand(1)
	outShapefile="%spoly"%county
	driver=ogr.GetDriverByName("ESRI Shapefile")
	if os.path.exists(outShapefile+".shp"):
		driver.DeleteDataSource(outShapefile+".shp")
	outDatasource = driver.CreateDataSource(outShapefile+ ".shp")
	prj=osr.SpatialReference()
	prj.SetWellKnownGeogCS("EPSG:4326")
	outLayer = outDatasource.CreateLayer("%spoly"%county, srs=prj)
	newField = ogr.FieldDefn('AREASCORE', ogr.OFTInteger)
	outLayer.CreateField(newField)
	gdal.Polygonize(band, None, outLayer, 0, [], callback=None)
	#os.system('ogr2ogr %spoly_dis.shp %spoly.shp  -dialect sqlite -sql "SELECT ST_Union(geometry),AREASCORE FROM %spoly GROUP BY AREASCORE"' %(county,county,county))
	fieldDefn=ogr.FieldDefn("Hazard",ogr.OFTString)
	#ds=driver.Open('%spoly_dis.shp'%county,1)
	#lyr=ds.GetLayer()
	outLayer.CreateField(fieldDefn)
	feature=outLayer.GetNextFeature()
	while feature:
		Value=feature.GetField('AREASCORE')
		if Value == 31:
			newVal='Neglibile'
		if Value==32:
			newVal='Low'
		if Value==33:
			newVal='Moderate'
		if Value==34:
			newVal='High'
		if Value==35:
			newVal='Extreme'
		feature.SetField('Hazard',newVal)
		outLayer.SetFeature(feature)
		feature=outLayer.GetNextFeature()
	#os.system('ogr2ogr %spoly_1field.shp %spoly.shp  -dialect sqlite -sql "SELECT Hazard FROM %spoly"' %(county,county,county))
	outDatasource.Destroy()
	#ds.Destroy()
	sourceRaster = None
	