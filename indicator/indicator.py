#!/usr/bin/env python

# -*- coding: utf-8 -*-

# mp
# indicator/indicator.py


import time

import machine


TIMEOUT = 0.1

# segments pins
A = machine.Pin(16, machine.Pin.OUT)
B = machine.Pin(5, machine.Pin.OUT)
C = machine.Pin(4, machine.Pin.OUT)
D = machine.Pin(0, machine.Pin.OUT)
E = machine.Pin(14, machine.Pin.OUT)
F = machine.Pin(12, machine.Pin.OUT)
G = machine.Pin(13, machine.Pin.OUT)
SEGMENTS = [A, B, C, D, E, F, G, ]

# symbols
SYMBOL_1 = [B, C, ]
SYMBOL_2 = [A, B, G, E, D, ]
SYMBOL_3 = [A, B, G, C, D, ]
SYMBOL_4 = [F, G, B, C, ]
SYMBOL_5 = [A, F, G, C, D, ]
SYMBOL_6 = [A, F, G, C, D, E, ]
SYMBOL_7 = [A, B, C, ]
SYMBOL_8 = [A, B, C, D, E, F, G, ]
SYMBOL_9 = [A, B, C, D, F, G, ]
SYMBOL_0 = [A, B, C, D, E, F, ]
SYMBOL_A = [E, F, A, B, C, G, ]
SYMBOL_B = [F, E, D, C, G, ]
SYMBOL_C = [A, F, E, D, ]
SYMBOL_D = [B, C, D, E, G, ]
SYMBOL_E = [A, F, G, E, D, ]
SYMBOL_F = [A, F, G, E, ]
SYMBOL_G = [A, F, E, D, C, ]
SYMBOL_H = [F, G, B, E, C, ]
SYMBOLS = {
    "1": SYMBOL_1,
    "2": SYMBOL_2,
    "3": SYMBOL_3,
    "4": SYMBOL_4,
    "5": SYMBOL_5,
    "6": SYMBOL_6,
    "7": SYMBOL_7,
    "8": SYMBOL_8,
    "9": SYMBOL_9,
    "0": SYMBOL_0,
    "A": SYMBOL_A,
    "B": SYMBOL_B,
    "C": SYMBOL_C,
    "D": SYMBOL_D,
    "E": SYMBOL_E,
    "F": SYMBOL_F,
    "G": SYMBOL_G,
    "H": SYMBOL_H,
}


def symbol(s: list=None):
    """
    Show symbol.

    :param s: symbol segments to power on.
    :type s: list.
    """

    clear()

    if s:
        for segment in s:
            segment.on()


def clear():
    """
    Clear display.
    """

    for segment in SEGMENTS:
        segment.off()


def text(t: str=None, timeout: float=None):
    """
    Show text.

    :param t: text to display.
    :type t: str.
    :param timeout: sleep timeout.
    :type timeout: float.
    """

    if t:
        for letter in t:
            if letter.upper() in list(SYMBOLS.keys()):
                symbol(SYMBOLS.get(letter))
                time.sleep(timeout if timeout else TIMEOUT)

    clear()


def main():
    """
    Program main.
    """

    clear()
    text("0x76696e74323168")  # vint21h (in hex)


if __name__ == "__main__":

    main()
