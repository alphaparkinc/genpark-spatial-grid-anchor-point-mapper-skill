"""Spatial Grid Anchor Point Mapper.
100% Python Standard Library.
"""

class SpatialGridMapper:
    """Maps continuous bounding boxes to discrete UI grid cells and click anchors."""
    def __init__(self, viewport_width=1920, viewport_height=1080, cols=8, rows=6):
        self.vw = viewport_width
        self.vh = viewport_height
        self.cols = cols
        self.rows = rows
        self.cell_w = self.vw / float(cols)
        self.cell_h = self.vh / float(rows)

    def map_box_to_anchor(self, box, coord_format="pixel"):
        if coord_format == "normalized_0_1":
            ymin, xmin, ymax, xmax = [
                box[0] * self.vh, box[1] * self.vw,
                box[2] * self.vh, box[3] * self.vw
            ]
        else:
            ymin, xmin, ymax, xmax = box

        center_x = (xmin + xmax) / 2.0
        center_y = (ymin + ymax) / 2.0

        col_idx = min(self.cols - 1, max(0, int(center_x / self.cell_w)))
        row_idx = min(self.rows - 1, max(0, int(center_y / self.cell_h)))

        col_letter = chr(ord('A') + col_idx)
        grid_id = f"{col_letter}{row_idx + 1}"

        return {
            "anchor_x": int(center_x),
            "anchor_y": int(center_y),
            "grid_cell": grid_id,
            "width": int(xmax - xmin),
            "height": int(ymax - ymin)
        }
