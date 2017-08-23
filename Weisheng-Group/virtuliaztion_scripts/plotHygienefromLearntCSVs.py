from geoplotlib.core import BatchPainter
import geoplotlib
from geoplotlib.colors import colorbrewer
from geoplotlib.utils import epoch_to_str, BoundingBox, read_csv
from geoplotlib.layers import BaseLayer


#REMEMBER: HIGH HYGIENE SCORE = BAD!

class TrailsLayer(BaseLayer):
    def __init__(self):
        self.df = read_csv('bayesian_ridge_regression_score.csv')
        self.cmap = colorbrewer(self.df['value'], alpha=255)
        self.maxT = self.df['value'].max()
        self.painter = BatchPainter()

    def draw(self, proj, mouse_x, mouse_y, ui_manager):
        self.painter = BatchPainter()
        for score in set(self.df['value']):
            if score <= self.maxT / 3:
                grp = self.df.where(self.df['value'] == score)
                self.painter.set_color([255, 255,0])

            if score > self.maxT / 3 and score <= 2 * self.maxT / 3:
                grp = self.df.where(self.df['value'] == score)
                self.painter.set_color([255, 165, 0])

            if score > 2 * self.maxT / 3:
                grp = self.df.where(self.df['value'] == score)
                self.painter.set_color([255, 0, 0])

            x, y = proj.lonlat_to_screen(grp['lon'], grp['lat'])
            self.painter.points(x, y, 10, rounded=True)
            self.painter.batch_draw()

    def bbox(self):
        return BoundingBox(north=40.785091, west=-73.968285, south=39.905711, east=-74.009512)

#geoplotlib.set_bbox(BoundingBox.USA)
geoplotlib.add_layer(TrailsLayer())
geoplotlib.show()