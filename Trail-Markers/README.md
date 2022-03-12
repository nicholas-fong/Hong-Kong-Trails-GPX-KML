Trail Markers (somewhat useful for hikers, depends on personal preference)

Append/import these markers (waypoints) to superimpose on the hiking trails on mobile devices if preferred.

`Marker Nomenclature`
<br>The first letter of the marker (sign post) denotes the first letter of the trail name.
<br>M denotes MacLehose Trail, H denotes Hong Kong Trail, L denotes Lantau Trail, W dentoes Wilson Trail

`Stats` There is a total of 567 trail markers for the 4 major hiking trails. On average, there is a trail marker (sign post) roughly every 500 meters. Hong Kong Trail has 100 markers, Lantau Trail has 139 markers, MacLehose Trail has 200 markers and Wilson Trail has 137 markers. 

`Files` Geo coordinates for the trail markers (sign posts) are compiled in `GeoJSON`, `GPX` and `KML`.

`Footnote` <br>1.8 km of Wilson Trail and Hong Kong Trail overlap each other near Jardine's Lookout. Hence 5 strangely labelled trail markers exist in that area: H053;W009 H054;W010 H055;W011 H056;W012 H057;W013

<hr>

`Perplexing` The label "Distance Post" on the sign post is misleading. It has nothing to do with distance. However, since the markers are roughly 500 m apart, one can argue strenuously that these are indeed incremental distance counters. More accurately, they should be titled "Truncated MGRS Coordinate with an ambigious grid zone GZD". Most hikers don't know, don't need or care about MGRS Coordinates.

`Curiosity` If you are familiar with MGRS or wearing a Garmin watch with MGRS, when you come across a trail marker, you will notice that the Grid Reference on the sign post is basically a truncated MGRS (100 m resolution) and the grid zone designator `GZD` is omitted.
That omission would be okay if all the (hiking) activities are within the same GZD, unfortunately they are not, hence the following issues/complexity arise:

`Complexity`<br>
Wilson Trail: all trail markers are in grid zone 50Q (cool)<br>
Hong Kong Trail: all trail markers are in grid zone 50Q (cool)<br>
Lantau Trail: trail markers L001 to L133 are in grid zone 49Q, markers L134 to L139 are in grid zone 50Q (totally not cool)<br>
MacLehose Trail: trail markers M001 to M190 are in grid zone 50Q, markers M191 to M200 are in grid zone 49Q (totally not cool)<br>

`Design flaw` Grid reference with ambigious grid zone is an inferior approach (Lantau Trail and MacLehose Trail).
