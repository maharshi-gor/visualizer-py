import sys

import pygfx as gfx
from wgpu.gui.auto import WgpuCanvas, run

from loader.reader import Reader
from ui.controller import Controller
from visualization.visualizer import Visualizer


class Window:

    def __init__(self, reader):
        self._reader = reader

        self._canvas = WgpuCanvas()
        self._renderer = gfx.renderers.WgpuRenderer(self._canvas)
        self._controller = Controller(gfx.Scene(),
                                      gfx.BackgroundMaterial((1, 1, 1)))
        self._visualizer = Visualizer(gfx.Scene())
        self._camera = gfx.PerspectiveCamera(70, 16 / 9)
        self._visualizer_oc = gfx.OrbitController(
            self._camera, register_events=self._renderer)
        self._c_camera = gfx.OrthographicCamera(0.3 * 1280, 720)
        self.win_size = (1280, 720)
        self._camera.local.position = ((0, 0, 0))
        self._camera.look_at((-1, 0, 0))

    def _animate(self):
        w, h = self.win_size
        self._renderer.render(
            self._visualizer.scene, self._camera,
            rect=(0.0 * w, 0.0 * h, 0.7 * w, 1.0 * h),
            flush=False
        )
        self._renderer.render(
            self._controller.scene, self._c_camera,
            rect=(0.7 * w, 0.0 * h, 0.3 * w, 1.0 * h),
            flush=False
        )
        self._renderer.flush()

    def show(self):
        """Display canvas.
        """
        self._canvas.request_draw(self._animate)

    @property
    def win_size(self): return self._canvas.get_logical_size()

    @win_size.setter
    def win_size(self, size):
        w, h = size
        self._canvas.set_logical_size(w, h)

    @property
    def controller(self): return self._controller

    @property
    def visualizer(self): return self._visualizer


def main():
    reader = Reader(sys.argv[1:])
    window = Window(reader)
    window.show()
    run()
