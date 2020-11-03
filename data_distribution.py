import matplotlib.pyplot as plt

girls_ages = [19, 24, 19, 17]
girls_names = ["Skylar", "Nadine", "Zoe", "Lelethu"]
x_pos = [i for i, _ in enumerate (girls_names)]
plt.bar(x_pos, girls_ages, color="red")
plt.xticks(x_pos, girls_names)
plt.show()