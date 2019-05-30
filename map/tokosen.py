from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
# 50N、100Wを見下ろす衛星の視点を用いて正射投影図投影を設定します。
# 低解像度の海岸線を使用する。

map = Basemap(projection='ortho',lat_0=45,lon_0=-100,resolution='l')
# 海岸線を描く、国境を塗る、大陸を塗る
map.drawcoastlines(linewidth=0.25)
map.drawcountries(linewidth=0.25)
map.fillcontinents(color='coral',lake_color='aqua')
# 地図投影領域（投影肢）の端を描画し、
map.drawmapboundary(fill_color='aqua')
# 緯度/経度グリッド線を30度ごとに描画します。
map.drawmeridians(np.arange(0,360,30))
map.drawparallels(np.arange(-90,90,30))
# 定期的な緯度/経度グリッドで何らかのデータを作ります。
nlats = 73; nlons = 145; delta = 2.*np.pi/(nlons-1)
lats = (0.5*np.pi-delta*np.indices((nlats,nlons))[0,:,:])
lons = (delta*np.indices((nlats,nlons))[1,:,:])
wave = 0.75*(np.sin(2.*lats)**8*np.cos(4.*lons))
mean = 0.5*np.cos(2.*lats)*((np.sin(2.*lats))**2 + 2.)
# lat / lonグリッドのネイティブマップ投影座標を計算します。
x, y = map(lons*180./np.pi, lats*180./np.pi)
# 地図上の等高線データ。
cs = map.contour(x,y,wave+mean,15,linewidths=1.5)
plt.title('contour lines over filled continent background')
plt.show()
