import time

for i in range(101):
    print("\r{:20d}%".format(i),end=' ')
    time.sleep(0.05)