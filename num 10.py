import numpy as np
import matplotlib.pyplot as plt

# Константы
epsilon_0 = 8.854187817e-12
k_e = 1 / (4 * np.pi * epsilon_0)

# Параметры моделирования
x_min, x_max = -10, 10
y_min, y_max = -10, 10
n_points = 50

# Создаем сетку
x = np.linspace(x_min, x_max, n_points)
y = np.linspace(y_min, y_max, n_points)
X, Y = np.meshgrid(x, y)

# Система зарядов
charges = [
    {'q': 1e-9, 'x': 2, 'y': 3},
    {'q': -1e-9, 'x': -2, 'y': -3},
    {'q': 2e-9, 'x': 0, 'y': 0}
]

# Вычисление электростатического поля
Ex = np.zeros_like(X)
Ey = np.zeros_like(Y)

for charge in charges:
    q = charge['q']
    x0 = charge['x']
    y0 = charge['y']

    r = np.sqrt((X - x0) ** 2 + (Y - y0) ** 2)
    Ex += k_e * q * (X - x0) / r ** 3
    Ey += k_e * q * (Y - y0) / r ** 3

# Нормализация поля для лучшей визуализации
E_norm = np.sqrt(Ex ** 2 + Ey ** 2)
Ex_norm = Ex / E_norm
Ey_norm = Ey / E_norm

# Визуализация электростатического поля
plt.figure(figsize=(10, 8))
plt.quiver(X, Y, Ex_norm, Ey_norm, E_norm, cmap='viridis', scale=20, headwidth=4, headlength=5)

# Визуализация зарядов
for charge in charges:
    if charge['q'] > 0:
        plt.plot(charge['x'], charge['y'], 'ro', markersize=12, markeredgecolor='black', markeredgewidth=1.5)
    else:
        plt.plot(charge['x'], charge['y'], 'bo', markersize=12, markeredgecolor='black', markeredgewidth=1.5)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Электростатическое поле системы неподвижных точечных зарядов')
plt.grid(True)
plt.colorbar(label='Величина поля')
plt.show()