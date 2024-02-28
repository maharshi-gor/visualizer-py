import pygfx as gfx

from base.section import Section
from base.util import Color
from ui.containers.slice import SliceContainer


class Controller(Section):
    def __init__(self,
                 scene: gfx.Scene,
                 renderer: gfx.Renderer,
                 rect: tuple,
                 win_size: tuple,
                 bg=None):

        self._camera = gfx.OrthographicCamera()
        super().__init__(scene, renderer, rect, win_size, bg)

        self._containers = []
        slice_container = SliceContainer()
        self._containers.append(slice_container)

        for container in self._containers:
            container.add_to_scene(self._scene)

        self._drag_started = False
        self._drag_target = None
        self._register_events()

        self._parent_element = gfx.Mesh(
            gfx.plane_geometry(*self.size),
            gfx.MeshBasicMaterial(color=Color.get_color('#ffffff')))

        self._scene.add(self._parent_element)

    def resized(self, win_size):
        super().resized(win_size)

        for container in self._containers:
            container.resize()

    def _register_events(self):
        self._scene.add_event_handler(
            self._pointer_down, 'pointer_down'
        )
        self._scene.add_event_handler(
            self._pointer_move, 'pointer_move'
        )
        self._scene.add_event_handler(
            self._pointer_up, 'pointer_up'
        )

    def _pointer_down(self, event):
        self._drag_started = True
        self._drag_target = event.target

    def _pointer_move(self, _event: gfx.PointerEvent):
        if self._drag_started:
            _event.stop_propagation()
            drag_event = gfx.PointerEvent(
                x=_event.x,
                y=_event.y,
                target=self._drag_target,
                type='pointer_drag'
            )
            self._renderer.dispatch_event(drag_event)

    def _pointer_up(self, _event):
        self._drag_started = False
        self._drag_target = None
