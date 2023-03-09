# import time
#
#
# def decorate_me(func):
#     def inner_func(*args, **kwargs):
#         print("It is a decorated function")
#         return func(*args, **kwargs)
#     return inner_func
#
#
# @decorate_me
# def addition(a, b, c):
#     return a + b + c
#
#
# # addition = decorate_me(addition)
#
# # start = time.time()
# print(addition(3, 4, 1))
# # end = time.time()
# # print(f"Total function execution time is {end-start}")
import time


def execution_time(func):
    def inner_func(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(f"The function execution time is {end-start}")
        return r
    return inner_func


@execution_time
def message_print():
    time.sleep(5)
    # for i in range(1000000000):
    #     pass
    print("Hello World")


# message_print = execution_time(message_print)
message_print()
