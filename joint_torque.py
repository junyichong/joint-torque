import pandas as pd
import math

# Read the csv file in
file_name = 'test.xlsx'

start = 0
end = 10

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
    
print(length_left_upperarm)
print(length_left_forearm)





