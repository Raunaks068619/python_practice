import sys
nums = sys.argv
def with_loop():
    total = 0 
    count = 1
    for i in range(10):
        num = int(input("{}.Enter number: ".format(count)))
        if num > 1:
            for j in range(2, num):
                if (num % j) == 0:
                    break
            else:
                total += num
        elif num == 1: 
            total += num
        else: 
            pass
        count += 1
    print("\nTotal : {}".format(total))
def with_argv(nums):
    total = 0 
    count = 1
    for i in range(1, len(nums)):
        if int(nums[i]) > 1: 
            for j in range(2, int(nums[i])):
                if (int(nums[i]) % j) == 0:
                    break
            else:
                total += int(nums[i])
        elif int(nums[i]) == 1: 
            total += int(nums[i])
        else: 
            pass
        count += 1
    print("\nTotal : {}".format(total))


with_loop()
with_argv(nums)
