# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 17:17:30 2021

@author: DELL
"""

import random
import matplotlib.pyplot as plt
account=0
x=[]
y=[]
for i in range(365):
    x.append(i+1)
    bet=random.randint(1,10)
    lucky_draw=random.randint(1, 10)
    print("Bet: ", bet)
    print("lucky draw: ",lucky_draw)
    if bet==lucky_draw:
        account=account+900-100
    else:
        account=account-100
    y.append(account)
print('Ammount in your game account: ', account)
plt.plot(x, y)
plt.show()