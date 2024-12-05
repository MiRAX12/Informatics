import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

with open("data.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=";")
    col = ["Открытие", "Макс", "Мин", "Закрытие"]
    dates = ['24.09.2018', '24.10.2018', '26.11.2018', '03.12.2018']
    arr = [[], [], [], []]
    counter = 0
    for row in file_reader:
        if counter == 0:
            pass
        elif row[0] == '24.09.2018':
            arr[0].append([int(row[1]), int(row[2]), int(row[3]), int(row[4])])
        elif row[0] == '24.10.2018':
            arr[1].append([int(row[1]), int(row[2]), int(row[3]), int(row[4])])
        elif row[0] == '26.11.2018':
            arr[2].append([int(row[1]), int(row[2]), int(row[3]), int(row[4])])
        elif row[0] == '03.12.2018':
            arr[3].append([int(row[1]), int(row[2]), int(row[3]), int(row[4])])
        counter += 1

    plt.figure(figsize=(10, 7))
    for i in range(4):
        data = pd.DataFrame(arr[i], columns=col)
        plt.subplot(2, 2, i + 1)
        sns.boxplot(data=data, palette='husl')
        plt.title(f"Данные на {dates[i]}")
        plt.legend(col, loc='best')
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    plt.show()