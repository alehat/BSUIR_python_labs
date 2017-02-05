class Logger(object):
    log = ""

    def __getattribute__(self, item):
        attr = object.__getattribute__(self, item)

        if callable(attr):
            def tmp_func(*args, **kwargs):
                func_result = attr(*args, **kwargs)
                self.log += "{func_name}({args}, {kwargs}) == {func_result}\n".\
                    format(func_name=item, func_result=func_result, args=args, kwargs=kwargs)
                return func_result

            return tmp_func

        return attr

    def __str__(self):
        return self.log


def test():
        class TestClass(Logger):
            some_par = 0

            def logging_result(self, test_param, **kwargs):
                self.some_par = test_param * 2
                print 'func with params:', test_param, kwargs, '\n'
                return self.some_par

        t = TestClass()
        t.logging_result(5)
        print t
        t.logging_result(10, attem=9)
        print t
        t.logging_result(20, attem=10, time="01:30", status="kill me, please!")
        print t


if __name__ == "__main__":
    test()
