#from shapely.geometry import shape, mapping
#from shapely.ops import unary_union
#import fiona
#import itertools
import os
import ogr

ABcountylist=["a10","a11","a12","a13","a14","a15","a16","a17","a18","a19","a20","a21","a22","a23","ab1","ab2","ab3","ab4","ab5","ab6","ab7","ab8","ab9","a24","a25"]
BCcountylist=["alb"]#"boo","bun","cap","cko","cov","csh","ctc","cto","eko","ffg","frv","grv","kob","kts","mox","mtw","nan","nro","nto","oks","pcr","pll","sqc","squ","ssc","sth","sti","tpn"]

for county in ABcountylist:
    inpath="c:/ting/fireline/AB/firelineAB/%s" %county
    os.chdir(inpath)

    os.system('ogr2ogr %sloc_diss.shp %sloc_truc.shp  -dialect sqlite -sql "SELECT ST_Union(geometry),Hazard FROM %sloc_truc GROUP BY Hazard"' %(county,county,county))
    #shape = fiona.open("%sloc_truc.shp" %county)
    # newschema = {'geometry': 'Polygon',
                 # 'properties': {'Hazard': 'str:10'}}

    # with fiona.open("%sdissolve.shp"%county, "w", "ESRI Shapefile", newschema,crs=shape.crs) as output:
        # e = sorted(shape, key=lambda k: k['properties']['Hazard'])
        # for key, group in itertools.groupby(e, key=lambda x:x['properties']['Hazard']):
            # properties, geom = zip(*[(feature['properties'],shape(feature['geometry'])) for feature in group])
            # output.write({'geometry': mapping(unary_union(geom)), 'properties': properties[0]})
            # shape.close()
            # output.close()