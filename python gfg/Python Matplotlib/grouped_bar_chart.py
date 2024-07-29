import matplotlib.pyplot as plt

BAR_WIDTH = 0.35

teama_results = (60, 75, 56, 62, 58)
teamb_results = (55, 68, 80, 73, 55)

index_teama = (1, 2, 3, 4, 5)
index_teamb = [i + BAR_WIDTH for i in index_teama]

ticks = [i + BAR_WIDTH / 2 for i in index_teama]
tick_labels = ('Lab 1', 'Lab 2', 'Lab 3', 'Lab 4', 'Lab 5')

plt.bar(index_teama, teama_results, BAR_WIDTH, color='b', label='Team A')
plt.bar(index_teamb, teamb_results, BAR_WIDTH, color='g', label='Team B')

plt.xlabel('Labs')
plt.ylabel('Scores')
plt.title('Scores by Lab')
plt.xticks(ticks, tick_labels)
plt.legend()
plt.show()