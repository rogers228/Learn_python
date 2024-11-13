from sympy import symbols, sqrt, latex

x = symbols('x')
# expr = sqrt(x) + x**2 + 1/x
expr = x**2 + 2*x + 1
latex_expr = latex(expr)
print(f"$$\n{latex_expr}\n$$")

## 貼上 https://stackedit.io/app# 就可產生 數學式