from base.section import Section
from ui.elements.slider import Slider


class Controller(Section):
    def __init__(self, scene, bg=None):
        super().__init__(scene, bg)
        slider = Slider()
        slider.add_to_scene(self._scene)
