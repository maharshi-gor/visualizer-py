class Color:
    def __init__(self):
        """Create a wrapper for accessing colors easily. It can support hex and
        rgba colors. It assumes 6-character hex or (R, G, B, alpha) where the
        range should be provided on 255 base.
        """
        pass

    @staticmethod
    def _normalize(value):
        return tuple(v/255.0 for v in value[:3])

    @staticmethod
    def get_color(color):
        if isinstance(color, str) and color[0] == '#':
            color = color.lstrip('#')
            color = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
            r, g, b = Color._normalize(color)
            return (r, g, b, 1)

        elif isinstance(color, tuple) and len(color) <= 4:

            if max(color > 255.0) and min(color < 0):
                ValueError('color values should not be grater than 255 or less'
                           + 'than 0')

            r, g, b = Color._normalize(color)

            if len(color) == 3 or (len(color) == 4 and color[3] > 1):
                color = (r, g, b, 1)
            else:
                color = (r, g, b, color[3])

            return color
