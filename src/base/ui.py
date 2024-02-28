from abc import abstractmethod


class UI:
    def __init__(self, position):
        self._position = position

    @abstractmethod
    def _get_objects(self): pass

    @abstractmethod
    def _set_position(self, win_size):
        pass

    def resized(self, win_size):
        self._set_position(win_size)

    def add_to_scene(self, scene):
        scene.add(*self._get_objects())

    def remove_from_scene(self, scene):
        scene.remove(*self._get_objects())
