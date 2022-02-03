from kivymd.app import MDApp
from kivy.lang import Builder
from kivy_garden.mapview import MapView


class MapViewApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Lime"
        mapview = MapView(zoom=0, lat=21.251384, lon=81.629641)
        return Builder.load_file('map2.kv')


MapViewApp().run()
