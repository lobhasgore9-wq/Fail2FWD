def group_anagrams(words):
    groups = {}
    for word in words:
        key = ''.join(sorted(word))
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]
    return list(groups.values())

u_input=input("enter the words")
items=u_input.split()
print(group_anagrams(items))
"""anagram-aise words jinke leeters ko rearrange karke new words bana sakte he"""