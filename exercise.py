import matplotlib.pyplot as plt

test_scores = [12, 99, 65, 85, 42]
test_names = ["Andy", "Martin", "Zahara", "Vuyo", "Ziyaad"]

x_pos = [i for i, _ in enumerate (test_names)]
plt.bar(x_pos, test_scores, color="purple")
plt.xticks(x_pos, test_names)
plt.show()