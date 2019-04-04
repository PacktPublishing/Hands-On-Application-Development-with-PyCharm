def custom_sum(n=1000000):
    result = 0
    for i in range(n):
        result += i

    return result


def built_sum(n=1000000):
    result = sum(range(n))
    return result


if __name__ == '__main__':
    print(custom_sum())
    #print(built_sum())
