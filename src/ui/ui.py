from abc import abstractmethod


class UI:
    def __init__(self):
        pass

    @abstractmethod
    def _get_objects(self): pass

    @abstractmethod
    def _register_for_update(self): pass

    def add_to_scene(self, scene):
        scene.add(*self._get_objects())

    def remove_from_scene(self, scene):
        scene.remove(*self._get_objects())
