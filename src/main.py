import threading
from function1 import func1
from function2 import func2

def run_in_threads():
    t1 = threading.Thread(target=lambda: print(func1()))
    t2 = threading.Thread(target=lambda: print(func2()))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    run_in_threads()