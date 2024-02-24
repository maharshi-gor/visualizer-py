import pygfx as gfx
from base.util import Color

from ui.ui import UI


class Slider(UI):

    def __init__(self,
                 line_width=200,
                 height=6,
                 disk_radius=6,
                 track_color='#5da9e9',
                 disk_color='#003F9',
                 position=(0, 0)):

        super().__init__()
        self._track_geo = gfx.plane_geometry(line_width, height)
        self._track = gfx.Mesh(self._track_geo, gfx.MeshBasicMaterial(
            color=Color.get_color(track_color)))
        self._disk_geo = gfx.cylinder_geometry(disk_radius, disk_radius)
        self._disk = gfx.Mesh(self._disk_geo, gfx.MeshBasicMaterial(
            color=Color.get_color(disk_color)))

        self._disk_clicked = False
        self._disk.add_event_handler(self._disk_drag_started, 'pointer_down')
        self._track.add_event_handler(self._disk_drag_continue, 'pointer_move')
        # self._disk.add_event_handler(self._disk_drag_ended, 'pointer_up')

        print(self._track.get_world_bounding_box())
        self._set_position()
        # self._disk.local.position = (position[0]
        #                              - self._track.get_bounding_box()[0] / 2,
        #                              self._track.get_bounding_box()[1]/2, 0)

    def _get_objects(self):
        return [self._track, self._disk]

    # def add_to_scene(self, scene):
    #     scene.add(self._track)
    #     scene.add(self._disk)

    # def remove_from_scene(self, scene):
    #     scene.remove(self._track)
    #     scene.remove(self._disk)

    def _set_position(self):
        bb = self._track.get_bounding_box()
        self._disk.local.position = (bb[0][0], (bb[0][1]+bb[1][1])/2, 0)

    def _disk_drag_started(self, event):
        self._disk_clicked = True
        print(self._disk.local.position, self._disk.world.position)
        # self._disk.local.position = (10, 10, 0)

    def _disk_drag_continue(self, event):
        if self._disk_clicked:
            print(event.pick_info['face_coord'][0])
            self._disk.local.position = (event.pick_info['face_coord'][1],
                                         self._disk.local.position[1],
                                         self._disk.local.position[2])
            # self._disk.local.position = (event.pic,
            #                              self._disk.world.position[1], 0)


