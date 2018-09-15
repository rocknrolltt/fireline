from osgeo import gdal
from osgeo import osr
#import numpy
from osgeo.gdalconst import *


##Beginning Entry:
emptygrid=np.zeros(shape=[3501,7001],dtype=int)
text=open("O:\\buildingSegmentation\\finaloutCSV\\California.csv","r")

ds = gdal.Open("C:\\ting\\Hail\\hailbatch\\allstate\\lastyearhail.tif")

band1=ds.GetRasterBand(1)
gt = ds.GetGeoTransform()
srs = osr.SpatialReference()
srs.ImportFromWkt(ds.GetProjection())
#print ds.GetProjection()
srslatlong = srs.CloneGeogCS()
	
ct = osr.CoordinateTransformation(srslatlong,srs)

	
	
#print "reading raster"
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
                emptygrid[y][x]=emptygrid[y][x]+1

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
		lat=float(row[1])
		#print lat
		lon=float(row[0])
		#st=row[0]
		#zip=row[1]
		#print claim
		value1=latlon2pixel([lat,lon])
		#print value1

	except Exception,e: 
		print str(e)


			

text.close()
driver=gdal.GetDriverByName('gtiff')
	#driver.Register()
outDs=driver.Create('C:\\ting\\fireline\\stateupdates\\201711\\pointdensity.tiff',7001,3501,1,gdal.GDT_Int32)
outBand=outDs.GetRasterBand(1)
outBand.WriteArray(emptygrid,0,0)
outDs.SetGeoTransform(gt)
outDs.SetProjection(ds.GetProjection())
	
outBand.FlushCache()
ds=None
#numpy.savetxt('tomtomhds_1y.csv',final,delimiter=",",fmt='%s')
	
