def minBanaEat(piles, h):
    left = 1
    right = max(piles)

    while left <= right:
        mid = (left + right) // 2
        k = 0
        for p in piles:
            k += (p // mid) + (p % mid != 0)
        if k <= h:
            right = mid - 1
        else:
            left = mid + 1

    return left
