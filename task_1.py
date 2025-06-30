import pulp

# Ініціалізація моделі:
model = pulp.LpProblem("Maximize Drink Production", pulp.LpMaximize)

# Кількість виробленого лимонаду і фруктового соку:
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

# Обмеження ресурсів:
model += 2 * lemonade + 1 * fruit_juice <= 100, "Вода"
model += 1 * lemonade <= 50, "Цукор"
model += 1 * lemonade <= 30, "Лимонний_сік"
model += 2 * fruit_juice <= 40, "Фруктове_пюре"

# Максимізуємо загальну кількість напоїв:
model += lemonade + fruit_juice, "Загальна_кількість_напоїв"

# Рішення:
model.solve()

print("Кількість Лимонаду для виробництва:", lemonade.varValue)
print("Кількість Фруктового соку для виробництва:", fruit_juice.varValue)
print("Загальна кількість напоїв:", lemonade.varValue + fruit_juice.varValue)
