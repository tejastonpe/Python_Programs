import time

def find_elapse_time(start,stop):
    seconds = stop - start
    print(f"Elapsed_time is {seconds}")
    convert_time(seconds)

def convert_time(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f"Elapsed_time in HH:MM:SS = {hours}:{minutes}:{seconds}")

def main():
    input("start the stopwatch by pressing enter:")
    start=time.time()
    input("stop the stopwatch by pressing enter:")
    stop=time.time()
    find_elapse_time(start,stop)
    

if __name__=="__main__":
    main()