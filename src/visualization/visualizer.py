import pygfx as gfx

from base.section import Section


class Visualizer(Section):
    def __init__(self, scene, renderer, rect, bg=None):

        self._camera = gfx.PerspectiveCamera()
        super().__init__(scene, renderer, rect, bg)

        self._camera.local.position = ((0, 0, 0))
        self._camera.look_at((-1, 0, 0))

        self._viewport = gfx.Viewport(renderer, rect=self.rect)

    @property
    def viewport(self): return self._viewport
