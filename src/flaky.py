import random

def flaky_operation():
    if random.random() < 0.7:
        raise Exception("Random failure")
    print("✅ Success")
