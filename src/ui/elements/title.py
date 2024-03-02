import pygfx as gfx

from base.ui import UI

TITLE_HEIGHT = 30


class Title(UI):
    def __init__(self, position, width=200, height=TITLE_HEIGHT,
                 text="Controllers"):
        self.width = width
        self.height = height
        self._title = text

        self._plane = gfx.Mesh(
            gfx.plane_geometry(self.width, self.height),
            gfx.MeshBasicMaterial(color="#ddd")
        )
        self._set_title(text)
        super().__init__(position)

    @property
    def title(self): return self._title

    @title.setter
    def title(self, title):
        self._set_title(text=title)

    def _get_objects(self):
        return [self._text, self._plane]

    def _set_position(self, position):
        print('I am here')
        text_bb = self._text.get_bounding_box()
        padding = 20
        text_width = text_bb[1][0] - text_bb[0][0] + padding
        self._text.local.position = (position[0] + text_width / 2,
                                     position[1] + self.height / 2, 1)
        self._plane.local.position = (position[0] + self.width / 2,
                                      position[1] + self.height / 2, 0)

    def _set_title(self, text='', color="#000", weight_offset=400):
        self._text = gfx.Text(
            gfx.TextGeometry(text=text, font_size=16),
            gfx.TextMaterial(color=color,
                             weight_offset=weight_offset, outline_thickness=0)
        )
