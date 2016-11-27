#!/usr/bin/python -p
import paho.mqtt.client as mqtt
from ctypes import cdll
from time import sleep
import thread
sleep(20)
boardLib = cdll.LoadLibrary('/home/pi/lib.so')

boardLib.pe2a_DO_DI_init()
# From https://github.com/lexruee/lm75
from tentacle_pi.LM75 import LM75
lm = LM75(0x48,"/dev/i2c-1")

def sendTemp():
    while True:
        client.publish("/devfest/temp", lm.temperature())
        sleep(1)

def on_connect(client, userdata, flags, rc):
    client.subscribe("/devfest")
    thread.start_new_thread(sendTemp, tuple() )

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    message = msg.payload
    if message == '1': boardLib.pe2a_DO_setHigh(7)
    elif message == '0': boardLib.pe2a_DO_setLow(7)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)

client.loop_forever()
