def power_of_2(no):
    for i in range(no+1):
        result= 2 ** i
        print(f"2^{i} = {result}")  


if __name__=="__main__":
    try:
        no=int(input("Enter power value till you want to find power of 2: "))
        if  not 0 <= no < 31:
            raise ValueError("Enter power in range between 0 ro 30")
        power_of_2(no)
    except ValueError as e:
        print(e)
