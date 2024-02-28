from base.container import Container
from ui.elements.slider import Slider


class SliceContainer(Container):

    def __init__(self):
        super().__init__()

        slider = Slider()
        self._elements.append(slider)
