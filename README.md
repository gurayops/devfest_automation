# Devfest Automation Project

This project includes an Android application written in Python with Kivy Framework and a Raspberry Pi application that controls a relay and sends temperature value from LM75 to MQTT server.

Mobile application can be used as a desktop app as well. The only thing you need is to install Kivy on your computer and run application with it.

You should change MQTT server and topic according to your server information.

# Installation
Firstly install some dependencies. For LM75, this project uses a library prepared by lexruee:
	https://github.com/lexruee/lm75
In order to install it, you may want to use these commands:
	sudo apt install python-dev i2c-tools libi2c-dev
	git clone https://github.com/lexruee/lm75.git
	sudo python setup.py install
You should check this modules page for updates.

For communicating with PE2A board, its own library is employed. You should compile it as a static object file(with .so extension if matters). You may prefer to change it according to your hardware if you are utilizing different parts.

Lastly, run the code like this:
	sudo python raspberry.py


For packaging the application as an APK file for android, you can use buildozer tool after editing buildozer.spec file according to your needs and information. After it, run:

	buildozer init
	buildozer android debug

This will give a debug APK file in the bin directory at current path.
Consider looking Kivy directory for mobile/desktop application and packaging details.
