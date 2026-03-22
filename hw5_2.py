import random
import math
import statistics

numbers = []
for i in range(100):
    numbers.append(random.randint(1, 100))

mean_val = statistics.mean(numbers)
median_val = statistics.median(numbers)
stdev_val = statistics.stdev(numbers)
sum_sqrt = math.sqrt(sum(numbers))
rounded_sqrt = round(sum_sqrt, 2)

print(f"Среднее: {mean_val:.2f}, Медиана: {median_val:.2f}, Стандартное отклонение: {stdev_val:.2f}, Корень из суммы: {rounded_sqrt:.2f}")
