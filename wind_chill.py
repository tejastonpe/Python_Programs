import math

def show_wind_chill(t,v):
    try:
        if (t > 50) or (v > 120 or v < 3):
            raise("Can't find wind chill at these range of values")
        else:
            w= 35.74 + 0.6215*t + (0.4275*t - 35.75)*math.pow(v,0.16)
            print(f"wind chill is {w}")
    except ValueError as e:
        print(e) 

def main():
    try:
        temperature=float(input("Enter temperature in fahrenheit: "))
        wind_speed=float(input("Enter wind speed: "))        
        show_wind_chill(temperature,wind_speed)        
    except ValueError:
        print("Enter integer values")
 

if __name__=="__main__":
    main()
    
    