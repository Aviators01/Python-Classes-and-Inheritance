"""
Timothy Queva
CS3010 Lab2
Jan. 29, 2021

This lab consists of two parts. Part 1 is the calculation of where two lines
intersect while part 2 is deals with a Time object elapsed time since creation.
Both will involve class creation.
"""

'''Part2:
To find the interception of two lines, we figure out the equations (y=mx+b) of
each line and set them equal to each other since they will have the same x,y
at the point of intersection.
'''
from datetime import datetime

class Time:
    def __init__(self):
        self.__hour = datetime.now().hour
        self.__min = datetime.now().minute
        self.__sec = datetime.now().second
        
        print("Time at creation of object is >>> " + str(self.__hour) + ":" +
              str(self.__min) + ":" + str(self.__sec) + " (h:m:s)")
    
    def get_hour(self):
        return self.__hour
    
    def get_min(self):
        return self.__min
    
    def get_sec(self):
        return self.__sec
    
    def setTime(self,lapse):
        self.__tmpTime = self.__hour*60*60 + self.__min*60 + self.__sec 
        self.__tmpTime += lapse
        
        self.__hour = self.__tmpTime//(60*60)
        self.__tmpTime = self.__tmpTime%(60*60)
        
        self.__min = self.__tmpTime//(60)
        self.__tmpTime = self.__tmpTime%(60)
        
        self.__sec = self.__tmpTime

if __name__ == '__main__':
    t_obj = Time()
    
    lapse = int(input("Please enter elapsed time in seconds: "))
    t_obj.setTime(lapse)
    
    print("The new time is >>> " + str(t_obj.get_hour()) + ":" + 
          str(t_obj.get_min()) + ":" + str(t_obj.get_sec()))