import mapnik

map = mapnik.Map(3134, 3134)
mapnik.load_map(map, 'alesund_terrain.xml')
bbox = mapnik.Box2d(mapnik.Coord(325000, 6900000),
                    mapnik.Coord(375000, 6950000))
map.zoom_to_box(bbox)
mapnik.render_to_file(map, 'alesund_terrain.png')
