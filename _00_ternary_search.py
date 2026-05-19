def ternary_search(F, a, b, eps=1e-9):
    """Find x in [a, b] that minimizes unimodal function F."""
    while b - a > eps:
        m1 = a + (b - a) / 3
        m2 = b - (b - a) / 3
        if F(m1) < F(m2):
            b = m2
        else:
            a = m1
    return (a + b) / 2
 
 
# --- Quick tests ---
if __name__ == "__main__":
    import math
 
    tests = [
        ("x^2",           lambda x: x**2,                    -10, 10,  0.0),
        ("(x-3)^2 + 1",   lambda x: (x-3)**2 + 1,            -5, 12,  3.0),
    ]
 
    for name, fn, a, b, true_x in tests:
        x = ternary_search(fn, a, b)
        print(f"F = {name:20s}  x* = {x:.10f}  F(x*) = {fn(x):.10f}  err = {abs(x - true_x):.2e}")