import matplotlib.pyplot as plot
from mpl_toolkits.basemap import Basemap

map = Basemap(
    llcrnrlon=128, urcrnrlon=147,
    urcrnrlat=47, llcrnrlat=30,
    resolution="l")

map.drawcoastlines()
plot.show()
