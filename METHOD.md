# Method used to generate high quality hiking GPX tracks<br>
On a section by section basis:
<br>(MacLehose 10 sections; Wilson 10 sections; Hong Kong 8 sections; Lantau 12 sections)
<br>use Google Map to search and zoom to the area of interest. 
<br>open `Overpass` and zoom to the same area.
<br>run [Overpass](https://www.overpass-turbo.eu) query wizard to extract nodes, e.g. in the query wizard search box enter: name ~ "MacLehose Trail Section 1"
<br>note the quoted text in the search box is case sensitive

Export the result as a `GeoJSON` file.

Invoke [Java OpenStreetMap Editor](https://josm.openstreetmap.de/) and open the GeoJSON file to manually correct for these data inconsistencies:
<br>-remove overlapping, duplicated or extraneous paths and objects
<br>-change direction of paths to be consistent (direction follows sign posts from n to n+1)
<br>-Lantau Trail: counter clockwise from Mui Wo ferry terminal. 
<br>-MacLehose Trail: counter clockwise from Pak Tam Chung.
<br>-Hong Kong Trail: counter clockwise from The Peak. 
<br>-Wilson Trail: south to north from Stanley Gap Road.
<br>-if 2 paths are separated, connect them as one. Select the tail node of one path and the head node of the second path: (M)
<br>-select 2 joined paths and combine: (C) 
<br>-optimize the number of nodes using JOSM's built-in "simplify way" tool to 0.5 m accuracy (Shift+Y)
<br>-save as a `GeoJSON` file. e.g. MacLehose1.geojson
<br>-invoke notepad++ and open above to check it has one and only one LineString

To combine trail sections: (e.g. Wilson Section 2 and Wilson Section 3)
<br>-invoke JOSM and open Wilson2.geojson and Wilson3.geojson
<br>-merge the layers into one layer: Ctrl+M
<br>-select the 2 trails and combine: Tools...Combine Way (C)
<br>-save as a `GeoJSON` file. e.g. Wilson-2-3.geojson

To generate `GPX tracks`,`GPX routes` and `KML` from `GeoJSON`:
<br>-use codes from [geoJSON-gpx-convert](https://github.com/nicholas-fong/geoJSON-gpx-convert). 

The elevation profile of the `GPX tracks` and `GPX routes` is added using codes from [gpx-add-SRTM](https://github.com/nicholas-fong/gpx-add-SRTM) and [NASA Digital Elevation Model](https://earthdata.nasa.gov/learn/articles/new-aster-gdem)

Note: `GeoJSON` files have no elevation data. Only `GPX route` and `GPX track` have elevation data.
