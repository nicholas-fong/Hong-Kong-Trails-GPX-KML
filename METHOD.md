# Methodology used to generate these high quality hiking GPX tracks:<br>
On a section by section basis: 
<br>use [Overpass](https://www.overpass-turbo.eu) query wizard to extract nodes, e.g. in the query wizard search box enter: name ~ "MacLehose Trail Section 1" 

Export the result as a `GeoJSON` file.

Invoke [Java OpenStreetMap Editor](https://josm.openstreetmap.de/) and open the GeoJSON file to manually correct for these data inconsistencies:
<br>-remove overlapping, duplicated or extraneous paths and objects
<br>-change direction of fragmented paths to be consistent (direction follows sign posts from n to n+1)
<br>-Lantau Trail: counter clockwise from Mui Wo ferry terminal. MacLehose Trail: counter clockwise from Pak Tam Chung.
<br>-Hong Kong Trail: counter clockwise from The Peak. Wilson Trail: south to north from Stanley Gap Road.
<br>-if 2 paths are separate, join the end nodes. Select the 2 nodes, Tools...Merge Node (M)
<br>-select 2 or more paths and combine: Tools...Combine Way (C) 
<br>-optimize the number of nodes using JOSM's built-in "simplify way" tool (Shift+Y)
<br>-save as a `GeoJSON` file. e.g. MacLehose1.geojson
<br>-invoke notepad++ and open above to check it has only one LineString


To generate `GPX tracks`,`GPX routes` and `KML` from above `GeoJSON`:
<br>-use codes from [geoJSON-gpx-convert](https://github.com/nicholas-fong/geoJSON-gpx-convert). 

To combine 2 trail sections: (e.g. Wilson Section 1 and Wilson Section 2)
<br>-invoke JOSM and open Wilson1.geojson and Wilson2.geojson
<br>-merge the layers into one layer: Ctrl+M
<br>-select the 2 trails and combine: Tools...Combine Way (C)
<br>-save as a `GeoJSON` file. e.g. Wilson-1-2.geojson

To generate `GPX tracks`,`GPX routes` and `KML` from above `GeoJSON`:
<br>-use codes from [geoJSON-gpx-convert](https://github.com/nicholas-fong/geoJSON-gpx-convert). 

The elevation profile of the `GPX tracks` and `GPX routes` is added using codes from [gpx-add-SRTM](https://github.com/nicholas-fong/gpx-add-SRTM) and [NASA Digital Elevation Model](https://earthdata.nasa.gov/learn/articles/new-aster-gdem)
