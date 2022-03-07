Hong Kong Hiking Trail - Trail Markers Geo Coordinate Repository (not useful for hikers, slightly helpful for search and rescue)

Most of the times, you don't need to use or worry about these trail markers.
They are included in this repository as GPX waypoints for completeness (Hong Kong Trail has 100 markers over 50 km, Lantau Trail has 139 markers over 67 km, MacLehose Trail has 200 markers over 98 km, Wilson Trail has 137 markers over 76 km). On average, there is a trail marker (sign post) roughly every 500 meters.

On the trail markers, the title "Distance Post" is misleading. It has nothing to do with distance. It should be "Truncated MGRS Coordinate with ambigious grid zone GZD". If you don't know what MGRS is, don't worry about it.

If you are familiar with MGRS or wearing a Garmin watch with MGRS, when you come across a trail marker, you will notice that the Grid Reference (on the trail marker) is a truncated MGRS (100 m resolution) and the grid zone designator `GZD` is omitted.
That omission would make sense if all the (hiking) activities are within the same GZD, but they are not and hence these issues arise:

Wilson Trail: all trail markers are in grid zone 50Q (cool)

Hong Kong Trail: all trail markers are in grid zone 50Q (cool)

Lantau Trail: trail markers L001 to L133 are in grid zone 49Q, markers L134 to L139 are in grid zone 50Q (not cool)

MacLehose Trail: trail markers M001 to M190 are in grid zone 50Q, markers M191 to M200 are in grid zone 49Q (not cool)

In summary, the use of truncated grid reference to locate hikers in distress is an inferior approach because of ambigious grid zone in Lantau and MacLehose. The sign post's identifier, e.g. M115 (prefix M denotes MacLehose) is at lat=22.348108 lon=114.153725 (see MacLehose-Trail-Markers.gpx). Similarily, sign post H048 (prefix H denotes Hong Kong Trail) is at lat=22.25856 lon=114.1831 (see Hong-Kong-Trail-Markers.gpx).
