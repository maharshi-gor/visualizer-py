class Container:
    def __init__(self):
        self._isOpen = False
        self._elements = []
        # self._size = size

    def resized(self, win_size):
        pass

    def add_to_scene(self, scene):
        for element in self._elements:
            element.add_to_scene(scene)
