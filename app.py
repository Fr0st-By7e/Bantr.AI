import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from kivy.properties import StringProperty, BooleanProperty, NumericProperty
from kivy.lang import Builder

from companions import chat_Cinema_Rasigan, chat_Sharma_ji_ka_Beta, chat_Sporty_Chettan

Window.clearcolor = (0.07, 0.09, 0.13, 1)

AVATAR_PATHS = {
    "Cinema Rasigan": "Companion_Avatars/Cinema_Rasigan.png",
    "Sharma-ji ka Beta": "Companion_Avatars/Sharma-ji_ka_Beta.png",
    "Sporty Chettan": "Companion_Avatars/Sporty_Chettan.png"
}

COMPANION_FUNCS = {
    "Cinema Rasigan": chat_Cinema_Rasigan,
    "Sharma-ji ka Beta": chat_Sharma_ji_ka_Beta,
    "Sporty Chettan": chat_Sporty_Chettan
}


class ChatBubble(BoxLayout):
    text = StringProperty()
    avatar = StringProperty()
    is_user = BooleanProperty(False)
    bubble_width = NumericProperty(0)


Builder.load_string('''
#:import dp kivy.metrics.dp

<RoundCard@BoxLayout>:
    canvas.before:
        Color:
            rgba: 0.11, 0.14, 0.20, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [22, 22, 22, 22]

<SoftButton@Button>:
    background_normal: ''
    background_down: ''
    background_color: 0, 0, 0, 0
    color: 1, 1, 1, 1
    bold: True
    canvas.before:
        Color:
            rgba: (0.16, 0.72, 0.53, 1) if self.state == 'normal' else (0.13, 0.62, 0.46, 1)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [18, 18, 18, 18]

<GhostButton@Button>:
    background_normal: ''
    background_down: ''
    background_color: 0, 0, 0, 0
    color: 0.85, 0.90, 0.95, 1
    bold: True
    canvas.before:
        Color:
            rgba: (0.15, 0.18, 0.24, 1) if self.state == 'normal' else (0.12, 0.15, 0.21, 1)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [16, 16, 16, 16]

<CompanionCard@ButtonBehavior+BoxLayout>:
    companion_name: ''
    avatar_source: ''
    subtitle: ''
    orientation: 'vertical'
    spacing: dp(12)
    padding: dp(18)
    size_hint_y: None
    height: dp(240)
    canvas.before:
        Color:
            rgba: (0.13, 0.17, 0.23, 1) if self.state == 'normal' else (0.15, 0.20, 0.27, 1)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [26, 26, 26, 26]
    BoxLayout:
        size_hint_y: None
        height: dp(120)
        padding: 0, dp(6), 0, 0
        Image:
            source: root.avatar_source
            allow_stretch: True
            keep_ratio: True
    Label:
        text: root.companion_name
        font_size: '20sp'
        color: 1, 1, 1, 1
        halign: 'center'
        valign: 'middle'
        text_size: self.width, None
        size_hint_y: None
        height: self.texture_size[1]
    Label:
        text: root.subtitle
        font_size: '14sp'
        color: 0.72, 0.78, 0.84, 1
        halign: 'center'
        valign: 'top'
        text_size: self.width, None
        size_hint_y: 1

<ChatBubble>:
    size_hint_y: None
    height: bubble_label.texture_size[1] + dp(26)
    padding: dp(8), dp(4)
    spacing: dp(8)

    Widget:
        size_hint_x: None
        width: 0 if root.is_user else dp(6)

    AnchorLayout:
        anchor_x: 'right' if root.is_user else 'left'
        size_hint_y: None
        height: bubble_label.texture_size[1] + dp(26)

        BoxLayout:
            orientation: 'horizontal'
            size_hint: None, None
            width: min(root.width * 0.82, max(dp(120), bubble_label.texture_size[0] + dp(46)))
            height: bubble_label.texture_size[1] + dp(26)
            spacing: dp(8)
            padding: dp(12), dp(10)

            canvas.before:
                Color:
                    rgba: (0.20, 0.70, 0.52, 1) if root.is_user else (0.13, 0.17, 0.23, 1)
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [20, 20, 20, 20]

            Image:
                source: root.avatar if not root.is_user else ''
                size_hint: None, None
                size: dp(32), dp(32)
                opacity: 1 if not root.is_user else 0

            Label:
                id: bubble_label
                text: root.text
                color: 1, 1, 1, 1
                font_size: '16sp'
                halign: 'left'
                valign: 'middle'
                text_size: self.width, None
                size_hint_y: None
                height: self.texture_size[1]

    Widget:
        size_hint_x: None
        width: dp(6) if root.is_user else 0

<ChatScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(14)
        spacing: dp(12)

        BoxLayout:
            size_hint_y: None
            height: dp(84)
            padding: dp(14)
            spacing: dp(12)
            canvas.before:
                Color:
                    rgba: 0.10, 0.13, 0.18, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [24, 24, 24, 24]

            Image:
                source: root.avatar
                size_hint: None, None
                size: dp(52), dp(52)

            BoxLayout:
                orientation: 'vertical'
                spacing: dp(2)

                Label:
                    text: root.companion_name
                    color: 1, 1, 1, 1
                    font_size: '22sp'
                    bold: True
                    halign: 'left'
                    valign: 'middle'
                    text_size: self.size

                Label:
                    text: 'Online companion'
                    color: 0.65, 0.88, 0.77, 1
                    font_size: '13sp'
                    halign: 'left'
                    valign: 'middle'
                    text_size: self.size

            GhostButton:
                text: 'Home'
                size_hint: None, None
                size: dp(90), dp(44)
                on_release: root.go_home()

        BoxLayout:
            canvas.before:
                Color:
                    rgba: 0.08, 0.10, 0.15, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [26, 26, 26, 26]

            ScrollView:
                id: scroll
                do_scroll_x: False
                bar_width: dp(4)
                scroll_type: ['bars', 'content']

                BoxLayout:
                    id: chat_box
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(12)
                    spacing: dp(10)

        BoxLayout:
            size_hint_y: None
            height: dp(72)
            spacing: dp(10)
            padding: 0, 0, 0, dp(2)

            BoxLayout:
                padding: dp(12), dp(8)
                canvas.before:
                    Color:
                        rgba: 0.10, 0.13, 0.18, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [22, 22, 22, 22]

                TextInput:
                    id: message_input
                    multiline: False
                    hint_text: 'Type a message...'
                    background_color: 0, 0, 0, 0
                    foreground_color: 1, 1, 1, 1
                    hint_text_color: 0.55, 0.62, 0.70, 1
                    cursor_color: 0.16, 0.72, 0.53, 1
                    font_size: '17sp'
                    padding: dp(6), dp(10)
                    on_text_validate: root.send_message()

            SoftButton:
                text: 'Send'
                size_hint: None, None
                size: dp(92), dp(56)
                font_size: '16sp'
                on_release: root.send_message()

<CompanionSelectScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(16)

        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(150)
            padding: dp(18)
            spacing: dp(8)
            canvas.before:
                Color:
                    rgba: 0.10, 0.13, 0.18, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [28, 28, 28, 28]

            Label:
                text: 'Bantr.AI'
                font_size: '34sp'
                bold: True
                color: 1, 1, 1, 1
                halign: 'left'
                valign: 'middle'
                text_size: self.size

            Label:
                text: 'Pick a vibe and start chatting'
                font_size: '16sp'
                color: 0.70, 0.77, 0.84, 1
                halign: 'left'
                valign: 'middle'
                text_size: self.size

        GridLayout:
            cols: 1 if self.width < dp(700) else 3
            spacing: dp(16)
            size_hint_y: None
            height: self.minimum_height

            CompanionCard:
                companion_name: 'Sharma-ji ka Beta'
                avatar_source: 'Companion_Avatars/Sharma-ji_ka_Beta.png'
                subtitle: 'Sharp, witty, and always has something to say.'
                on_release: root.select_companion('Sharma-ji ka Beta')

            CompanionCard:
                companion_name: 'Cinema Rasigan'
                avatar_source: 'Companion_Avatars/Cinema_Rasigan.png'
                subtitle: 'Movie lover energy with fun, dramatic conversations.'
                on_release: root.select_companion('Cinema Rasigan')

            CompanionCard:
                companion_name: 'Sporty Chettan'
                avatar_source: 'Companion_Avatars/Sporty_Chettan.png'
                subtitle: 'Lively, energetic, and sports-obsessed chat mode.'
                on_release: root.select_companion('Sporty Chettan')
''')


