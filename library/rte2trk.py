# input gpx file, waypoints are preserved
# tracks are preserved
# route points are converted to track points of a new track segment

import sys
import gpxpy

with open( sys.argv[1]+'.gpx', 'r' ) as infile:
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
    
for track in org.tracks:
    t=gpxpy.gpx.GPXTrack()
    t.name = track.name
    new.tracks.append(t)
    for segment in track.segments:
        s=gpxpy.gpx.GPXTrackSegment()
        t.segments.append(s)
        for p in segment.points:
            lat = f"{p.latitude:.6f}"
            lon = f"{p.longitude:.6f}"
            if (p.elevation!=None):
                ele=int(p.elevation)
                q = gpxpy.gpx.GPXTrackPoint(lat,lon,ele)
            else:
                q = gpxpy.gpx.GPXTrackPoint(lat,lon)
            s.points.append(q) 

for r in org.routes:
    t = gpxpy.gpx.GPXTrack()
    t.name = r.name
    new.tracks.append(t)
    s = gpxpy.gpx.GPXTrackSegment()
    t.segments.append(s)
    for p in r.points:
        lat = f"{p.latitude:.6f}"
        lon = f"{p.longitude:.6f}"
        if (p.elevation!=None):
            q = gpxpy.gpx.GPXTrackPoint(lat,lon)
            q.elevation =int(p.elevation)
        else:
            q = gpxpy.gpx.GPXTrackPoint(lat,lon)  
        s.points.append(q)

print (new.to_xml())

with open(sys.argv[1]+'.gpx', 'w') as file:
    file.write( new.to_xml() )
