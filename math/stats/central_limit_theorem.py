def central_limit_theorem():
    # returns standard error
    n = int(input("Sample size: "))
    p = float(input("Probability: "))
    if (n * p >= 10) and (n * (1 - p) >= 10):
        return ((p * (1 - p)) / n) ** (1 / 2)
    else:
        print('Success-failure condition failed')

