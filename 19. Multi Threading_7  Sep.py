


"""Multithreading"""

"""
Q. When we use our machine, a lot of different processes are being executed on it. Are all these
processes running on the CPU at the same time or is one process running at a time?

A. The CPU executes only one process at a time.
Even though one process is executed by the CPU at a time, even then we do not feel so. We feel
that all the processes are working at the same time

This is because our systems have the capability to perform multiple tasks at the same time, i.e.,
our machine can perform multitasking

Q. What enables multitasking in the machines?
A. Operating System.

OSs enable the machine to perform multitasking

The multitasking systems are of two different types:

1. Multiprocessing systems: They are used in big standalone applications where the resources of 
one application cannot be used by another application

2. Multi threading systems: They are used in small applications where the resources of one 
application can be used by another application


Q. How does OS help us to perform multitasking?
A. When there are multiple tasks to be performed at the same time, then the OS provides the 
CPU to each and every task one-by-one and during that time, the CPU is completely dedicated for
that single task. After sometime, the OS switches the program and provides the CPU to another 
program.

This switching between different programs is done at such a high speed that it gives us the 
impression that all of the tasks are being performed at the same time
"""

# # New Program
#
# def func1():
#     for i in range(100):
#         print("This is func1", i)
#
# def func2():
#     for i in range(100):
#         print("This is func2", i)
#
# func1()
# func2()


# # New Program
# import threading
#
# def func1():
#     for i in range(100):
#         print("This is func1", i)
#
# def func2():
#     for i in range(100):
#         print("This is func2", i)
#
# th1 = threading.Thread(target = func1)
# th2 = threading.Thread(target = func2)
#
# th1.start()
# th2.start()


# # New Program
# import threading
#
# def func1():
#     for i in range(100):
#         print(threading.current_thread().getName(), i)
#
# th1 = threading.Thread(target = func1)
# th2 = threading.Thread(target = func1)
#
# th1.setName("Thread 1")
# th2.setName("Thread 2")
#
#
# th1.start()
# th2.start()


# # New Program
# import threading
#
# def func1():
#     for i in range(100):
#         print("This is func1", i)
#
# def func2():
#     for i in range(100):
#         print("This is func2", i)
#
# th1 = threading.Thread(target = func1)
# th2 = threading.Thread(target = func2)
#
# th1.setDaemon(True)
# th2.setDaemon(True)
#
# th1.start()
# th2.start()
#
#
# for i in range(15):
#     print(threading.current_thread().getName(), i)


# # New Program
# import threading
# def func1():
#     global x
#     for i in range(100000):
#         x+=1
#
# def func2():
#     global y
#     for i in range(100000):
#         y+=1
#
# x, y = 0, 0
# th1 = threading.Thread(target = func1)
# th2 = threading.Thread(target = func2)
#
# th1.start()
# th2.start()
 #
# print(x, y)

"""
Q. How many types of memories are there in our machine?
A. There are 3 types of memories in the machine, they are:

1. cache memory: The data / variables which are very frequently accesses by the programs are 
stored in the cache memory

2. RAM memory
3. ROM memory


CPU ---> cache      :   fastest
CPU ---> RAM        :   slower
CPU ---> ROM        :   even slower
CPU ---> Hardware   :   slowest
"""

# # New Program
# import threading
# def func1():
#     global x
#     for i in range(100000):
#         x+=1
#
# def func2():
#     global y
#     for i in range(100000):
#         y+=1
#
# x, y = 0, 0
# th1 = threading.Thread(target = func1)
# th2 = threading.Thread(target = func2)
#
# th1.start()
# th2.start()
#
# while th1.is_alive() == True or th2.is_alive() == True: pass
#
# print(x, y)


# # New Program
# import threading
# def func1():
#     global x
#     for i in range(100000):
#         x+=1
#
# def func2():
#     global y
#     for i in range(100000):
#         y+=1
#
# x, y = 0, 0
# th1 = threading.Thread(target = func1)
# th2 = threading.Thread(target = func2)
#
# th1.start()
# th2.start()
#
# th1.join()
# th2.join()
#
# print(x, y)


# # New Program
# import threading
# def func1():
#     global x
#     for i in range(100000):
#         x+=1
#
# x = 0
# th1 = threading.Thread(target = func1)
# th2 = threading.Thread(target = func1)
#
# th1.start()
# th2.start()
#
# th1.join()
# th2.join()
#
# print(x)

"""
race condition: Race condition occurs when 2 or more threads access the same variable at the 
same time

To avoid the race condition we have to create an object of the Lock class

"""

# New Program
import threading
lock = threading.Lock()

def func1():
    global x
    for i in range(100000):
        lock.acquire()
        x+=1
        lock.release()

x = 0
th1 = threading.Thread(target = func1)
th2 = threading.Thread(target = func1)

th1.start()
th2.start()

th1.join()
th2.join()

print(x)








