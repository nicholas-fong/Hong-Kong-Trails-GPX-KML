### GPX-GPX Python codes

Ocassionally some gpx files are "corrupted" and they fail to work in handheld devices.

gpx2gpx.py can sometimes clean up the corrupted gpx file (within reasons) so that it conforms to GPX XML Schema. [GPX 1.1 Schema Documentation](https://www.topografix.com/GPX/1/1/).

To clean `hiking.gpx`:
```
$python3 gpx2gpx.py hiking
```
The above code cannot clean up gpx file that is corrupted in this manner:<br>Imagine a route with points A..B..C..D..E but the gpx file route points are in a different order, e.g. A..C..D..E..B, the above code cannot fix such logical error.

Also included are two GPX conversion utilities:<br> 
`rte2trk.py` and `trk2rte.py`.

They can be used to convert between GPX-route file and GPX-track file. Some mobile devices get less cranky when given the correct route/track type.
```
$python3 rte2trk.py hiking
$python3 trk2rte.py hiking
```
