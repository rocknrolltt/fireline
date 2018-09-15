import fiona

shape = fiona.open("D:/tiger/scratch/a10/a10loc.shp")
newschema = {'geometry': 'Polygon',
             'properties': {'Hazard': 'str:10'}}

with fiona.open("D:/tiger/scratch/a10/a10loc_truc.shp",'w','ESRI Shapefile',newschema,crs=shape.crs) as output:
    for feat in shape:
        if feat['properties']['AREASCORE'] == 0:
            hazard = 'Negligible'
        if feat['properties']['AREASCORE'] == 1:
            hazard = 'Low'
        if (feat['properties']['AREASCORE'] == 2) or (feat['properties']['AREASCORE']==3):
            hazard = "Moderate"
        if (feat['properties']['AREASCORE'] >= 4) and (feat['properties']['AREASCORE'] <= 12):
            hazard = "High"
        if feat['properties']['AREASCORE'] >= 13:
            hazard = "Extreme"

        feat['properties'] = {'Hazard':hazard}
        output.write(feat)
