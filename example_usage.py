from client import SpatialGridMapper

mapper = SpatialGridMapper(1920, 1080)
click_target = mapper.map_box_to_anchor([300, 400, 350, 500])
print("Target click anchor:\n", click_target)
