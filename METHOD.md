# Methodology used to generate these high quality hiking GPX tracks:<br>
On a per trail section basis: 
<br>use [Overpass](https://www.overpass-turbo.eu) query wizard to extract nodes, e.g. in the query wizard search box type: name ~ "MacLehose Trail Section 1" 

Eexport the result as `GeoJSON` file.

Open [Java OpenStreetMap Editor](https://josm.openstreetmap.de/) to manually correct these data inconsistencies:
<br>-remove overlapping/duplicated/extraneous paths and objects
<br>-change direction of fragmented paths to be consistent (direction follows sign posts from n to n+1)
<br>-join nodes along the trail that were disjointed
<br>-merge all fragmented paths into one continuous path, when this is achieved, pressing "R" (reverse way) does not generate error
<br>-optimize the number of nodes using JOSM's built-in "simplify way" tool
<br>-ensure the final GeoJSON file has only one LineString.

The cleaned up data is saved as `GeoJSON` and then converted to `GPX tracks`,`GPX routes` and `KML` using codes from [geoJSON-gpx-convert](https://github.com/nicholas-fong/geoJSON-gpx-convert). 

The elevation profile of the GPX tracks and GPX routes is added using codes from [gpx-add-SRTM](https://github.com/nicholas-fong/gpx-add-SRTM) and [NASA Digital Elevation Model](https://earthdata.nasa.gov/learn/articles/new-aster-gdem)
