from abc import abstractmethod
import pygfx as gfx


class Section:

    def __init__(self, scene, renderer, rect, bg=None):
        self._scene = scene
        self._renderer = renderer
        self.rect = rect
        self._bg = None

        self._camera.width = self.rect[2]
        self._camera.height = self.rect[3]

        if not bg:
            bg = gfx.BackgroundMaterial((0, 0, 0))
        self.set_background(bg)

    @property
    def scene(self): return self._scene

    @property
    def camera(self): return self._camera

    @abstractmethod
    def resized(self, win_size):
        RuntimeError('Method resized should be implemented in '
                     + self.__class__.__name__)

    def set_background(self, bg):
        """Set background of the controller section.

        Parameters
        ----------
        bg : Background or BackgroundMaterial
        """
        if self._bg:
            self._scene.remove(self._bg)

        if isinstance(bg, gfx.Background):
            self._bg = bg
        elif isinstance(bg, gfx.BackgroundMaterial):
            self._bg = gfx.Background(None, bg)
        else:
            ValueError('Inappropriate background data passed!')
        self._scene.add(self._bg)

    def render(self):
        self._renderer.render(
            self._scene, self._camera, rect=self.rect, flush=False
        )

    def get_bounding_box(self):
        return [
            [self.rect[0], self.rect[1]],
            [self.rect[0] + self.rect[2], self.rect[1] + self.rect[3]]
        ]
