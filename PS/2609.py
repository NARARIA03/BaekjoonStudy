def gcd(A, B):

    remain = A % B
    if remain == 0:
        return B
    else:
        return gcd(B, remain)


def lcm(A, B, gcd):
    return (A * B) / gcd


A, B = map(int, input().split())

if A > B:
    gcd_value = gcd(A, B)
else:
    gcd_value = gcd(B, A)
lcm_value = lcm(A, B, gcd_value)
print(gcd_value)
print(round(lcm_value))
