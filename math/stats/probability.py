def addition_rule(a, b):
    # P(a or b), where events are disjoint
    return a + b


def general_addition_rule(a, b):
    # P(A or B) = P(A) + P(B) - P(A and B)
    # e.g. P(ace or red card) = aces + red cards - (red aces)
    both = float(input('A + B = '))
    return a + b - both


def conditional(a, b):
    # P(A given B) = P(A or B) / P(B)
    disjoint = input('Are events disjoint? (y/n): ').lower()
    if disjoint == 'y':
        return addition_rule(a, b) / b
    elif disjoint == 'n':
        return general_addition_rule(a, b) / b


def general_multiplication_rule(a, b_given_a):
    # P(A and B) = P(A) * P(B given A)
    return a * b_given_a


