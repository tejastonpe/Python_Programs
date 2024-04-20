def harmonic_no(no):
    result=0
    for i in range(1,no+1):
        result += 1/i 
        print(result)


if __name__=="__main__":
    try:
        no=int(input("Enter no: "))
        if no <= 0:
            raise ValueError("Enter value greater than 0")
        harmonic_no(no)
    except ValueError as e:
        print(e)