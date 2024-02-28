from abc import abstractmethod


class UI:
    def __init__(self, position):
        self.position = position

    @abstractmethod
    def _get_objects(self):
        RuntimeError('Method _get_objects should be implemented in '
                     + self.__class__.__name__)

    @abstractmethod
    def set_position(self, win_size):
        RuntimeError('Method _set_position should be implemented in '
                     + self.__class__.__name__)

    def add_to_scene(self, scene):
        scene.add(*self._get_objects())

    def remove_from_scene(self, scene):
        scene.remove(*self._get_objects())
