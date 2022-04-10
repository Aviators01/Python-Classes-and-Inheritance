"""
Timothy Queva
CS3010 Lab2
Jan. 29, 2021

This lab consists of two parts. Part 1 is the calculation of where two lines
intersect while part 2 is deals with a Time object elapsed time since creation.
Both will involve class creation.
"""

'''Part1:
To find the interception of two lines, we figure out the equations (y=mx+b) of
each line and set them equal to each other since they will have the same x,y
at the point of intersection.
'''

class Intersection:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def find_slope(self):
        return (self.x2-self.x1) / (self.y2-self.y1)
    
    def find_yintercept(self,m,x,y):
        #y=mx+b --> b = -mx +y
        return -(m*x) + y
    
    
    @staticmethod
    def find_intercept(line1,line2):
        m1 = line1.find_slope()
        m2 = line2.find_slope()
        
        b1 = line1.find_yintercept(m1,line1.x1,line1.y1)
        b2 = line2.find_yintercept(m2,line1.x2,line2.y1)
        
        '''Algebra to equate the two lines
        m1x+b1 = m2x+b2
        m1x -m2x +b1 -b2 = 0
        x(m1-m2) + b1 -b2 = 0
        x=(b2-b1)/(m1-m2)
        '''
        
        x =(b2-b1)/(m1-m2)
        y = m1*x + b1
        
        print()
        print("The point of intersection for line [" + str(line1.x1) + "," + 
              str(line1.y1) + "," + str(line1.x2) + "," + str(line1.y2) +
              "] and line [" + str(line2.x1) + "," + str(line2.y1) + "," +
              str(line2.x2) + "," + str(line2.y2) + "] is at x,y of " +
              "%0.2f, %0.2f" %(x,y))
        

if __name__ == '__main__':
    line1 = input("Please enter end points of the first line " +
                  "(x1,y1,x2,y2): ")
    x1,y1,x2,y2 = line1.split(",")
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    line1 = Intersection(x1,y1,x2,y2)
    
    line2 = input("Please enter end points of the second line " +
                  "(x1,y1,x2,y2): ")
    x1,y1,x2,y2 = line2.split(",")
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    line2 = Intersection(x1,y1,x2,y2)
    
    Intersection.find_intercept(line1,line2)