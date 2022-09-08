Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:34:34) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def recortar(num, lim_inf, lim_sup):
    return max(min(num, lim_sup), lim_inf)

recortar(-2, 0, 10)