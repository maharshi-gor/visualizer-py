import pygfx as gfx

from base.ui import UI


class Slider(UI):

    def __init__(self,
                 range=(0, 100),
                 initial_value=50,
                 line_width=200,
                 height=6,
                 disk_radius=10,
                 track_color='#5da9e9',
                 disk_color='#008bf8',
                 position=(0, 0)):

        self._track_geo = gfx.plane_geometry(line_width, height)
        self._track = gfx.Mesh(self._track_geo, gfx.MeshBasicMaterial(
            color=track_color))
        self._disk_geo = gfx.cylinder_geometry(disk_radius, disk_radius)
        self._disk = gfx.Mesh(self._disk_geo, gfx.MeshBasicMaterial(
            color=disk_color))

        self._width = line_width + disk_radius
        self._height = 2 * disk_radius

        self._disk_clicked = False
        self._disk.add_event_handler(self._disk_dragged, 'ui_pointer_drag')
        self._set_disk_position(0)
        super().__init__(position)

    def _get_objects(self):
        return [self._track, self._disk]

    def _set_disk_position(self, x_position):
        bb = self._track.get_bounding_box()
        x_position = max(bb[0][0], x_position)
        x_position = min(bb[1][0], x_position)
        self._disk.local.position = (x_position, (bb[0][1]+bb[1][1])/2, 0)

    def _disk_dragged(self, event):
        self._set_disk_position(event.x)

    def _set_position(self, position):
        self._track.local.position = (position[0], position[1], 0)
        # TODO: Update x_position according to value of the slider
        self._set_disk_position(position[0])
