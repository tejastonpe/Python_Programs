def user_input():
    name = str(input("Enter your name: "))
    if len(name) < 3:
        print("Enter valid name hanving three characters")
    else:
        print(f"Hello {name}, How are you?")
        
    
if __name__=="__main__":
    user_input()