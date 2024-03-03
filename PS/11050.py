def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def binomial(n, k):
    return round(factorial(n) / (factorial(k) * factorial(n - k)))


N, K = map(int, input().split())
print(binomial(N, K))
