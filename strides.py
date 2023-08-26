# "We are determining which runners ran the least and most strides in a 5 mile run and the difference in strides between those two runners"

import math
runners = {'John': [7, 2], 'Will': [7, 5], 'Max': [7, 9], 'Lisa': [6, 10], 'Luke': [7, 6], 'Marry': [7, 8]}
max_stride = 0
min_stride = 500
for i in runners:
    convert_to_inches = runners[i][0]*12 + runners[i][1]
    if convert_to_inches > max_stride:
        max_stride = convert_to_inches
        max_key = max(runners, key=runners.get)
    if convert_to_inches < min_stride:
        min_stride = convert_to_inches
        min_key = min(runners, key=runners.get)
    print(i + "'s", 'stride is', runners[i][0], 'feet', runners[i][1], 'inches long or', convert_to_inches, 'inches long.')  
print('\nThe runner with the largest strides is', max_key, 'at', max_stride, "inches long.")
print('The runner with the smallest strides is', min_key, 'at', min_stride, "inches long.\n")
print(max_key, 'ran', math.ceil(max_stride * 5280 * 5), 'strides in a 5 mile run.')
print(min_key, 'ran', math.ceil(min_stride * 5280 * 5), 'strides in a 5 mile run.')
difference = math.ceil(max_stride * 5280 * 5) - math.ceil(min_stride * 5280 * 5)
print('\nThe stride difference between', max_key, 'and', min_key, 'is', difference, 'strides.')