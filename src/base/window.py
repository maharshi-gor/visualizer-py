import sys

import pygfx as gfx
from wgpu.gui.auto import WgpuCanvas, run
from base.util import debounce

from loader.reader import Reader
from ui.controller import Controller
from visualization.visualizer import Visualizer


class Window:

    def __init__(self, reader):
        self._reader = reader

        self._canvas = WgpuCanvas()
        self._renderer = gfx.renderers.WgpuRenderer(self._canvas)

        self.win_size = (1280, 720)

        self._visualizer = Visualizer(gfx.Scene(), self._renderer,
                                      (0, 0, 0.7, 1),
                                      self.win_size)
        self._controller = Controller(gfx.Scene(), self._renderer,
                                      (0.7, 0, 0.3, 1),
                                      self.win_size,
                                      gfx.BackgroundMaterial((1, 1, 1)))

        gfx.OrbitController(self._visualizer.camera,
                            register_events=self._visualizer.viewport)

        self._canvas.add_event_handler(self._resized, 'resize')

        self._register_events()

    def _resized(self, event):
        self._visualizer.resized((event['width'], event['height']))
        self._controller.resized((event['width'], event['height']))
        debounce(self._animate)

    def _animate(self):
        self._visualizer.render()
        self._controller.render()
        self._renderer.flush()

    def show(self):
        self._canvas.request_draw(self._animate)

    def _update(self, _event):
        self._canvas.request_draw()

    def _register_events(self):
        self._renderer.enable_events()
        self._renderer.add_event_handler(self._update, 'pointer_drag')

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
