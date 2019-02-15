# ADC_loop_ESP32.py
# Reads the ESP32 ADC and measures the time and speed to read 20000 samples.
# based on http://www.robertocolistete.net/MicroPython/ADC_loop.zip

import machine
from machine import Pin
from machine import ADC
import time

def ADCloopBenchmark():
  adc = machine.ADC(Pin(32))
  adcread = adc.read()
  t1 = time.ticks_us()
  for i in range(20000):
      adcread = adc.read()
  t2 = time.ticks_us()
  print("20000 ADC readings done after %u us." %(t2-t1))
  print("Mean time for each ADC reading = %15.13f us" % ((t2-t1)/20000.0))
  print("ADC reading = %15.13f ksamples/s" % (1000/((t2-t1)/20000.0)))

ADCloopBenchmark()

