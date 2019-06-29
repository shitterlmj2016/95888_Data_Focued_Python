import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

data = [
    {'x': [10, 20, 30],
     'y': [3, 4, 5],
     'horizontal': True},
    {'x': [10, 20, 30],
     'y': [1, 2, 3],
     'horizontal': True}
]

# alternatively


figure, axes = plt.subplots(1, 2, figsize=(10, 5), sharey=True)
male = axes[0]
female = axes[1]

plt.suptitle("Patient Age by Gender")

male.barh(data[0]['x'], data[0]['y'], color="darkblue")
male.invert_xaxis()
male.set_xlabel("Count")
male.set_title("Male")
male.yaxis.tick_right()
male.set_xticks([x for x in range(0, 6)])

# male.xaxis.set_major_locator(MultipleLocator(10))
female.barh(data[1]['x'], data[1]['y'], color="darkred")
female.set_title("Female")
female.set_xlabel("Count")
female.xaxis.set_major_locator(MaxNLocator(integer=True))
female.set_xticks([x for x in range(0, 6)])
# Show the plot

plt.show()
