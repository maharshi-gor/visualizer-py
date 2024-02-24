import pygfx as gfx
from base.util import Color

from ui.ui import UI


class Slider(UI):

    def __init__(self,
                 line_width=100,
                 height=10,
                 disk_radius=10,
                 track_color='#5da9e9',
                 disk_color='#003F9'):

        super().__init__()

        self._geo = gfx.plane_geometry(line_width, height)
        self._track = gfx.Mesh(self._geo, gfx.MeshBasicMaterial(
            color=Color.get_color(track_color)))

    def add_to_scene(self, scene):
        scene.add(self._track)
