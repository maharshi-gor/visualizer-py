import pygfx as gfx


class Section:

    def __init__(self, scene, bg=None):
        self._scene = scene
        self._bg = None
        if not bg:
            bg = gfx.BackgroundMaterial((0, 0, 0))
        self.set_background(bg)

    @property
    def scene(self): return self._scene

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
