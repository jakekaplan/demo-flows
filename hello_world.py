import os

def hello_world():
    print("hi from a branch!")
    for key, value in os.environ.items():
        print(f"{key}: {value}")
