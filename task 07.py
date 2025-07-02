def combine_anagrams(words_array):
    groups = []

    for word in words_array:
        key = ''.join(sorted(word.lower())) 
        found = False
        
        for group in groups:
            if ''.join(sorted(group[0].lower())) == key:
                group.append(word)
                found = True
                break
        if not found:
            groups.append([word])
    return groups
print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
"creams", "scream"]))