import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt


# Межі інтегрування:
a, b = 0, 2
num_samples = 100000


# Визначення функції для інтегрування:
def f(x):
    return x**2


# Обчислення інтеграла
result, error = spi.quad(f, a, b)

print("Інтеграл: ", result, error)


def visualize_results(x_random, y_random):
    # Створення діапазону значень для x:
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    _, ax = plt.subplots()

    ax.plot(x, y, "green", linewidth=2)
    ax.scatter(x_random, y_random, color="darkgreen")

    # Заповнення області під кривою:
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    # Налаштування графіка:
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    # Додавання меж інтегрування та назви графіка:
    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title(f"Графік інтегрування f(x) від {a} до {b}")

    plt.grid()
    plt.show()


def monte_carlo(a, b, num_samples):

    # Обчислення інтеграла методом Монте-Карло:

    x_random = np.random.uniform(a, b, num_samples)
    y_random = np.random.uniform(0, f(b), num_samples)

    # Кількість точок під кривою:
    under_curve = np.sum(y_random <= f(x_random))

    # Площа під кривою:
    area_under_curve = (under_curve / num_samples) * (b - a) * f(b)

    # Обчислення інтеграла за допомогою функції quad:
    result, error = spi.quad(f, a, b)

    print(
        "Площа обчислена методом Монте-Карло:",
        area_under_curve,
        "Площа обчислена функцією quad:",
        result,
    )
    visualize_results(x_random, y_random)


if __name__ == "__main__":
    for density in [100, 1000, 10000, 100000]:
        print(f"\n\tResults for points amount: {density}")
        monte_carlo(a, b, density)


"""
Зі збільшенням кількості випадкових точок результат роботи методу Монте-Карло стає точнішим і наближенішим до 
результатів, які дає функція quad. Це підтверджує правильність розрахунків і те, що метод працює коректно.
"""
