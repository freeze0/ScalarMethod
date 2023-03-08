#первая матрица нарушает условие
#вторая работает
#третья с отрицательным лямбда

def dot_product(x, y):
    return sum([x[i] * y[i] for i in range(len(x))])

def norm(x):
    return sum([x[i]**2 for i in range(len(x))])**0.5

def power_iteration_method(A, x0, e, lambda0):
    # Step 1
    n, m = len(A), len(A[0])
    k = 1
    x = x0.copy()
    lambda_prev = lambda0

    while True:
        # Step 2
        s0 = dot_product(x, x)
        norm_x = norm(x)
        x = [x[i] / norm_x for i in range(m)]

        # Step 3
        y = [0] * m
        for i in range(n):
            for j in range(m):
                y[i] += A[i][j] * x[j]

        # Step 4
        sk = dot_product(y, y)
        tk = dot_product(y, x)
        norm_y = norm(y)
        x = [y[i] / norm_y for i in range(m)]
        lambda_curr = sk / tk

        # Step 5
        if abs(lambda_curr - lambda_prev) > e:
            lambda_prev = lambda_curr
            k += 1
        else:
            return lambda_curr, x

with open('matrix1.txt', 'r') as f:
    matrix_data = [[float(num) for num in line.split(',')] for line in f.readlines()]
A = matrix_data

# Input initial vector x0, tolerance e, and initial approximation lambda0
x0 = [1.0] * len(A[0])
e = 1e-6
lambda0 = 0.0

# Compute dominant eigenvalue and eigenvector
lambda1, x1 = power_iteration_method(A, x0, e, lambda0)

# Output results
print(f"Dominant eigenvalue: {lambda1}")
print(x1)
otveti = open('otvet.txt', 'w')
otveti.write(f"Dominant eigenvalue: {lambda1}")
otveti.write('\n')
otveti.write(str(x1))
