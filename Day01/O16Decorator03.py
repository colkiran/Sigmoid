import time


def timeCalc(fnc):

    def helperFun(y):
        print("Executing the funtion.....")
        st = time.perf_counter()
        fnc(y)
        et = time.perf_counter()
        print("Completed executing......")
        print("-" * 60)
        print(f"The total time taken to execute the function is {round(et-st, 2)}")

    return helperFun


@timeCalc
def fun(x):
    lst = []
    for i in range(1, x+1):
        for j in range(1, i+1):
            lst.append(j ** 3)


fun(8500)
