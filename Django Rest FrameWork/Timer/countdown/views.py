from django.shortcuts import render
import datetime

# Create your views here.
class Timer:
    thenHr,thenMin,thenSec=0,0,0
    def __init__(self, amount, unit):
        if amount>0:
            self.amount=amount
            if unit == 'hrs' or unit=='min' or unit=='sec':
                self.unit=unit
                self.setTimer()
    
    def setTimer(self):
        now=datetime.datetime.now()
        print(now)
        
        self.formatTime(self.amount,self.unit)
        print(self.thenHr,self.thenMin, self.thenSec)       
        then=datetime.datetime(now.year, now.month, now.day,now.hour+self.thenHr, now.minute+self.thenMin, now.second+self.thenSec)
        print(then)
        #startTimer(now,then)
    
    def formatTime(self, amount, unit):
        if unit=='sec':
            if amount>=60:
                r=amount%60
                self.thenSec=r
                q=int(amount/60)
                if q>=60:
                    qr=q%60
                    self.thenMin=qr
                    qq=int(q/60)
                    self.thenHr=qq
                else:
                    self.thenMin=q
            else:
                self.thenSec=amount

        elif unit=='min':
            if self.amount>=60:
                r=self.amount%60
                self.thenMin=r
                q=int(self.amount/60)
                self.thenHr=q



obj=Timer(61,'min')