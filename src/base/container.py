import pygfx as gfx

from base.ui import UI
from ui.elements.title import Title, TITLE_HEIGHT


class Container(UI):
    def __init__(self, position, width, height):
        self.is_open = False
        self._elements = []

        self._width = width
        self._height = height

        self._title = Title(position, width)
        self._plane = gfx.Mesh(
            gfx.plane_geometry(width, height - TITLE_HEIGHT),
            gfx.MeshBasicMaterial(color="#000")
        )
        super().__init__(position)

    def _set_position(self, position):
        self._plane.local.position = (position[0],
                                      position[1] + TITLE_HEIGHT, 0)

    def _get_objects(self):
        objects = self._title.objects
        for element in self._elements:
            objects += element.objects
        objects += [self._plane]
        return objects
