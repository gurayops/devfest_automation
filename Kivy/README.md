# Kivy Application

This directory contains a desktop and mobile application for controlling devices over MQTT. It is written for a Devfest event.
A working example can be found at:
	https://play.google.com/store/apps/details?id=org.gryl.devfestkutahya

The code is intended to be clear as well as easy to understand. For using it as a desktop application, you should have Kivy installed with Python 2.7.x on your system.

If you want to pack it as an APK file, you can use buildozer.spec file in this directory. You should change the application name, domain and other details according to your needs. After them, in a Buildozer installed environment, you can make APK file with this command:
	buildozer android debug
This command creates a APK file for debug. In order to get a release version for distributing the application, you can pack it with this command:
	buildozer android release

Both of this commands will result in an APK file in "bin" directory with their name and versions as filename. You can use Android guidelines for signing applications before trying to put them in Google Play.

Consult Kivy and Buildozer installation guide and Android documentation for more info and details.
