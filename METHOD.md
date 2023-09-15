# Method used to generate high quality hiking GPX tracks<br>
On a section by section basis:
<br>(MacLehose: 10 sections; Wilson: 10 sections; Hong Kong: 8 sections; Lantau: 12 sections)
<br>use Google Map to search and zoom to the area of interest. 
<br>open `Overpass` and zoom to the same area.
<br>run [Overpass](https://www.overpass-turbo.eu) query wizard to extract trail, e.g. in the query wizard search box enter: name ~ "MacLehose Trail Section 3"
<br>-other smaller trails are called "Fitness Trail", "Country Trail", "Tree Walk", "Family Walk", "Nature Trail"
<br>-note the quoted text in the search box is case sensitive

Export the result as a `GeoJSON` file.

Invoke [Java OpenStreetMap Editor](https://josm.openstreetmap.de/) and open above GeoJSON file to manually correct for data inconsistencies:
<br>-remove overlapping, duplicated or extraneous paths and objects
<br>-hint: highlight the main trail and hit delete. The extraneous little paths are revealed, move cursor close to them. Ctrl-Z to restore main trail.
<br>-try to select those little paths and delete them.
<br>-change direction of main trail path to be consistent (direction follows sign posts from n to n+1) as follows:
<br>-Lantau Trail: counter clockwise from Mui Wo ferry terminal. 
<br>-MacLehose Trail: counter clockwise from Pak Tam Chung.
<br>-Hong Kong Trail: counter clockwise from The Peak. 
<br>-Wilson Trail: south to north from Stanley Gap Road.
<br>-when all extraneous little paths are eliminated, work on the main trail.
<br>-if 2 paths are separated, connect them as one. Select the tail node of one path and the head node of the second path: (M)
<br>-select 2 joined paths and combine: (C) 
<br>-save as a `GeoJSON` file. e.g. MacLehose3.geojson
<br>-invoke notepad++ and open above to check it has one and only one word 'LineString' or use GPXSee to visually inspect

To combine trail sections: (e.g. to combine Wilson Section 2 and Wilson Section 3)
<br>-invoke JOSM and open Wilson2.geojson and Wilson3.geojson
<br>-merge the layers into one layer: Ctrl+M
<br>-if 2 paths are separated, connect them as one. Select the tail node of one path and the head node of the second path: (M)
<br>-select the 2 trails and combine: Tools...Combine Way (C)
<br>-save as a `GeoJSON` file. e.g. Wilson-2-3.geojson

To generate `GPX tracks`,`GPX routes` from `GeoJSON`:
<br>-use codes from [GeoJSON-to-gpx](https://github.com/nicholas-fong/GeoJSON-to-gpx). 

The elevation profile of the `GPX tracks` and `GPX routes` is added using codes from [SRTM-GeoTIFF](https://github.com/nicholas-fong/SRTM-GeoTIFF) and [NASA Digital Elevation Model](https://earthdata.nasa.gov/learn/articles/new-aster-gdem)

After that, the elevation of the `GeoJSON` is added using codes from [SRTM-GeoTIFF](https://github.com/nicholas-fong/SRTM-GeoTIFF). KML is also created from the `GeoJSON` using codes from [KML-to-GeoJSON](https://github.com/nicholas-fong/KML-to-geoJSON).
