from base.container import Container
from ui.elements.slider import Slider


class SliceContainer(Container):

    def __init__(self, position, width, height, text='Slice Container'):
        super().__init__(position, width, height)

        self._title.title = text
        slider = Slider()
        self._elements.append(slider)
