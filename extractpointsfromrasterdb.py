from osgeo import gdal
from osgeo import osr
#import numpy
from osgeo.gdalconst import *


##Beginning Entry:

text=open("C:\\ting\\Hail\\hailbatch\\allstate\\verisk_inp800k_addressfields.csv","r")
writer1=open("C:\\ting\\Hail\\hailbatch\\allstate\\results\\allstate_lastyearhail.csv","w")
ds = gdal.Open("C:\\ting\\Hail\\hailbatch\\allstate\\lastyearhail.tif")

band1=ds.GetRasterBand(1)
gt = ds.GetGeoTransform()
srs = osr.SpatialReference()
srs.ImportFromWkt(ds.GetProjection())
print ds.GetProjection()
srslatlong = srs.CloneGeogCS()
	
ct = osr.CoordinateTransformation(srslatlong,srs)

	
	
print "reading raster"
ras = band1.ReadAsArray()

latlonpairs = []
def latlon2pixel(latlonpairs):
	
	point = latlonpairs
	

	
	#print point
	#print enumerate(latlonpairs)
	#print ct.TransformPoints(point[1],point[0])
	(point[1],point[0],holder) = ct.TransformPoint(point[1],point[0])
	#print "done"
	x = (point[1] - gt[0])/gt[1]
	y = (point[0] - gt[3])/gt[5]
	
	try:
		value1 = ras[int(y),int(x)]
		#print value1
		
	except Exception,e:
		value1=999 
	return value1
	
	#values.append(value1)


	
line=text.readline()
#final=[]
while line!="":
	#print line
	try:
		line=text.readline()
		line=line.strip('\n')
		row=line.split(",")
		#print row
		#claim=row[1]
		#print claim
		lat=float(row[-1])
		#print lat
		lon=float(row[-2])
		#st=row[0]
		#zip=row[1]
		#print claim
		value1=latlon2pixel([lat,lon])
		#print value1
		
		if (int(value1)>=0 and int(value1)<=9999):
			writer1.write(line+","+str(value1)+'\n')
			#print "appended"
	except Exception,e: 
		print str(e)


			
ds = None
text.close()
writer1.close()
#numpy.savetxt('tomtomhds_1y.csv',final,delimiter=",",fmt='%s')
	
