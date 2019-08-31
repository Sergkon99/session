import matplotlib.pyplot as plt
# x[n+1] = 4x[n](1-x[n]) x[0] = 1/3
# y[n+1] = 4y[n]-4y^2[n] y[0] = 1/3
# |y[n] - x[n]| = ?


def series_x(n: int) -> list:
    x = [0] * n
    x[0] = 1/3
    for i in range(n-1):
        x[i+1] = 4*x[i]*(1 - x[i])
    return x


def series_y(n: int) -> list:
    y = [0] * n
    y[0] = 1/3
    for i in range(n-1):
        y[i+1] = 4*y[i] - 4*y[i]**2
    return y


def abs_diff(x: list, y: list) -> list:
    n = len(x)
    return [abs(x[i] - y[i]) for i in range(n)]

n = 500
x = series_x(n)
y = series_y(n)
diff = abs_diff(x, y)

plt.title('Абсолютная разность двух рядов')
plt.xlabel('Порядковый номер')
plt.ylabel('Разность')
plt.xlim(0, n)
plt.ylim(0, 1)
plt.scatter(range(n), diff, s=1)
plt.show()
