# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:10:59 2020

@author: HP-intel
"""

import webbrowser
import time
import pyautogui as gui

interval  = 60
position = 664,310
 
numbers={918955503052,919928829271}

msg="Hi"

for i in numbers:
    url='https://wa.me/{}?text={}'.format(i,msg)
    
    webbrowser.open(url)
    time.sleep(15)
    gui.click(position)
    time.sleep(5)
    gui.click(671,399)
    time.sleep(30)
    gui.press('enter')
    time.sleep(interval)



    