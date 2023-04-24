import pygetwindow as gw

# funtion that focuses a windows application
def focus_window(name):
    res = gw.getWindowsWithTitle(name)[0]
    res.restore()
    res.minimize()
    res.restore()
    res.maximize()
