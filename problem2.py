import math

def compute_gcd_sum(lines):

    total = 0

    for line in lines:

        line = line.strip().replace(',', ' ')

        parts = line.split()

        if len(parts) != 3:

            continue

        try:

            a, b, c = map(int, parts)

            total += math.gcd(math.gcd(a, b), c)

        except Exception:

            continue

    return total
 
lines = [

    "23 45 67",

    "12,14,18",

    "4, 5, 9",

    "100 200",

    "10,20,30,40",

    "-5 0 5"

]

print(compute_gcd_sum(lines))
 