# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
def newtons_method(f, x0, eps=1e-6, max_iter=100, tol=1e-5):
    """The optimization function using newton's method
    f: function to optimize
    x0: starting point
    eps: epsilon
    tol: tolerance

    """

    def derivative(func, x, h=1e-5):
        return (func(x + h) - func(x)) / (h) #using definition instead of central difference

    def second_derivative(func, x, h=1e-5):
        return (derivative(func, x + h, h) - derivative(func, x)) / (2 * h) #using definition instead of central difference

    x = x0
    for i in range(max_iter):
        f_prime = derivative(f, x, h)
        f_double_prime = second_derivative(f, x, h)

        if abs(f_double_prime) < 1e-12:  # avoid division by zero
            print("Second derivative too small — stopping.")
            break

        x_new = x - f_prime / f_double_prime

        if abs(x_new - x) < tol:  # stopping criterion
            return x_new, f(x_new), i + 1

        x = x_new

    return x, f(x), max_iter
