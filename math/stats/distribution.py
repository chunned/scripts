from factorial import factorial
from math import e


def n_choose_k(n, k, repetition):       # calculates C(n,k)
    if repetition == 'n':
        return factorial(n)/(factorial(k)*factorial(n-k))
    elif repetition == 'y':
        return factorial(n + k - 1) / (factorial(k) * factorial(n - 1))


def binomial(n, k, p):
    # Calculates binomial distribution
    # n = number of trials, k = number of successes, p = probability of a single success
    choose = n_choose_k(n, k, 'n')
    probability = (p**k)*(1-p)**(n-k)
    return choose*probability


def binomial_fewer_than(n, k, p):
    # Calculates the probability of k or fewer successes
    total = 0
    for i in range(0, k+1):
        total += binomial(n, i, p)
    return total


def negative_binomial(n, k, p):
    # describes the probability of observing the kth success on the nth trial, where trials are independent
    return n_choose_k(n - 1, k - 1, 'n') * p ** k * (1 - p) ** (n - k)


def z_score(value, mean, standard_deviation):
    return (value - mean) / standard_deviation


def geometric_probability(p, n):
    # p = probability of single success
    # n = number of trials
    # probability of finding the first success in the nth trial:
    return (1 - p)**(n - 1) * p


def geometric_variance(p):
    return (1 - p) / p ** 2


def poisson(rate, k):
    # rate = average rate over a period of time
    # k = number of events
    return (rate ** k * e ** (rate * -1))/factorial(k)


def hypergeometric(population, success_states,
                   draws, observed_successes):
    return (n_choose_k(success_states, observed_successes, 'n') * n_choose_k(
        population - success_states, draws - observed_successes, 'n')) / n_choose_k(population, draws, 'n')


