def solution(n):
    if (n % (int(n))) > 0.75:
        n = int(n) + 1
    elif (n % (int(n))) > 0.25:
        n = int(n) + 0.5
    else:
        n = int(n)
    return n