class ChatScreen(Screen):
    companion_name = StringProperty()
    avatar = StringProperty()

    def go_home(self):
        self.manager.current = 'select'

    def __init__(self, companion_name, **kwargs):
        super().__init__(**kwargs)
        self.companion_name = companion_name
        self.avatar = AVATAR_PATHS[companion_name]
        self.companion_func = COMPANION_FUNCS[companion_name]

    def on_enter(self):
        self.ids = self.manager.get_screen(self.name).ids
        self.ids.chat_box.clear_widgets()

    def send_message(self):
        message = self.ids.message_input.text.strip()
        if not message:
            return
        self.add_bubble(message, True)
        self.ids.message_input.text = ''
        self.ids.scroll.scroll_y = 0
        self.get_response(message)

    def add_bubble(self, text, is_user):
        bubble = ChatBubble(
            text=text,
            avatar=self.avatar if is_user else AVATAR_PATHS[self.companion_name],
            is_user=is_user
        )
        self.ids.chat_box.add_widget(bubble)
        self.ids.scroll.scroll_y = 0

    def get_response(self, message):
        from threading import Thread
        from kivy.clock import Clock

        def fetch():
            try:
                response = self.companion_func(message)
            except Exception as e:
                response = f"[Error] {str(e)}"
            Clock.schedule_once(lambda dt: self.add_bubble(response, False))

        Thread(target=fetch).start()


class CompanionSelectScreen(Screen):
    def select_companion(self, companion_name):
        if not self.manager.has_screen(companion_name):
            self.manager.add_widget(ChatScreen(name=companion_name, companion_name=companion_name))
        self.manager.current = companion_name


class BantrAIApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(CompanionSelectScreen(name='select'))
        return sm


if __name__ == '__main__':
    BantrAIApp().run()