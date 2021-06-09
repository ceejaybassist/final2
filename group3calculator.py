import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

# Designate our kv design file
Builder.load_file('group3calculator.kv')

class MyLayout(Widget):

    def num_sound(self):
        sound = SoundLoader.load('sounds/LaughTrack.wav')
        if sound:
            sound.play()

    def clear(self):
        self.ids.calc_input.text = '0'

    def button_press(self, button):
        prior = self.ids.calc_input.text

        if "SYNTAX ERROR" in prior:
                prior = ''

        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    def posneg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")
        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = f'{prior}'
        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = f'{prior}'

        num_list = prior.split("-")
        if "-" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = f'{prior}'
        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = f'{prior}'

        num_list = prior.split("*")
        if "*" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = f'{prior}'
        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = f'{prior}'

        num_list = prior.split("/")
        if "/" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = f'{prior}'
        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = f'{prior}'

    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = prior
        self.ids.calc_input.text = f'{prior}{sign}'

    def equals(self):
        prior = self.ids.calc_input.text

        try:
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = str("SYNTAX ERROR")

class CalculatorApp(App):
    def build(self):
        self.icon = 'images/calculatoricon.ico'
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()