import numpy

test_scores = [99, 10, 55, 69, 70, 89, 90, 92, 93, 88]
my_mean = numpy.mean(test_scores)
my_median = numpy.median(test_scores)
print("The mean is:", my_mean)
print("The median is:", my_median)

test_scores = [67, 76, 86, 58, 61]
my_mean = numpy.mean(test_scores)
my_median = numpy.median(test_scores)
y = numpy.percentile(test_scores, 75)
x = numpy.var(test_scores)
print("The mean is:", my_mean)
print("The median is:", my_median)
print("The 75% percentile for the marks is", y)
print("The variance is:", x)
