import math


        # KULA
def objetosc_kula(r):
    return  3 / 4 * 3.14 * r ** 3

def masa_kula(r, d):
    return 3 / 4 * 3.14 * r ** 3 * d

def pole_kula(r):
    return 4 * 3.14 * r ** 2


      # CZWOROŚCIAN FOREMNY

def objetosc_kostka(a):
    return ((a ** 2 * math.sqrt(3)) / 4) * (a * math.sqrt(6)) / 3 / 3

def pole_kostka(a):
    return a ** 2 * math.sqrt(3)

def masa_kostka(a, d):
    return ((a ** 2 * math.sqrt(3)) / 4) * (a * math.sqrt(6)) / 3 * d / 3


        # ELIPSOIDA


def objetosc_elipsoida(a, b, c):
    return 4 / 3 * a * b * c * 3.14


def pole_elipsoida(a, b, x):
    return 2 * 3.14 * b * (b + (a / x) * math.asin(x))


def masa_elipsoida(a, b, c, d):
    return objetosc_elipsoida(a, b, c) * d

# OSTROSŁUP


def objetosc_ostroslupa(a, b, H):
    return 1 / 3 * a * b * H


def pole_ostroslupa(a, b, h):
    return a * b + a * h + b * h


def masa_ostroslupa(a, b, d, H):
    return 1 / 3 * a * b * H * d

 # STOŻEK


def pole_stozek(r, l):
    return 3.14 * r ** 2 + 3.14 * r * l


def objetosc_stozek(r, H):
    return 1 / 3 * 3.14 * r ** 2 * H


def masa_stozek(d, r, H):
    return objetosc_stozek(r, H) * d

 # WALEC


def pole_walec(r, H):
    return 2 * 3.14 * r ** 2 + 2 * 3.14 * r * H


def objetosc_walec(r, H):
    return 3.14 * r ** 2 * H


def masa_walec(r, H, d):
    return objetosc_walec(r, H) * d


