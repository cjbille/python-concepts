import time

def multiply_by_three(val):
    return val * 3

print(multiply_by_three(10))

def perform_op(num1: int, num2: int, op: str) -> int:
    if op == "sum" or op == "add":
        return num1 + num2
    elif op == "multiply":
        return num1 * num2
    else:
        print(f"{op} is not a valid operation")
        return 0

print(perform_op(1, 2, "multiply")) 
print(perform_op(op="sum", num2=3, num1=4)) # keyword args must come after positional args, and can be in any order
print(perform_op(5, 6, "divide"))

def exception_handling():
    start = time.time()
    try:
        answer = 2/1
        print(f"this answer is {answer}")
    except Exception as e:
        print(f"The exception type is {type(e)} and the exception message is {e}")
    finally:
        print(f"this took {time.time() - start} seconds to execute")

exception_handling()

# raise exception
def raise_error(n):
    if n == 0:
        raise Exception()
    print(n)

try:
    raise_error(0)
except Exception as e:
    print(f"an exception of type {type(e)} occurred and exception message is {e}")

# custom exception
class CustomException(Exception):
    pass

def cause_error():
    raise CustomException("Called cause_error function")

cause_error()

def many_args(*args): # can use an asterisk for 1 or more args for positional arguments (not keyword args)
    return args # this is a tuple

print(many_args(1, 2, 3))

def key_word_args(**kwargs): # use for keyword args
    return kwargs # this is a dictionary

print(key_word_args(key="val", anotherkey="anotherVal"))

lambda_func = lambda x: x * 2

print(lambda_func(3))
