import time
from functools import wraps

def cached(max_size=None, seconds=None):
    if not isinstance(max_size, int):
        max_size = None

    if not isinstance(seconds, int):
        seconds = None

    def decorator(func):
        cache = {}  
        order = []  

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal cache, order

            key = (args, frozenset(kwargs.items()))

            current_time = time.time()

            if seconds is not None:
                for k in list(cache.keys()):
                    stored_time, _ = cache[k]
                    if current_time - stored_time > seconds:
                        del cache[k]
                        if k in order:
                            order.remove(k)
            if key in cache:
                if key in order:
                    order.remove(key)
                order.append(key)
                return cache[key][1]  

            result = func(*args, **kwargs)

            if max_size is not None:
                while len(cache) >= max_size:
                    lru_key = order.pop(0)  
                    del cache[lru_key]
            cache[key] = (current_time, result)
            order.append(key)

            return result

        return wrapper

    return decorator

@cached(max_size=3, seconds=2)
def slow_function(x):
    print(f"Вычисляю для {x}...")
    return x ** 2

print("=== Первый вызов: вычисление ===")
print(slow_function(2))  # Вычисляется

print("\n=== Второй вызов: берётся из кэша ===")
print(slow_function(2))  # Из кэша

print("\n=== Третий вызов: после истечения времени ===")
time.sleep(2)  # ждём больше 2 секунд
print(slow_function(2))  # Снова вычисляется
print("\n=== Четвёртый вызов с другим аргументом ===")
print(slow_function(3))  # Новое вычисление

print("\n=== Пятый вызов: снова для 2, должно быть в кэше ===")
print(slow_function(2))  # Должно быть в кэше, если не прошло 2 секунд

print("\n=== Шестой вызов: переполнение кэша ===")
print(slow_function(4))  # Теперь кэш полон
print(slow_function(5))
print(slow_function(6))  # При max_size=3 — первые записи начнут удаляться
print(slow_function(2))  # Запись может уже не быть в кэше