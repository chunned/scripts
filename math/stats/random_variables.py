# 'values' in all functions should be a list of tuples
# each tuple should be of the format (outcome, probability of this outcome)
def expected_value(values):
    ex = 0
    for i in values:
        ex += i[0] * i[1]
    return ex


def general_variance(x):
    variance = 0
    for i in x:
        variance += (i[0] - expected_value(x))**2 * i[1]
    return variance

