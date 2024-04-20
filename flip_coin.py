import random

def flip_coin(no_coin_fliped):
    if no_coin_fliped <=0:
        print("Enter valid no of times coin flipped")  
    
    head_count=0
    tail_count=0

    for flip in range(no_coin_fliped):
        value=random.random()
        if value < 0.5:
            tail_count +=1
        else:
            head_count +=1
    
    print(f"Percentage of Head: {(head_count/no_coin_fliped)*100} %")
    print(f"Percentage of Tail: {(tail_count/no_coin_fliped)*100} %")
    

if __name__=="__main__":
    try:
        num_flips = int(input("Enter the number of times to flip the coin: "))
        flip_coin(num_flips)
    except ValueError:
        print("Please enter a valid positive integer.")


