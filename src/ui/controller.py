import pygfx as gfx

from base.section import Section
from ui.elements.slider import Slider


class Controller(Section):
    def __init__(self, scene, renderer, rect, win_size, bg=None):

        self._camera = gfx.OrthographicCamera()
        super().__init__(scene, renderer, rect, win_size, bg)

        slider = Slider()
        slider.add_to_scene(self._scene)
