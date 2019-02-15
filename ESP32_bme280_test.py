from machine import Pin,I2C
import time, bme280

addrBME280  = 0x76

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000) # ESP32 DevKit

bme = bme280.BME280(i2c=i2c,address=addrBME280)

print("\nRead BME280 sensor every 10 s ...")

while True:
  #print(bme.values)
  temp,pa,hum = bme.values 
  print("Temperature = ", temp)
  print("Humidity\t= ", hum)
  print("Pressure\t= ", pa)
  time.sleep(10)

