import numpy
from scipy import stats

test_scores = [12, 99, 86, 87, 88, 45, 87, 94, 78, 77, 85, 86, 85]
my_mode = stats.mode(test_scores)
my_range = numpy.ptp(test_scores)
my_stdn = numpy.std(test_scores)
print("The mode is:", my_mode)
print("The range is:", my_range)
print("The standard deviation is:", my_stdn)

