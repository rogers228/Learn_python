from functools import wraps

def my_decorator(param1, param2):
    """這是一個可傳入參數的裝飾器"""
    def decorator(func):
        @wraps(func)  # 保留原函式資訊，避免 Flask route 出錯
        def wrapper(*args, **kwargs):
            print(f"[裝飾器啟動] param1={param1}, param2={param2}")
            # 在執行原函式前做一些事情
            result = func(*args, **kwargs)
            # 在執行原函式後做一些事情
            print("[裝飾器結束]")
            return result
        return wrapper
    return decorator


# 使用範例
@my_decorator("A", 123)
def hello(name):
    print(f"Hello, {name}!")

hello("Rogers")
