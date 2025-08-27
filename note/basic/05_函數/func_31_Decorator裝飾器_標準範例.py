def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("裝飾器：在執行原函式之前")

        # 執行原函式，並接收回傳值
        result = func(*args, **kwargs)

        print("裝飾器：在執行原函式之後")

        return result  # 不可缺少，否則原函式的結果會消失

    wrapper.__name__ = func.__name__  # 保留原函式名稱 (Flask 等框架需要)
    return wrapper


# --- 測試用原始函式 ---
@my_decorator
def hello(name):
    print(f"Hello, {name}!")
    return f"Greeting sent to {name}"


# --- 呼叫 ---
print(hello("Alice"))
