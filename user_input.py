def User_Input():
    name = str(input("Enter your name: "))
    if len(name) < 3:
        print("Enter valid name hanving more than three characters")
    else:
        print(f"Hello {name}, How are you?")
    



if __name__=="__main__":
    User_Input()