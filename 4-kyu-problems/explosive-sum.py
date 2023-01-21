"""
How many ways can you make the sum of a number?

4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
"""

def exp_sum(n: int) -> int:
    """Calculates the number of integer partitions for a given
    integer n using memoization

    Args:
        n (int): positive integer

    Returns:
        int: the number of integer partitions for n
    """
    partitions = [0] * (n + 1)
    partitions[0] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]
    return partitions[n]
