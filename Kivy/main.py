from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
import paho.mqtt.client as mqtt


class RootWidget(BoxLayout):
	def __init__(self, **kwargs):
		super(RootWidget, self).__init__(**kwargs)
		self.client = mqtt.Client()
		self.client.on_connect = self.on_connect
		self.client.on_message = self.on_message
		self.client.connect("iot.eclipse.org", 1883, 60)
		self.client.loop_start()

        def on_message(self, client, userdata, msg):
		self.ids.temp.text = str(msg.payload) + " C"

	def on_connect(self, client, userdata, flags, rc):
		self.client.subscribe("/devfest/temp")

	def stateChanged(self, newState):
		self.client.publish("/devfest", int(newState))
		

class DevFestApp(App):
	def build(self):
		return RootWidget()
		

if __name__ == '__main__':
	DevFestApp().run()
