class Container:
    def __init__(self):
        self._isOpen = False
        self._elements = []

    def set_position(self, position):
        for element in self._elements:
            element.set_position(position)

    def add_to_scene(self, scene):
        for element in self._elements:
            element.add_to_scene(scene)
