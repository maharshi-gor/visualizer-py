from abc import abstractmethod


class UI:
    def __init__(self, position):
        self.position = position

    """
    Properties
    """
    @abstractmethod
    def _get_objects(self):
        RuntimeError('Method _get_objects should be implemented in '
                     + self.__class__.__name__)

    @property
    def position(self): return self._position

    @position.setter
    def position(self, position):
        self._set_position(position)

    @property
    def size(self): return (self._width, self._height)

    """
    Private methods
    """
    @abstractmethod
    def _set_position(self, position):
        RuntimeError('Method _set_position should be implemented in '
                     + self.__class__.__name__)

    """
    Public methods
    """
    def add_to_scene(self, scene):
        scene.add(*self._get_objects())

    def remove_from_scene(self, scene):
        scene.remove(*self._get_objects())

    def get_bounding_box(self):
        half_w = self._width / 2.0
        half_h = self._height / 2.0
        return [
            [self._position[0] - half_w, self._position[1] - half_h],
            [self._position[0] + half_w, self._position[1] + half_h]
        ]

    def get_rect(self):
        half_w = self._width / 2.0
        half_h = self._height / 2.0
        return (self._position[0] - half_w, self._position[1] - half_h,
                self._width, self._height)
