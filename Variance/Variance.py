import os
from statistics import mean, stdev
os.system("cls")

i = 1
while i < 6:
    print(f"Grill {i}:")
    num = [int(line) for line in open(f"Grill_{i}.txt", "r")]
    min_num, max_num, mean_num, stdev_num = min(num), max(num), mean(num), stdev(num)

    #high: 358
    #low: 342

    print("Min: ", min_num)
    print("Max: ", max_num)
    print("Mean:", mean_num)
    print("Standard Deviation of temps is: ", stdev_num)

    if min_num <= 342 and max_num >= 358:
        print('''Too Hot and Too Cold: Fail!
        ''')
    elif min_num <= 342:
        print('''Too Cold: Fail!
        ''')
    elif max_num >= 358:
        print('''Too Hot: Fail!
        ''')
    else:
        print('''Pass!
        ''')
    i += 1