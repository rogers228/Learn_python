# 數學表達式
## 貼上 https://stackedit.io/app# 就可產生 數學式

from sympy import (symbols,  latex,
    sqrt, sin, limit)

def test1():
    x = symbols('x') # 定義一個符號變數 x，可以用來建立代數運算式。
    expr = sqrt(x) + x**2 + 1/x
    # expr = x**2 + 2*x + 1
    latex_expr = latex(expr) # 定義一個符號變數 x，可以用來建立代數運算式。
    print(f"$${latex_expr}$$")

def test2():
    x, a = symbols('x a')
    f = sin(x)/x
    lim_expr = limit(f, x, a)

    latex_code = latex(limit(f, x, a)) + " = " + latex(lim_expr)
    print(f"$$\n{latex_code}\n$$")

if __name__ == '__main__':
    test2()