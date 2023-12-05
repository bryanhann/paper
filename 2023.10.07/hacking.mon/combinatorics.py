def permute( total, take ):
   return factorial(total)/factorial(total-take)


def choose( total, take ):
    return permute( total, take ) / permute(take,take)
