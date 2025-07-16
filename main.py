from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.image import Image
from kivymd.uix.swiper import MDSwiper, MDSwiperItem
from kivy.core.window import Window
from kivy.clock import Clock

Window.size = (375, 667)

class MainApp(MDApp):
    def build(self):
        self.root = Builder.load_file("main.kv")
        self.add_swiper_items()
        return self.root
    
    def add_swiper_items(self):
        for i in range(3):  # 添加3个轮播项
            swiper_item = MDSwiperItem()
            img = Image(source=f"banner/banner_{i}.png", 
                        allow_stretch=True,
                        fit_mode="fill")  # 中心定位)
            swiper_item.add_widget(img)
            self.root.ids.swiper.add_widget(swiper_item)
    def on_scan(self):
        print("点击了：扫一扫")

    def on_service(self):
        print("点击了：客服")

    def on_settings(self):
        print("点击了：设置")
    
if __name__ == '__main__':
    MainApp().run()