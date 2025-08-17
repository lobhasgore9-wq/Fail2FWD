nums = input("Enter numbers (space separated): ").split()
nums_int = []
for x in nums:
    nums_int.append(int(x))
nums_set = set(nums_int)
longest = 0
for num in nums_int:
    if num - 1 not in nums_set:
        length = 1
        while num + length in nums_set:   
            length += 1
        longest = max(longest, length)    
print("Longest consecutive sequence length:", longest)


