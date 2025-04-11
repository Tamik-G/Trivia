def digital_root(n):
    if n > 9:
        case = 0
        for i in str(n):
            case += int(i)
        n = case
        return digital_root(n)
    else:
        return n
