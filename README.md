# Devfest Automation Project

This project includes an Android application written in Python with Kivy Framework and a Raspberry Pi application that controls a relay and sends temperature value from LM75 to MQTT server.

Mobile application can be used as a desktop app as well. The only thing you need is to install Kivy on your computer and run application with it.

You should change MQTT server and topic according to your server information.

For packaging the application as an APK file for android, you can use buildozer tool after editing buildozer.spec file according to your needs and information. After it, run:

	buildozer init
	buildozer android debug

This will give a debug APK file in the bin directory at current path.
