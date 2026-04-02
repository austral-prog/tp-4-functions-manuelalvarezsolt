
from uaclient.security_status import get_livepatch_fixed_cves


def roots(a, b, c):
    val1 = (b * b)
    sinraiz = (val1 - 4 * a * c)
    if sinraiz >= 0:
        val2 = sinraiz ** 0.5
        val3 = (-b + val2)
        val4 = (-b - val2)
        divisor = (2 * a)
        raiz1 = val3 / divisor
        raiz2 = val4 / divisor
        if raiz1 == raiz2:
            return(f"({raiz1})")

        else:
            return(f"({raiz1}, {raiz2})")
    else:
        return("( )")



def value_y(a, b, c, x):
    valor = (a * x)
    valor1 = valor ** 2
    valor2 = (b * x)
    valor3 = valor1 + valor2 + c
    return(valor3)


def to_string(a, b, c):
    if a == 0 and b != 0 and c!= 0:
        return (f"f(x) = {b} * X + {c}")
    elif b == 0 and a != 0 and c != 0:
        return (f"f(x) = {a} * X^2 + {c}")
    elif a == 0 and b == 0 and c != 0:
        return (f"f(x) = {c}")
    elif c == 0 and a != 0 and b != 0:
        return (f"f(x) = {b} * X")
    elif c == 0 and b == 0 and c != 0:
        return (f"f(x) = {a} * X^2")
    elif c == 0 and a == 0 and b != 0:
        return(f"f(x) = {b} * X")
    else:
        return(f"f(x) = {a} * X^2 + {b} * X + {c}")

def derivation(a, b, c):
    val1 = 2 * a
    if a != 0 and b != 0:
        return(f"f'(x) = {val1} * X + {b}")
    elif a != 0 and b == 0:
        return (f"f'(x) = {val1} * X")
    else:
        return (f"f'(x) = {b}")
