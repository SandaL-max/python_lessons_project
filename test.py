import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_csv("Students_Performance.csv")

bins = np.linspace(20, 100, 40)

plt.hist(
    [students["math score"], students["reading score"], students["writing score"]],
    bins,
    label=["Тест по математике", "Тест по чтению", "Тест по правописанию"],
)
plt.xlabel("Баллы за тест")
plt.ylabel("Количество студентов")
plt.legend()
plt.show()
