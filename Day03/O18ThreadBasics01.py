import time

def fun(x):
    print("Function is going to sleep....")
    time.sleep(x)
    print("Function fun just woke up.....")

print("Calling function.....")
st = time.perf_counter()
fun(2)
fun(2)
fun(2)
et = time.perf_counter()

print("Funtion call completed.....")

print(f"The total time taken to execute the function :{et - st}")
