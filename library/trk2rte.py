# input gpx file, 
# waypoints are preserved
# routes are preserved
# track are converted to route of a new route.

import sys
import gpxpy

with open( sys.argv[1]+'.gpx' ) as infile:
    org = gpxpy.parse(infile)
infile.close()  #for peace of mind.

new = gpxpy.gpx.GPX()        #create a new destination object

for j in org.waypoints:
    lat = f"{j.latitude:.6f}"
    lon = f"{j.longitude:.6f}"
    if (j.elevation!=None):
        p=gpxpy.gpx.GPXWaypoint(lat,lon)
        p.name = j.name
        p.elevation=int(j.elevation)
    else:
        p=gpxpy.gpx.GPXWaypoint(lat,lon)
        p.name= j.name
    new.waypoints.append(p)

for route in org.routes:
    newroute = gpxpy.gpx.GPXRoute(route.name)
    #newroute.name = route.name
    new.routes.append(newroute)
    for p in route.points:
        lat = f"{p.latitude:.6f}"
        lon = f"{p.longitude:.6f}"
        if p.elevation :
            ele =int(p.elevation)
            np = gpxpy.gpx.GPXRoutePoint(lat,lon,ele)
        else:
            np = gpxpy.gpx.GPXRoutePoint(lat,lon)  
        newroute.points.append(np)   

for track in org.tracks:
    r = gpxpy.gpx.GPXRoute(track.name)
    new.routes.append(r)
    for segment in track.segments:
        for p in segment.points:
            lat = f"{p.latitude:.6f}"
            lon = f"{p.longitude:.6f}"
            if (p.elevation!=None):
                ele=int(p.elevation)
                q = gpxpy.gpx.GPXRoutePoint(lat,lon,ele)
            else:
                q = gpxpy.gpx.GPXRoutePoint(lat,lon)
            r.points.append(q) 

print (new.to_xml())

with open(sys.argv[1]+'.gpx', 'w') as file:
    file.write( new.to_xml() )

