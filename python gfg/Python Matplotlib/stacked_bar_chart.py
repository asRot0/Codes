import matplotlib.pyplot as plt

labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
index = (1, 2, 3, 4, 5)
web_usage = [20, 2, 5, 10, 14]
data_science_usage = [15, 8, 5, 15, 2]
games_usage = [10, 1, 5, 5, 4]

plt.bar(index, web_usage, tick_label=labels, label='web')
plt.bar(index, data_science_usage, tick_label=labels, label='data science',
        bottom=web_usage)
web_data_science_usage = [web_usage[i]+data_science_usage[i]
                          for i in range(len(web_usage))]
plt.bar(index, games_usage, tick_label=labels, label='games',
        bottom=web_data_science_usage)

plt.ylabel('usage')
plt.xlabel('programming languages')
plt.legend()
plt.show()