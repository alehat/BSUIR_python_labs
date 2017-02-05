import exceptions


class MyXrange:
    def __init__(self, *args):
        if len(args) == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1

        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1

        elif len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
            if args[2] == 0:
                raise exceptions.\
                    ValueError("Generation's step can't be equal to zero!")

    def __iter__(self):
        return self

    def next(self):
        if ((self.start >= self.stop) and (self.step > 0)) \
                or ((self.start <= self.stop) and (self.step < 0)):
            raise exceptions.StopIteration()
        else:
            cur_val = self.start
            self.start += self.step
            return cur_val


def test():
    for num in MyXrange(5):
        print '{}'.format(num)
    print ("____________")

    for num1 in MyXrange(30, 300, -10):
        print '{}'.format(num1)


if __name__ == "__main__":
    test()