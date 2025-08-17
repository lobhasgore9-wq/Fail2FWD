s = input("Enter a string: ")
longest = 0

for i in range(len(s)):
    sub = ""
    for j in range(i, len(s)):
        if s[j] in sub:
            break
        sub += s[j]
        longest = max(longest, len(sub))

print(longest)