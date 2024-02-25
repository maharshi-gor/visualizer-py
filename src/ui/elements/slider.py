import pygfx as gfx
from base.util import Color

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
                 position=(0, 0, 0)):

        super().__init__()
        self._track_geo = gfx.plane_geometry(line_width, height)
        self._track = gfx.Mesh(self._track_geo, gfx.MeshBasicMaterial(
            color=Color.get_color(track_color)))
        self._disk_geo = gfx.cylinder_geometry(disk_radius, disk_radius)
        self._disk = gfx.Mesh(self._disk_geo, gfx.MeshBasicMaterial(
            color=Color.get_color(disk_color)))
        self._back_plane = gfx.Mesh(
            gfx.plane_geometry(line_width + 2 * disk_radius, 2 * disk_radius),
            gfx.MeshBasicMaterial(color=(1, 1, 1, 1)))
        self._outer = gfx.Mesh(gfx.plane_geometry(line_width + 3 * disk_radius,
                                                  3 * disk_radius),
                               gfx.MeshBasicMaterial(color=(1, 1, 1, 1)))

        self._disk_clicked = False
        self._disk.add_event_handler(self._disk_drag_started, 'pointer_down')
        self._back_plane.add_event_handler(self._disk_drag_continue,
                                           'pointer_move')
        self._outer.add_event_handler(self._mouse_moved_out, 'pointer_move')
        self._track.add_event_handler(self._disk_drag_continue, 'pointer_move')
        self._track.add_event_handler(self._track_clicked, 'pointer_down')
        self._disk.add_event_handler(self._disk_drag_ended, 'pointer_up')
        self._track.local.position = position
        self._set_position(0)

    def _get_objects(self):
        return [self._track, self._disk, self._back_plane, self._outer]

    def _set_position(self, x_position):
        bb = self._track.get_bounding_box()
        x_position = max(bb[0][0], x_position)
        x_position = min(bb[1][0], x_position)
        self._disk.local.position = (x_position, (bb[0][1]+bb[1][1])/2, 0)

    def _disk_drag_started(self, event):
        self._disk_clicked = True
        self._mouse_moved_out = False
        event.stop_propagation()

    def _track_clicked(self, event):
        x_offset = 0.85 * 1280
        x_position = event.x - x_offset
        self._set_position(x_position)

    def _disk_drag_continue(self, event):
        if self._disk_clicked:
            x_offset = 0.85 * 1280
            x_position = event.x - x_offset
            self._set_position(x_position)

    def _mouse_moved_out(self, _event):
        self._disk_clicked = False

    def _disk_drag_ended(self, event):
        self._disk_clicked = False
        event.stop_propagation()
        # TODO Calculate the value here...
