### Hong-Kong-Hiking-Trails-GPX-KML

For hiking enthusiasts savvy with mobile devices and offline hiking apps. This repository hosts a complete set of unofficial high quality GPS coordinates (GPX and KML) for the 4 major hiking trails in Hong Kong SAR (MacLehose Trail 麥理浩徑 98 km, Hong Kong Trail 港島徑 45 km, Wilson Trail 衛奕信徑 77 km and Lantau Trail 鳳凰徑 67 km for a total of 287 km with over 24,000 route points). Use these files at your own risks.

Due to the length of trails, Hong Kong hiking trails are divided into sections. Consult [Wikipedia](https://en.wikipedia.org/wiki/List_of_hiking_trails_in_Hong_Kong) or [Enjoy Hiking website](https://www.hiking.gov.hk) for various trail heads and how to get there.

Alltrails.com also has many such trails in GPX and KML formats. 

### Methodology used to generate these tracks:

Use [Overpass](https://www.overpass-turbo.eu) query wizard to extract trails and export as GeoJSON file to JOSM - [Java OpenStreetMap Editor](https://josm.openstreetmap.de/) to manually correct data inconsistencies and other errors. The cleaned up data is then converted to `GPX tracks`, `GPX routes` and `KML` using Python codes from [GeoJSON-to-gpx](https://github.com/nicholas-fong/geoJSON-to-gpx) repository. The elevation of the trails is derived from NASA's Advanced Spaceborne Thermal Emission and Reflection Radiometer `ASTER` Global Digital Elevation Model `GDEM` V3 GeoTIFF geospatial metadata, using Python codes from [SRTM-GeoTIFF](https://github.com/nicholas-fong/SRTM-GeoTIFF) repository. For more detailed steps, see [this page.](https://github.com/nicholas-fong/Hong-Kong-Trails-GPX-GeoJSON-KML/blob/main/METHOD.md)

### To visualize these tracks:

Download the GPX or KML files and drop it in [geojson.io](https://geojson.io). `GPX track` and `GPX route` are for use primarily with mobile devices. `KML` are for use with `Google Earth` and `Google My Maps` and also used by mobile devices. 

For [Google My Maps](https://mymaps.google.com/), sign in first, "Create A New Map", import a KML file. The map is stored in your Google Account's Google Drive. 

### How to use these tracks:

There are many outdoor/hiking mobile phone apps such as `Locus Map`, `Komoot`, `Avenza Maps`, `Garmin Explore`, `GPX Viewer 2`, etc. 

For `Garmin` handheld GPS device such as `eTrex SE`, use a USB cable to copy GPX files of interests to the device.

Some apps/devices work happier with GPX track, some work happier with GPX routes. Experiment to find the format that works best.

To merge tracks and waypoints into one file, use [geojson.io](https://geojson.io) to load the tracks and waypoints and save the combined features as a GeoJSON file, then convert to GPX using code from [GeoJSON-to-gpx](https://github.com/nicholas-fong/geoJSON-to-gpx) or convert to KML using code from [KML-to-GeoJSON](https://github.com/nicholas-fong/KML-to-GeoJSON)

### `Government websites:`

The Agriculture, Fisheries and Conservation Department `AFCD` 漁農自然護理署 of Hong Kong SAR's [Enjoy Hiking website](https://www.hiking.gov.hk) is an excellent starting point for planning a hike. The Country and Marine Parks Authority `CMPA` 郊野公園及海岸公園管理局 of Hong Kong SAR operates and maintains the trails.

The Office of the Communications Authority `OFCA` 通訊事務管理局辦公室 of Hong Kong SAR publishes [PDF trail maps](https://www.ofca.gov.hk/en/consumer_focus/guide/safety/country_parks/coverage_survey/digital_map/index.html) including estimated mobile phone signal coverage. 

