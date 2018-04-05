#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 13:17:51 2018

@author: unityspace
"""

def get_issuer(number):
    if (str(number)[:2] == '34' or str(number)[:2] == '37') and len(str(number)) == 15:
        return 'AMEX'
    elif str(number)[:4] == '6011' and len(str(number)) == 16:
        return 'Discover'
    elif (str(number)[:2] == '51' or str(number)[:2] == '52'or str(number)[:2] == '53' or str(number)[:2] == '54' or str(number)[:2] == '55') and len(str(number)) == 16:
        return 'Mastercard'
    elif str(number)[0] == '4' and (len(str(number)) == 13 or len(str(number)) == 16):
        return 'VISA'
    else:
        return 'Unknown'
    
    
    
"""
VENDORS = [
    # Name         Begins with    Length
    ['AMEX',       (34, 37),      (15,)],
    ['Discover',   (6011,),       (16,)],
    ['Mastercard', range(51, 56), (16,)],
    ['VISA',       (4,),          (13, 16)],
]


def get_issuer(number):
    return next((
        vendor[0] for vendor in VENDORS
        if len(str(number)) in vendor[2] and any(str(number).startswith(str(start)) for start in vendor[1])
   ), 'Unknown')
    
"""

"""
def get_issuer(number):
    s = str(number)
    return ("AMEX"       if len(s)==15 and s[:2] in ("34","37") else
            "Discover"   if len(s)==16 and s.startswith("6011") else
            "Mastercard" if len(s)==16 and s[0]=="5" and s[1] in "12345" else
            "VISA"       if len(s) in [13,16] and s[0]=='4' else
            "Unknown")

"""