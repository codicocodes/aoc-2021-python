import collections
import utils

day = "day-1"

def main():
    nums = utils.parse_ints(utils.read_input(day))
    count = -1
    prev = -1
    sliding=[]

    for num in nums:
        sliding.append(num)
        if len(sliding) == 4:
            sliding.pop(0)

        if len(sliding) == 3:
            sliding_sum = sum(sliding)
            if sliding_sum > prev:
                count+=1
            prev = sliding_sum

    print(count)
    pass

main()
