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
def f(x):
    return x ^ 3 - 3 * x ^ 2 + 4 * x


# %%
x0 = 10

# %%
result = f(x0)
print(result)


# %%
def first_derivative(x):
    return 3 * x ^ 2 - 6 * x + 4


def second_derivative(x):
    return 6 * x - 6


# %%
x1 = x0 - first_derivative(x0) / second_derivative(x0)
print(x1)

# %%
i = 0
while True:
    print(i, end=" ")
    i = i + 1

# %%
