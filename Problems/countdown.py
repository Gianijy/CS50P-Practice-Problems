import time

start = int(input("Starting number: "))
print(f"\n{start}")

while start > 0:
    time.sleep(1)
    start -= 1
    print(start)
    if start == 1:
        break

time.sleep(1)
print("\nLift off!🚀")
