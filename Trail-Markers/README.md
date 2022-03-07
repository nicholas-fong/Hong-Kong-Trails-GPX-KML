Trail Markers Geo Coordinates (not useful for hikers, slightly helpful for search and rescue)

Most of the times, you don't need to use or worry about these trail markers.
They are included in this repository as GPX waypoints for completeness (Hong Kong Trail has 100 markers over 45 km, Lantau Trail has 139 markers over 67 km, MacLehose Trail has 200 markers over 98 km, Wilson Trail has 137 markers over 76 km). On average, there is a trail marker (sign post) roughly every 500 meters.

On the trail markers, the title "Distance Post" is misleading. It has nothing to do with distance. However, since the markers are roughly 500 m apart, one can argue strenuously that these are indeed incremental distance markers. More precisely, they should be labelled "Truncated MGRS Coordinate with ambigious grid zone GZD". If you don't know what MGRS or grid zone is, don't worry about it.

If you are familiar with MGRS or wearing a Garmin watch with MGRS, when you come across a trail marker, you will notice that the Grid Reference (on the trail marker) is a truncated MGRS (100 m resolution) and the grid zone designator `GZD` is omitted.
That omission would make sense if all the (hiking) activities are within the same GZD, but they are not and hence these issues arise:

Wilson Trail: all trail markers are in grid zone 50Q (cool)

Hong Kong Trail: all trail markers are in grid zone 50Q (cool)

Lantau Trail: trail markers L001 to L133 are in grid zone 49Q, markers L134 to L139 are in grid zone 50Q (not cool)

MacLehose Trail: trail markers M001 to M190 are in grid zone 50Q, markers M191 to M200 are in grid zone 49Q (not cool)

In summary, the use of truncated grid reference to locate hikers in distress is an inferior approach because of the ambigious grid zone in Lantau and MacLehose. The sign post's identifier is more useful, e.g. M115 (prefix M denotes MacLehose) is at lat=22.348108 lon=114.153725 (see MacLehose-Trail-Markers.gpx), H062 (prefix H denotes Hong Kong Trail) is at lat=22.26045 lon=114.21352 (see Hong-Kong-Trail-Markers.gpx), L047 is at lat=22.22656 lon=113.8668 (see Lantau-Trail-Markers.gpx), W128 is at lat=22.4928 lon=114.23158 (see Wilson-Trail-Markers.gpx).

Footnote: Approximately 1.6 km of Wilson Trail and Hong Kong Trail overlap each other near Jardine's Lookout. Hence these strange trail markers exist: H053;W009 H054;W010 H055;W011 H056;W012 H057;W013
