from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen,SwapTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock

Builder.load_file("templates/splashScreen.kv")
Builder.load_file("templates/loginScreen.kv")

class SplashScreen(Screen):
    pass
class LoginScreen(Screen):
    pass

#Main call all Screens
class Chatbotx(App):
    def build(self):
        sm1 = ScreenManager(transition = SwapTransition())
        sm1.add_widget(SplashScreen(name = "splashManager"))
        sm1.add_widget(LoginScreen(name = "loginManager"))
        Clock.schedule_once(self.show_next_screen, 3)
        return sm1
    def show_next_screen(self,dt):
        self.root.current = "loginManager"

if __name__ == '__main__':
   Chatbotx().run()
