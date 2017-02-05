def cached(func_to_decor):
    cache_dict = dict()

    def wrapper(*args, **kwargs):
        cache_key = func_to_decor.__name__ +\
                    str(args) + str(kwargs)
        if cache_key in cache_dict:
            print "Take an already existing value:"
            return cache_dict[cache_key]
        else:
            print "Add new value:"
            result = func_to_decor(*args, **kwargs)
            cache_dict[cache_key] = result
            return result

    return wrapper


def test():
    @cached
    def gcd(a, b):
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return a + b
    #gcd = cached(gcd)

    print(gcd(300, 18))
    print(gcd(1024, 480))
    print(gcd(300, 18))


if __name__ == "__main__":
    test()
