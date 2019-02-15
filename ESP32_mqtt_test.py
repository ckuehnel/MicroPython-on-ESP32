import time, ubinascii, machine, network
from umqtt.simple import MQTTClient
from machine import Pin
from credentials import BROKER, BRPORT, BRUSER, BRPWD, SSID, PWD


# Many ESP32 boards have active-low "flash" button on GPIO0.
button = Pin(0, Pin.IN)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
  print('connecting to network...')
  wlan.connect(SSID, PWD)
  while not wlan.isconnected():
    pass
print('network config:', wlan.ifconfig())

# Default MQTT server to connect to
SERVER = BROKER
PORT = BRPORT
USER = BRUSER
PASSWORD = BRPWD
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b"test/led"


c = MQTTClient(CLIENT_ID, BROKER, BRPORT, BRUSER, BRPWD)
c.connect()
print("Connected to %s, waiting for button presses" % BROKER)
while True:
  while True:
    if button.value() != 0:
      break
    time.sleep_ms(200)
    print("Button pressed")
    c.publish(TOPIC, b"toggle")
    time.sleep_ms(200)

c.disconnect()
 
 
