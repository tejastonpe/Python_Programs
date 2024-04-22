import random

def coupon_numbers(no):
    coupons = set()
    total_random_no = 0

    while len(coupons) < no:
        random_number = random.randint(1, no)
        total_random_no += 1
        coupons.add(random_number)
        print(coupons)
        
    print(f"Total random numbers required: {total_random_no}")

def main():
    coupon_no=int(input("Enter number of coupons you want to create?"))
    coupon_numbers(coupon_no)


if __name__=="__main__":
    main()
