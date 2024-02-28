import pygfx as gfx

from base.section import Section
from ui.containers.slice import SliceContainer
from ui.elements.title import Title


class Controller(Section):
    def __init__(self,
                 scene: gfx.Scene,
                 renderer: gfx.Renderer,
                 rect: tuple,
                 bg=None,
                 on_close=None):

        self._camera = gfx.OrthographicCamera()
        super().__init__(scene, renderer, rect, bg)

        self._title = Title(self.rect[2], 30,
                            (-self.rect[2]/2, self.rect[3]/2 - 30))
        self._title.add_to_scene(self._scene)

        self._containers = []
        slice_container = SliceContainer()
        self._containers.append(slice_container)

        for container in self._containers:
            container.add_to_scene(self._scene)

        self._drag_started = False
        self._drag_target = None

        self._on_close = on_close
        self._register_events()

    def resized(self, win_size):
        super().resized(win_size)

        for container in self._containers:
            container.resize()

    def _register_events(self):

        self._scene.add_event_handler(self._handle_events, 'pointer_down',
                                      'pointer_move', 'pointer_up')

        self._scene.add_event_handler(
            self._pointer_down, 'ui_pointer_down'
        )
        self._scene.add_event_handler(
            self._pointer_move, 'ui_pointer_move'
        )
        self._scene.add_event_handler(
            self._pointer_up, 'ui_pointer_up'
        )

    def _handle_events(self, event):
        event.stop_propagation()
        ui_event = None
        if event.__class__.__name__ == 'PointerEvent':
            ui_event = gfx.PointerEvent(
                x=event.x - self.rect[0] - self.rect[2]/2,
                y=event.y - (self.rect[3])/2,
                target=event.target,
                type='ui_' + event.type
            )
        self._renderer.dispatch_event(ui_event)

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
                type='ui_pointer_drag'
            )
            self._renderer.dispatch_event(drag_event)

    def _pointer_up(self, _event):
        self._drag_started = False
        self._drag_target = None
