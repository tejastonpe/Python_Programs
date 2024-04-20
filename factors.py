def factors(no):
    num=2
    while (num*num<=no):
        while(no>1):
            while no%num==0:
                print(num)
                no=no/num
            num+=1


if __name__=="__main__":
    try:
        no=int(input("Enter no: "))
        if no <=0:
            raise ValueError("Enter value greater than 0")
        factors(no)
    except ValueError as e:
        print(e)
        
   

