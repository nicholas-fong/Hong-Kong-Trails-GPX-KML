Trail Markers Geo Coordinates (not useful for hikers, slightly helpful for search and rescue)

Most of the times, you don't need to use or worry about these trail markers.
They are included in this repository as GPX waypoints for completeness.<br>
Hong Kong Trail has 100 markers over 45 km, Lantau Trail has 139 markers over 67 km, MacLehose Trail has 200 markers over 98 km, Wilson Trail has 137 markers over 76 km. On average, there is a trail marker (sign post) roughly every 500 meters.

On the trail markers, the title "Distance Post" is misleading. It has nothing to do with distance. However, since the markers are roughly 500 m apart, one can argue strenuously that these are indeed incremental distance markers. More precisely, they should be labelled "Truncated MGRS Coordinate with ambigious grid zone GZD". If you don't know what MGRS or grid zone is, don't worry about it.

If you are familiar with MGRS or wearing a Garmin watch with MGRS, when you come across a trail marker, you will notice that the Grid Reference (on the trail marker) is a truncated MGRS (100 m resolution) and the grid zone designator `GZD` is omitted.
That omission would make sense if all the (hiking) activities are within the same GZD, but they are not and hence these issues/complexity arise:

Wilson Trail: all trail markers are in grid zone 50Q (cool)<br>
Hong Kong Trail: all trail markers are in grid zone 50Q (cool)<br>
Lantau Trail: trail markers L001 to L133 are in grid zone 49Q, markers L134 to L139 are in grid zone 50Q (not cool)<br>
MacLehose Trail: trail markers M001 to M190 are in grid zone 50Q, markers M191 to M200 are in grid zone 49Q (not cool)<br>

In short, the use of truncated grid reference to locate a friend/hiker in distress is an inferior approach because of the ambigious grid zone in Lantau Trail and MacLehose Trail. 

In view of above, perhaps the sign post's identifier is more useful, e.g. Sign post M115 (prefix M denotes MacLehose) is at lat=22.348108 lon=114.153725. Sign post H062 (prefix H denotes Hong Kong Trail) is at lat=22.26045 lon=114.21352. Sign post L047 is at lat=22.22656 lon=113.8668 (prefix L denotes Lantau Trail). Sign post W128 is at lat=22.4928 lon=114.23158 (prefix W dentoes Wilson Trail).<br>
Latitude and longitude for all the trail markers are stored in the corresponding Trail-Makers.GPX file, they can be viewed using [GPXSee](http://www.gpxsee.org) or [notepad++](https://notepad-plus-plus.org/)

Footnote: <br>1.8 km of Wilson Trail and Hong Kong Trail overlap each other near Jardine's Lookout. Hence 5 strangely labelled trail markers exist in that area: H053;W009 H054;W010 H055;W011 H056;W012 H057;W013
