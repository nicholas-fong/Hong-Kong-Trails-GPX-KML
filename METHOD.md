# Methodology used to generate these hiking GPX tracks:<br>
Use [Overpass](https://www.overpass-turbo.eu) query wizard to extract nodes, e.g. in the query wizard box: name ~ "MacLehose Trail" 

Save (export) the output as `GeoJSON`

Open [Java OpenStreetMap Editor](https://josm.openstreetmap.de/) to manually correct data inconsistencies:
<br>-remove overlapping/duplicated/extraneous paths and objects
<br>-change direction of fragmented paths to be consistent (direction follows sign posts from n to n+1)
<br>-join nodes along the trail that were disjointed
<br>-merge all segments into one complete path. 
<br>-optimize (reduce) the number of nodes using JOSM built in tool
<br>-ensure GeoJSON file has only one LineString, GPX file has only one track segment or only one route

The cleaned up data is saved as `GeoJSON` and then converted to `GPX tracks`,`GPX routes` and `KML` using code from [geoJSON-gpx-convert](https://github.com/nicholas-fong/geoJSON-gpx-convert). 

The elevation profile of the GPX tracks and GPX routes is added using code from [gpx-add-SRTM](https://github.com/nicholas-fong/gpx-add-SRTM) and [NASA Digital Elevation Model](https://earthdata.nasa.gov/learn/articles/new-aster-gdem)
