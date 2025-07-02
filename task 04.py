def sort_list(lst):
    if not lst:
        return []

    min_val = min(lst)
    max_val = max(lst)

    new_lst = []
    for num in lst:
        if num == min_val:
            new_lst.append(max_val)
        elif num == max_val:
            new_lst.append(min_val)
        else:
            new_lst.append(num)

    new_lst.append(min_val)
    return new_lst
print(sort_list([]))                
print(sort_list([2, 4, 6, 8]))        
print(sort_list([1]))                
print(sort_list([1, 2, 1, 3]))