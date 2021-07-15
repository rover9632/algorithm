
def pow(a, n: int):
    ret = 1
    while n:
        if n % 2 == 1:
            ret *= a
        a *= a
        n //= 2
    return ret


def gcd(a: int, b: int) -> int:
    """compute the greatest common divisor
    """
    while b:
        r = a % b
        a = b
        b = r
    return a
