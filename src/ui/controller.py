import pygfx as gfx

from base.section import Section
from ui.elements.slider import Slider


class Controller(Section):
    def __init__(self, scene, renderer, rect, win_size, bg=None):

        self._camera = gfx.OrthographicCamera()
        super().__init__(scene, renderer, rect, win_size, bg)

        self._containers = []

        slider = Slider()
        slider.add_to_scene(self._scene)

        # self._scene.add_event_handler(self._resized, 'resize')

    def resized(self, win_size):
        super().resized(win_size)
