from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.image import Image
from kivymd.uix.swiper import MDSwiper, MDSwiperItem
from kivy.core.window import Window
from kivy.clock import Clock

from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty

Window.size = (375, 667)

class MenuItem(MDBoxLayout):
    icon = StringProperty("")
    text = StringProperty("")

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print(f"点击了：{self.text}")
            return True
        return super().on_touch_down(touch)

class MyGridItem(MDBoxLayout):
    icon = StringProperty("")
    text = StringProperty("")

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print(f"点击了：{self.text}")
            return True
        return super().on_touch_down(touch)
    
class MainApp(MDApp):
    def build(self):
        self.root = Builder.load_file("kv/main.kv")
        self.add_swiper_items()
        return self.root
    
    def add_swiper_items(self):
        for i in range(3):  # 添加3个轮播项
            swiper_item = MDSwiperItem()
            img = Image(source=f"banner/banner_{i}.png", 
                        allow_stretch=True,
                        fit_mode="fill")  # 中心定位)
            swiper_item.add_widget(img)
            self.root.ids.home.ids.swiper.add_widget(swiper_item)
    def on_scan(self):
        print("点击了：扫一扫")

    def on_service(self):
        print("点击了：客服")

    def on_settings(self):
        print("点击了：设置")

    def on_search(self):
        # 获取输入内容
        input_text = self.root.ids.search_input.text.strip()
        print("用户输入了：", input_text)
        # 可以在这里触发搜索逻辑
    def on_login_label_click(self):
        print("点击了登录/注册")
        # 打开登录页面或弹出对话框

if __name__ == '__main__':
    MainApp().run()