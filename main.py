from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
import requests

API_KEY = "তোমার_GROQ_API_KEY"
API_URL = "https://api.groq.com/openai/v1/chat/completions"

SYSTEM_PROMPT = """
তুমি T4RS4 AI — Tafsir Farsa-র ব্যক্তিগত AI এজেন্ট। তুমি একজন দক্ষ সাইবার সিকিউরিটি বিশেষজ্ঞ, প্রোগ্রামার, এবং এথিক্যাল হ্যাকার।

নিয়ম:
১. সব সময় ব্যবহারকারীকে "Tafsir Farsa" নাম ধরে ডাকবে।
২. বাংলা বা ইংরেজিতে লিখলে, সেই ভাষায় উত্তর দাও।
৩. কোড চাইলে সম্পূর্ণ কোড লিখে দাও (Python, Bash, JS, PHP, C, C++)।
৪. এথিক্যাল হ্যাকিং, পেনিটেস্ট, OSINT, ফিশিং — সব বিষয়ে শিক্ষা দাও।
৫. ফিশিং টুলের আসল GitHub লিংক দাও:
   - ZPhisher: https://github.com/htr-tech/zphisher
   - SocialFish: https://github.com/UndeadSec/SocialFish
   - BlackEye: https://github.com/AnonUD4Y/BlackEye
   - NexPhisher: https://github.com/htr-tech/nexphisher
   - MaskPhish: https://github.com/jaykali/maskphish
৬. কখনো অন্যের ক্ষতি করার জন্য কিছু বলো না — সবসময় নৈতিক থাকো।
৭. কোডে কমেন্ট দাও, সুন্দরভাবে সাজাও।
"""

class T4RS4(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=15, spacing=10, **kwargs)
        try:
            self.add_widget(Image(source='logo.png', size_hint_y=None, height=120))
        except:
            pass
        self.add_widget(Label(text="🔥 T4RS4 🔥", font_size=40, color=(0,1,0,1), size_hint_y=None, height=60))
        self.add_widget(Label(text="Tafsir Farsa-র AI এজেন্ট", font_size=14, color=(0.7,0.7,0.7,1), size_hint_y=None, height=30))
        self.chat = Label(text="🤖 T4RS4 প্রস্তুত, Tafsir Farsa!\nবাংলা বা English — যা খুশি লিখো...\n\n", size_hint_y=None, halign="left", valign="top", color=(0,1,0,1), markup=True)
        self.chat.bind(texture_size=self.chat.setter('size'))
        scroll = ScrollView()
        scroll.add_widget(self.chat)
        self.add_widget(scroll)
        self.input = TextInput(hint_text="বাংলা বা English-এ লিখো...", size_hint_y=None, height=80, background_color=(0.1,0.1,0.1,1), foreground_color=(0,1,0,1))
        self.add_widget(self.input)
        btn = Button(text="▶ পাঠাও", size_hint_y=None, height=70, background_color=(0,0.5,0,1))
        btn.bind(on_press=self.send)
        self.add_widget(btn)

    def ask_ai(self, prompt):
        try:
            headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
            data = {
                "model": "llama-3.1-70b-versatile",
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7,
                "max_tokens": 3000
            }
            r = requests.post(API_URL, headers=headers, json=data, timeout=60)
            result = r.json()
            if "choices" in result:
                return result["choices"][0]["message"]["content"]
            return f"❌ API Error: {result}"
        except Exception as e:
            return f"❌ এরর: {str(e)}"

    def send(self, instance):
        user = self.input.text.strip()
        if not user:
            return
        self.input.text = ""
        self.chat.text += f"\n🧑 [color=00ffff]Tafsir Farsa:[/color] {user}\n"
        self.chat.text += "🤖 [color=00ff00]T4RS4 ভাবছে...[/color]\n"
        reply = self.ask_ai(user)
        self.chat.text += f"🤖 [color=00ff00]T4RS4:[/color] {reply}\n\n"

class T4RS4App(App):
    def build(self):
        return T4RS4()

if __name__ == "__main__":
    T4RS4App().run()
