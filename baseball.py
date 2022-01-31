import random

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# add some random data to baseball
for x in range(1100):
    another_player = [random.randint(170, 220),
                      random.randint(70, 110) + random.randint(0, 99)/100]
    baseball.append(another_player)

# import numpy package
import numpy as np

# create np_baseball (2 cols)
np_baseball = np.array(baseball)

# print out the 50th row of np_baseball
print(np_baseball[49,:])

# select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]

# print out the height of the 124th player
print(np_baseball[123, 0])




