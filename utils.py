import json
from shapely.geometry import shape, Point


SP_FENCE = 'shippingPointFence'
LANE = 'smfLane-0304705806.geojson'

# Load lane
with open(LANE, 'r') as f:
    lane = json.load(f)

# Construct point from geolocation
point = Point(-77.5210123, 40.027551)

for feature in lane['features']:
    properties = feature['properties']
    if properties['type'] == SP_FENCE:
        polygon = shape(feature['geometry']) 
        if polygon.contains(point):
            print "Point is in %s" % (properties['poiName']) 