from machine import Pin
import time

red = Pin(15, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(13, Pin.OUT)


def all_off():
    red.value(0)
    yellow.value(0)
    green.value(0)


while True:
    all_off()
    red.value(1)
    print('DO - Dung')
    time.sleep(5)

    all_off()
    green.value(1)
    print('XANH - Di')
    time.sleep(5)

    all_off()
    yellow.value(1)
    print('VANG - Chuan bi dung')
    time.sleep(2)
