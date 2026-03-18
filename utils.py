# ==============================
# AIRCRAFT CONSTANTS
# ==============================

DOW = 43898
DOI = 58.4
ADULT = 75

# ==============================
# TRIM TABLE (CG → STAB)
# ==============================

TRIM_TABLE = [
    (20, 6.5),
    (22, 5.5),
    (24, 4.5),
    (26, 3.5),
    (28, 2.5),
    (30, 1.5),
    (32, 0.5),
    (34, -0.5),
    (36, -1.5),
    (38, -2.5)
]

# ==============================
# FUNCTIONS
# ==============================

def index_to_cg(index):
    return 20 + index * 0.2


def get_stab_from_cg(cg):
    table = sorted(TRIM_TABLE)

    for i in range(len(table) - 1):
        cg1, s1 = table[i]
        cg2, s2 = table[i + 1]

        if cg1 <= cg <= cg2:
            ratio = (cg - cg1) / (cg2 - cg1)
            return round(s1 + ratio * (s2 - s1), 2)

    # Outside range
    if cg < table[0][0]:
        return table[0][1]
    else:
        return table[-1][1]
