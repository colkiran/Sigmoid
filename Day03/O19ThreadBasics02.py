
import threading
import time

def doJob():
    print(f"Going to sleep for 2 secs......{threading.current_thread().name}")
    time.sleep(2)
    print(f"Just woke up from sleep......{threading.current_thread().name}")

st = time.perf_counter()

thrd1 = threading.Thread(target=doJob, name="th1")
thrd2 = threading.Thread(target=doJob, name="th2")
thrd3 = threading.Thread(target=doJob, name="th3")
thrd4 = threading.Thread(target=doJob, name="th4")
thrd5 = threading.Thread(target=doJob, name="th5")
thrd6 = threading.Thread(target=doJob, name="th6")



thrd1.start()
thrd2.start()
thrd3.start()
thrd4.start()
thrd5.start()
thrd6.start()

thrd1.join()
thrd2.join()
thrd3.join()
thrd4.join()
thrd5.join()
thrd6.join()

et = time.perf_counter()
print(f"The total time taken to execute the task :{et - st}")
