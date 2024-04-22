def triplates(num):
    triplates_count=0
    triplates=[]
    n=len(num)

    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if num[i] + num[j] + num[k] == 0:
                    result= (num[i],num[j],num[k])
                    if result not in triplates:
                        triplates.append(result)
                        triplates_count+=1
    print(f"total riplates count is {triplates_count} & they are {triplates}")    

def main():
    try:
        total_int=list(map(int,input("Enter integers values seperated by space:").split()))
        if len(total_int) < 3:
            raise ValueError("Enter at least three integers")
        triplates(total_int)
    except ValueError as e:
        print(e)


if __name__=="__main__":
    main()
