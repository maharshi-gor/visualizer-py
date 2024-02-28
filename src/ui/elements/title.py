import pygfx as gfx

from base.ui import UI


class Title(UI):
    def __init__(self, width, height, position, text="Controllers"):
        self.width = width
        self.height = height
        self.text = text

        self._plane = gfx.Mesh(
            gfx.plane_geometry(self.width, self.height),
            gfx.MeshBasicMaterial(color="#ddd")
        )
        self._text_material = gfx.TextMaterial(color="#000", weight_offset=400,
                                               outline_thickness=0)
        self._text = gfx.Text(
            gfx.TextGeometry(text=text, font_size=16),
            self._text_material
        )
        super().__init__(position)

    def _get_objects(self):
        return [self._text, self._plane]

    def _set_position(self, position):
        text_bb = self._text.get_bounding_box()
        padding = 20
        text_width = text_bb[1][0] - text_bb[0][0] + padding
        self._text.local.position = (position[0] + text_width / 2,
                                     position[1] + self.height / 2, 1)
        self._plane.local.position = (position[0] + self.width / 2,
                                      position[1] + self.height / 2, 0)
