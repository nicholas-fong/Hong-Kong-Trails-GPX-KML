import sys
import gpxpy

with open( sys.argv[1]+'.gpx' ) as infile:
    data = gpxpy.parse(infile)

gpx = gpxpy.gpx.GPX()

for p in data.waypoints:
    lat = f"{p.latitude:.6f}"
    lon = f"{p.longitude:.6f}"
    if p.elevation :
        np=gpxpy.gpx.GPXWaypoint(lat,lon,int(p.elevation))
        np.name = p.name
    else:
        np=gpxpy.gpx.GPXWaypoint(lat,lon)
        np.name= p.name
    gpx.waypoints.append(np)

for route in data.routes:
    newroute = gpxpy.gpx.GPXRoute()
    newroute.name = route.name
    gpx.routes.append(newroute)
    for p in route.points:
        lat = f"{p.latitude:.6f}"
        lon = f"{p.longitude:.6f}"
        if p.elevation :
            np = gpxpy.gpx.GPXRoutePoint(lat,lon,int(p.elevation))
        else:
            np = gpxpy.gpx.GPXRoutePoint(lat,lon)  
        newroute.points.append(np)    
    
for track in data.tracks:
    newtrack=gpxpy.gpx.GPXTrack()
    newtrack.name = track.name
    gpx.tracks.append(newtrack)
    for segment in track.segments:
        s=gpxpy.gpx.GPXTrackSegment()
        newtrack.segments.append(s)
        for p in segment.points:
            lat = f"{p.latitude:.6f}"
            lon = f"{p.longitude:.6f}"
            if p.elevation :
                ele=int(p.elevation)
                np = gpxpy.gpx.GPXTrackPoint(lat,lon,ele)
            else:
                np = gpxpy.gpx.GPXTrackPoint(lat,lon)
            if p.time :
                np.time = p.time
            s.points.append(np) 

#print (gpx.to_xml())

with open(sys.argv[1]+'.gpx', 'w') as file:
    file.write( gpx.to_xml() )
