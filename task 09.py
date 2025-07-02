def connect_dicts(dict1, dict2):
    sum1 = 0
    for key in dict1:
        sum1 += dict1[key]

    sum2 = 0
    for key in dict2:
        sum2 += dict2[key]

    if sum1 > sum2:
        primary = dict1
        secondary = dict2
    else:
        primary = dict2
        secondary = dict1
        
    result = {}

    keys_primary = list(primary.keys())
    for i in range(len(keys_primary)):
        key = keys_primary[i]
        value = primary[key]
        if value >= 10:
            result[key] = value

    keys_secondary = list(secondary.keys())
    for i in range(len(keys_secondary)):
        key = keys_secondary[i]
        value = secondary[key]
        if value >= 10 and key not in result:
            result[key] = value

    sorted_items = sorted(result.items(), key=lambda item: item[1])
    sorted_dict = {}
    for key, value in sorted_items:
        sorted_dict[key] = value

    return sorted_dict
print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }))
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }))
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }))