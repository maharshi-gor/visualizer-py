import pygfx as gfx


class Section:

    def __init__(self, scene, renderer, rect, win_size, bg=None):
        self._scene = scene
        self._renderer = renderer
        self._rect = rect
        self._bg = None
        self._update_bounding_box(win_size)

        self._camera.width = self._bounding_box[2]
        self._camera.height = self._bounding_box[3]

        if not bg:
            bg = gfx.BackgroundMaterial((0, 0, 0))
        self.set_background(bg)

    @property
    def scene(self): return self._scene

    @property
    def camera(self): return self._camera

    @property
    def size(self):
        return (
            abs(self._bounding_box[2] - self._bounding_box[0]),
            abs(self._bounding_box[1] - self._bounding_box[3])
        )

    @property
    def bounding_box(self): return self._bounding_box

    def _update_bounding_box(self, win_size):
        w, h = win_size
        self._bounding_box = (
            self._rect[0] * w,
            self._rect[1] * h,
            self._rect[2] * w,
            self._rect[3] * h
        )

    def resized(self, win_size):
        self._update_bounding_box(win_size)

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
            self._scene, self._camera, rect=self._bounding_box, flush=False
        )
