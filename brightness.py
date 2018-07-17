#!/usr/bin/env python

# -*- coding: utf-8 -*-


import machine
import time


PORT = 0
TIMEOUT = 0.01


def brightness(port: int=None, timeout: float=None):
    """
    Read brightness level from photo resistor connected to ADC and change PWM of LED.

    :param port: port number.
    :type port: int.
    :param timeout: sleep timeout.
    :type timeout: float.
    """

    adc = machine.ADC(port if port else PORT)
    pin = machine.Pin(port if port else PORT, machine.Pin.OUT)
    pwm = machine.PWM(pin)

    pin.on()

    while True:
        time.sleep(timeout if timeout else TIMEOUT)
        pwm.duty(1024 - adc.read())


def main():
    """
    Program main.
    """

    brightness()


if __name__ == "__main__":

    main()
