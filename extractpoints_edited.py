from osgeo import gdal
from osgeo.gdalconst import *
from osgeo import osr
import numpy
text = numpy.genfromtxt("V:/FireLine/Batch/Scripts/wildfire/AZ_try.txt",delimiter='\t',dtype=None,skiprows=1)
countylist=["apa","cno","coc","cuz","gee","ghm","gla","moh","mrc","nav","paz","pin","pma","yav","yma"]
AZscorefinal=[]
for county in countylist:
	#reading areafuel image"
	aflist="F:/ArcFireLine/FireRing/FRoldSHIA2014/AZ/%s/%sfroshia.img"%(county,county)
	print aflist
	ds1 = gdal.Open(aflist)
	band2=ds1.GetRasterBand(1)
	gt1 = ds1.GetGeoTransform()
	srs1 = osr.SpatialReference()
	srs1.ImportFromWkt(ds1.GetProjection())
	srslatlong1 = srs1.CloneGeogCS()
	ct1 = osr.CoordinateTransformation(srslatlong1,srs1)
	ras1 = band2.ReadAsArray()
	ds1=None
	
	#reading fuel and slope image"
	fuelslopelist="F:/ArcFireLine/FireRing/Mosaic2014/AZ/%s/%smosaic.img"%(county,county)
	print fuelslopelist
	ds=gdal.Open(fuelslopelist)
	band1=ds.GetRasterBand(1)
	gt = ds.GetGeoTransform()
	srs = osr.SpatialReference()
	srs.ImportFromWkt(ds.GetProjection())
	srslatlong = srs.CloneGeogCS()
	ct = osr.CoordinateTransformation(srslatlong,srs)
	ras2 = band1.ReadAsArray()
	ds=None
	
	# reading access image"
	accesslist="F:/ArcFireLine/Hazard/GRID/AZ/%s/%shazg/w001001.adf" %(county,county)
	print accesslist
	ds2=gdal.Open(accesslist)
	band3=ds2.GetRasterBand(1)
	gt2=ds2.GetGeoTransform()
	srs2=osr.SpatialReference()
	srs2.ImportFromWkt(ds2.GetProjection())
	srslatlong2 = srs2.CloneGeogCS()
	ct2 = osr.CoordinateTransformation(srslatlong2,srs2)
	ras3 = band3.ReadAsArray()
	ds2=None
	def areafuel(latlonpairs):
		print "running function areafuel"
		point = latlonpairs
		(point[1],point[0],holder) = ct1.TransformPoint(point[1],point[0])
		x = (point[1] - gt1[0])/gt1[1]
		y = (point[0] - gt1[3])/gt1[5]
		try:
			value1 = ras1[int(y),int(x)]
			#print "arefuel"
			#print value1
			return value1
		except IndexError:
			return 
		
	def fuelslope(latlonpairs):
		print "running function fuelslope"
		point = latlonpairs
		(point[1],point[0],holder) = ct.TransformPoint(point[1],point[0])
		x = (point[1] - gt[0])/gt[1]
		y = (point[0] - gt[3])/gt[5]
		try:
			value2 = ras2[int(y),int(x)]
			#print "slopefuel="
			#print  value2
			return value2
		except IndexError:
			return 
			

	def accessore(latlonpairs):
		print "running accessore"
		point = latlonpairs
		(point[1],point[0],holder) = ct2.TransformPoint(point[1],point[0])
		x = (point[1] - gt2[0])/gt2[1]
		y = (point[0] - gt2[3])/gt2[5]
		try:
			value3 = ras3[int(y),int(x)]
			#print "access="
			#print value3
			return value3
		except IndexError:
			return 
		
	
	
	
	
	for row in text:
		#claim=row[1]
		
		lat=row[3]
		lon=row[2]
		#Shia=row[2]
		#print lat,lon
		value1=areafuel([lat,lon])
		value2=fuelslope([lat,lon])
		value3=accessore([lat,lon])
		access=value3
		if value3>=11 and value3>=46:
			access="A0"
		elif value3>=61 and value<=96:
			access="A1"
		elif value3>=111 and value3<=146:
			access="A3"
		elif value3>=161 and value3<=194:
			access="A5"
		else:
			access=999
		if value1>=0 and value1<110 and value2>0 and value2<60:
			AF=value1
			slope=value2/10
			if value2%10==4:
				Fuel="NF"
			elif value2%10==6:
				Fuel="WA"
			elif value2%10==5 or value2%10 ==0:
				Fuel="F0"
			elif value2%10==2:
				Fuel="F3"
			elif value2%10==3:
				Fuel="F5"
			else:
				Fuel="F1"
			
			if slope==4:
				if lon and lat not in AZscorefinal:
					AZscorefinal.append([row[0],row[1],lon,lat,AF,"5",Fuel,access])
			else:
				if lon and lat not in AZscorefinal:
					AZscorefinal.append([row[0],row[1],lon,lat,AF,slope,Fuel,access])
		else:
			print value1,value2
		
	# ds1=None
	# ds=None
	# ds2=None


numpy.savetxt('V:/FireLine/Batch/Scripts/wildfire/AZscore.txt',AZscorefinal,delimiter="\t",fmt='%s')
