from machine import Pin,I2C
import ssd1306

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)

lcd=ssd1306.SSD1306_I2C(128,64,i2c)

lcd.text("DFRobot",0,0)
lcd.text("chengdu",24,16)
lcd.text("123456",64,24)
lcd.show()
