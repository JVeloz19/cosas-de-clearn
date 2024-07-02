def bit_rec(n, exp):
    if 2**exp < n:
        return bit_rec(n,exp+1)
    return 2**exp