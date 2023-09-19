import pandas as pd
import math
import numpy as np

# Read the csv file in
file_name = 'test.xlsx'

male = True
weight = 49

start = 0
end = 10

# Get segment position
segment_position = pd.read_excel(file_name, sheet_name='Segment Position')

pos_right_upperarm = segment_position[['Right Upper Arm x', 'Right Upper Arm y', 'Right Upper Arm z']]
pos_right_forearm = segment_position[['Right Forearm x', 'Right Forearm y', 'Right Forearm z']]
pos_right_hand = segment_position[['Right Hand x', 'Right Hand y', 'Right Hand z']]
pos_left_upperarm = segment_position[['Left Upper Arm x', 'Left Upper Arm y', 'Left Upper Arm z']]
pos_left_forearm = segment_position[['Left Forearm x', 'Left Forearm y', 'Left Forearm z']]
pos_left_hand = segment_position[['Left Hand x', 'Left Hand y', 'Left Hand z']]

# Calculate the length of the upper arm and forearm
length_right_upperarm = []
length_right_forearm = []
length_left_upperarm = []
length_left_forearm = []

for i in range(start, end):
    length_right_upperarm.append(math.sqrt((pos_right_upperarm.iloc[i, 0] - pos_right_forearm.iloc[i, 0]) ** 2 + \
                            (pos_right_upperarm.iloc[i, 1] - pos_right_forearm.iloc[i, 1]) ** 2 + \
                            (pos_right_upperarm.iloc[i, 2] - pos_right_forearm.iloc[i, 2]) ** 2))
    length_right_forearm.append(math.sqrt((pos_right_forearm.iloc[i, 0] - pos_right_hand.iloc[i, 0]) ** 2 + \
                            (pos_right_forearm.iloc[i, 1] - pos_right_hand.iloc[i, 1]) ** 2 + \
                            (pos_right_forearm.iloc[i, 2] - pos_right_hand.iloc[i, 2]) ** 2))
    length_left_upperarm.append(math.sqrt((pos_left_upperarm.iloc[i, 0] - pos_left_forearm.iloc[i, 0]) ** 2 + \
                            (pos_left_upperarm.iloc[i, 1] - pos_left_forearm.iloc[i, 1]) ** 2 + \
                            (pos_left_upperarm.iloc[i, 2] - pos_left_forearm.iloc[i, 2]) ** 2))
    length_left_forearm.append(math.sqrt((pos_left_forearm.iloc[i, 0] - pos_left_hand.iloc[i, 0]) ** 2 + \
                            (pos_left_forearm.iloc[i, 1] - pos_left_hand.iloc[i, 1]) ** 2 + \
                            (pos_left_forearm.iloc[i, 2] - pos_left_hand.iloc[i, 2]) ** 2))

length_upperarm = (sum(length_right_upperarm) + sum(length_left_upperarm)) / (2 * (end - start))
length_forearm = (sum(length_right_forearm) + sum(length_left_forearm)) / (2 * (end - start))


# Calculate the mass and moment of inertia of each segment

if male:
    mass_upperarm = -0.36785+1.15588*length_upperarm+0.02712*weight
    I_upperarm = [[-317.679+1007.85*length_upperarm+1.85249*weight, 0, 0],
                [0, -312.14+999.691*length_upperarm+1.74277*weight, 0],
                [0, 0, -11.1029+(-44.8794)*length_upperarm+0.71203*weight]]
    I_upperarm = np.divide(I_upperarm, 10000)
    
    mass_forearm = -0.43807+2.22923*length_forearm+0.01397*weight
    I_forearm = [[-145.867+562.219**length_forearm+0.85722*weight, 0, 0],
                [0, -146.449+576.691*length_forearm+0.79727*weight, 0],
                [0, 0, -13.4756+26.3785*length_forearm+0.24644*weight]]
    I_forearm = np.divide(I_forearm, 10000)
    


else:
    mass_upperarm = -0.49429+2.04431*length_upperarm+0.02414*weight
    I_upperarm = [[-243.445+888.26*length_upperarm+1.28134*weight, 0, 0],
                [0, -239.382+890.139*length_upperarm+1.13366*weight, 0],
                [0, 0, -15.0461+16.5561*length_upperarm+0.45614*weight]]
    I_upperarm = np.divide(I_upperarm, 10000)
    
    mass_forearm = -0.33838+2.42059*length_forearm+0.01079*weight
    I_forearm = [[-85.1542+387.145*length_forearm+0.53763*weight, 0, 0],
                [0, -86.1268+401.195*length_forearm+0.48729*weight, 0],
                [0, 0, -6.19627+22.5716*length_forearm+0.14122*weight]]
    I_forearm = np.divide(I_forearm, 10000)

print(mass_upperarm)
print(I_upperarm)
print(mass_forearm)
print(I_forearm)

