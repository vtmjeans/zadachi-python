def max_odd(array):
    max_val = None
    for item in array:
        if isinstance(item, (int, float)) and item == int(item):
            num = int(item)
            if num % 2 == 1:
                if max_val is None or num > max_val:
                    max_val = num
    return max_val
print(max_odd([1, 2, 3, 4, 5]))                 
print(max_odd([21.0, 22.5, 23.7, 25]))          
print(max_odd([2, 4, 6, 8]))                    
print(max_odd(["a", {}, [2, 4], 15.0]))         
print(max_odd([10.0, 21.0, 22, 23.5, 25.0]))    
print(max_odd([2.2, 4.4, 6.6, 8.8]))            