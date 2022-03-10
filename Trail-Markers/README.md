Trail Markers (totally not useful for hikers)

The marker locations are included in this repository for completeness. It may be useful for trail maintenance or search & rescue.

`Stats` There is a total of 567 trail markers in the 4 major hiking trails. On average, there is a trail marker (sign post) roughly every 500 meters. Hong Kong Trail has 100 markers, Lantau Trail has 139 markers, MacLehose Trail has 200 markers and Wilson Trail has 137 markers. 

`Perplexing` The words "Distance Post" on the sign post is misleading. It has nothing to do with distance. However, since the markers are roughly 500 m apart, one can argue strenuously that these are indeed incremental distance counters. More accurately, they should be titled "Truncated MGRS Coordinate with an ambigious grid zone GZD". Most hikers don't know, don't need or care about MGRS Coordinates.

`Curiosity` If you are familiar with MGRS or wearing a Garmin watch with MGRS, when you come across a trail marker, you will notice that the Grid Reference (on the trail marker) is a truncated MGRS (100 m resolution) and the grid zone designator `GZD` is omitted.
That omission would be okay if all the (hiking) activities are within the same GZD, unfortunately they are not and hence these issues/complexity arise:

`Complexity`<br>
Wilson Trail: all trail markers are in grid zone 50Q (cool)<br>
Hong Kong Trail: all trail markers are in grid zone 50Q (cool)<br>
Lantau Trail: trail markers L001 to L133 are in grid zone 49Q, markers L134 to L139 are in grid zone 50Q (totally not cool)<br>
MacLehose Trail: trail markers M001 to M190 are in grid zone 50Q, markers M191 to M200 are in grid zone 49Q (totally not cool)<br>

`Design flaw` The use of truncated grid reference to locate a friend/hiker in distress could be an inferior approach because of the ambigious grid zone in Lantau Trail and MacLehose Trail. It will likely cause uncertainty and error. 

`Discovery` The sign post's identifier gives more useful information, e.g. 
<br>Sign post M115 (prefix M denotes MacLehose Trail) is at lat lon 22.348108, 114.153725. 
<br>Sign post H062 (prefix H denotes Hong Kong Trail) is at lat lon 22.260450, 114.21352. 
<br>Sign post L047 (prefix L denotes Lantau Trail) is at lat lon 22.22656, 113.8668. 
<br>Sign post W128 (prefix W dentoes Wilson Trail) is at lat lon 22.4928, 114.23158.

`Final Product` Latitude and longitude (WGS84) for all the trail markers (sign posts) are contained in All-576-markers.gpx and All-576-markers.kml. The GPX file can be visualized using [GPXSee](http://www.gpxsee.org) or [notepad++](https://notepad-plus-plus.org/). If need be, imported into a mobile device for field work (e.g. maintenance/S&R). The KML file can be imported to Google Earth or Google My Maps. Optionally, append/import these markers to the hiking trails.

`Footnote` <br>1.8 km of Wilson Trail and Hong Kong Trail overlap each other near Jardine's Lookout. Hence 5 strangely labelled trail markers exist in that area: H053;W009 H054;W010 H055;W011 H056;W012 H057;W013
