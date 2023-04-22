import pygetwindow as gw


def focus_window(name):
    res = gw.getWindowsWithTitle(name)[0]
    res.restore()
    res.minimize()
    res.restore()
    res.maximize()
