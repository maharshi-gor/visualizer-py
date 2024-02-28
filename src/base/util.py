import time


def debounce(fn, delay=500):
    """Debounce a function.

    Args:
    fn: The function to be debounced.
    delay: The delay in milliseconds.

    Returns:
    A debounced function.
    """

    timer = None

    def debounced(*args, **kwargs):
        nonlocal timer
        if timer is not None:
            timer.cancel()
        timer = time.Timer(delay, fn, args=args, kwargs=kwargs)
        timer.start()

    return debounced
