from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, NumericProperty


Window.size = (375, 667)

# 注册字体
LabelBase.register(name="Roboto",
                   fn_regular="fonts/pingfang-hei.ttf",
                   fn_bold="fonts/pingfang-hei.ttf")


class GridItem(MDBoxLayout):
    pass

class DataCard(Screen):
    icon_source = StringProperty("")   # 图标路径
    item_name = StringProperty("")     # 名称
    rating = NumericProperty(0)        # 评分（数字）

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
        return self.root

    def on_scan(self):
        print("点击了：扫一扫")

    def on_service(self):
        print("点击了：客服")

    def on_settings(self):
        print("点击了：设置")

    def on_search(self):
        # 获取输入内容
        input_text = self.root.ids.search.ids.search_input.text.strip()
        print("用户输入了：", input_text)
        # 可以在这里触发搜索逻辑
    def on_login_label_click(self):
        print("点击了登录/注册")
        # 打开登录页面或弹出对话框
    def show_toast(self, msg):
        print(msg)
if __name__ == '__main__':
    MainApp().run()