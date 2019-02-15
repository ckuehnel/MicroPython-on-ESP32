# Affichage OLED SSD1306 en MicroPython | MicroPython SSD1306  OLED display
# affiche les mesures d'un capteur BME280 i2c sur un 鑼卌ran OLED
# Display values from an i2c BME280 sensor on OLED screen
# https://projetsdiy.fr - https://diyprojects.io (dec. 2017)

import machine, time, ssd1306, bme280
from machine import Pin,I2C

pinScl      = 22  #ESP8266 GPIO5 (D1)
pinSda      = 18  #ESP8266 GPIO4 (D2)
addrOled    = 60  #0x3c
addrBME280  = 118 #0x76
hSize       = 32  # Hauteur ecran en pixels | display heigh in pixels
wSize       = 128 # Largeur ecran en pixels | display width in pixels

oledIsConnected = False
bmeIsConnected  = False
temp = 0
pa = 0
hum = 0

# init ic2 object
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000) # ESP32 DevKit

# Scan le bus i2c et verifie si le BME280 et l'ecran OLED sont connectes
# Scan i2c bus and check if BME2 and OLDE display are connected
print('Scan i2c bus...')
devices = i2c.scan()
if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))
  for device in devices: 
    if device == addrOled:
      oledIsConnected = True
    if device == addrBME280:
      bmeIsConnected = True  
    print(device)

while True:
 if bmeIsConnected:
  bme = bme280.BME280(i2c=i2c,address=addrBME280)
  print("BME280 values:")
  print(bme.values)
  temp,pa,hum = bme.values 
  print(temp)
  print(pa) 
  print(hum)
  
 if oledIsConnected:
  oled = ssd1306.SSD1306_I2C(wSize, hSize, i2c, addrOled)
  oled.fill(0)
  if bmeIsConnected:
     
     oled.text("Temp. "+temp, 0, 0)
     oled.text("PA "+pa, 0, 10)
     oled.text("Hum. "+hum, 0, 20)
     oled.show()
  else:   
    oled.text("BME KO", 0, 0)
    oled.show()
 else:
  print('! No i2c display')
 time.sleep_ms(5000)

