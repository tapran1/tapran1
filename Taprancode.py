# importing libraries
import geemap
import ee
Map = geemap.Map()

#Studyarea
SA = ee.FeatureCollection("users/abranidrees666/SA")
Map.centerObject(SA,10)
Map.addLayer(SA, '','StudyArea')

# Load a Landsat 8 image from the collection before disaster
image = ee.Image(ee.ImageCollection('LANDSAT/LC08/C01/T1_TOA') 
                 .filterDate('2018-04-01', '2018-04-30') 
                 .filterBounds(SA)
                 .sort('CLOUD_COVER') 
                 .first())
# for visual parameters
vizParams = {
 'bands': ['B5', 'B4', 'B2'],
 'min': 0,
 'max': 0.5,
 'gamma': [0.95, 1.1, 1]
}
#adding layer to map
Map.addLayer(image.clip(SA), vizParams, 'Landsat-8 Before')

#Compute the Normalized Difference Vegetation Index (NDVI) before disaster
nir = image.select('B5')
red = image.select('B4')
ndvi = nir.subtract(red).divide(nir.add(red)).rename('NDVI_Before')

# Display the result.
ndviParams = {'min': -1, 'max': 1, 'palette': ['blue', 'white', 'green']}
Map.addLayer(ndvi.clip(SA), ndviParams, 'NDVI_Before')

# Load a Landsat 8 image from the collection after Disaster
image1 = ee.Image(ee.ImageCollection('LANDSAT/LC08/C01/T1_TOA') 
                 .filterDate('2018-08-01', '2018-09-30')
                 .filterBounds(SA)
                 .sort('CLOUD_COVER') 
                 .first())
# for visual parameters
vizParams1 = {
  'bands': ['B5', 'B4', 'B2'],
  'min': 0,
  'max': 0.5,
  'gamma': [0.95, 1.1, 1]
}
Map.addLayer(image1.clip(SA), vizParams1, 'Landsat-8 After')

# Compute the Normalized Difference Vegetation Index (NDVI) after Disaster
NIR = image1.select('B5')
Red = image1.select('B4')
ndvi_1 = NIR.subtract(Red).divide(NIR.add(Red)).rename('NDVI_After')

# Display the result.

ndviParams1 = {'min': -1, 'max': 1, 'palette': ['blue', 'white', 'green']}
Map.addLayer(ndvi_1.clip(SA), ndviParams1, 'NDVI_After')
Map

#To export map as html file.
# Calling libaraies
import os

# directory location
download_dir = os.path.join(os.path.expanduser('-'), 'Documents')
if not os.path.exists(download_dir):
    os.makedirs(download_dir)
html_file = os.path.join(download_dir,'my_map.html')

# Parametrs
Map.to_html(outfile = html_file, title = 'My Map', width = '100%', height ='880px')
