import threading
import time


# python中GIL锁：在同一时刻，只有一个线程在运行


def task():
    time.sleep(5)


def main():
    start_time = time.time()
    thread1 = threading.Thread(target=task())
    thread2 = threading.Thread(target=task())
    thread1.start()
    thread2.start()
    # 让其他线程等待自己执行完成
    thread1.join()
    thread2.join()
    end_time = time.time()
    print(end_time - start_time)


if __name__ == '__main__':
    main()
