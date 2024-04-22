import math

def find_distance(x,y):
    dist=math.sqrt(x*x + y*y)
    print(f"Euclidean Distance from points {x,y} & (0,0) is {dist} ")
 

if __name__=="__main__":
    try:
        x=int(input("Enter x co-ordinate: "))
        y=int(input("Enter y co-ordinate: "))        
       
        find_distance(x,y)
    except ValueError:
        print("Enter integer values")
    