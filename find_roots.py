import math

def find_roots(a,b,c):
    delta = (b*b - 4*a*c)
    root1 = (-b + math.sqrt(delta)) / (2*a)
    root2 = (-b - math.sqrt(delta)) / (2*a)

    print(f"Roots of the equation are {root1} & {root2}")   

def main():
    try:
        a=int(input("Enter value of a: "))
        b=int(input("Enter value of b: "))    
        c=int(input("Enter value of c: "))    
       
        find_roots(a,b,c) 
    except ValueError:
        print("Enter integer values")
 

if __name__=="__main__":
    main()
    
    