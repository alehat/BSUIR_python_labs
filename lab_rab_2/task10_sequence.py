class Sequence(object):
    def __init__(self, iter_object):
        self.iter_object = iter_object
        self.seq_list = list()

    def __iter__(self):
        for i in iter(self.iter_object):
            yield i

    def filter(self, func):
        def temp_gen():
            for item in iter(self):
                if func(item):
                    yield item
        return Sequence(temp_gen())
        #return Sequence([value for value in self.iter_object if func(value)])

    def __str__(self):
        return "[" + ", ".join([str(x) for x in iter(self)]) + "]"


def test():
    s1 = Sequence([1, 2, 3, 4, 5, 6, 7, 8])
    print s1.filter(lambda x: x > 4)
    print s1.filter(lambda x: x % 2 == 0)

if __name__ == "__main__":
    test()
