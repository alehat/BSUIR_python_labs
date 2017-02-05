class MyMetaclass(type):
    def __new__(mcs, name, bases, dct):
        filename = dct['filename']
        if filename != "":
            try:
                with open(filename, "r") as file_handle:
                    for line in file_handle:
                        if line != "":
                            param = line.strip().split(' ', 1)
                            dct[param[0]] = param[1]
                return super(MyMetaclass, mcs).__new__(mcs, name, bases, dct)
            except Exception, e:
                    print e


def test():
    class Book(object):
        __metaclass__ = MyMetaclass
        filename = "metaclass.txt"
        publishing_house = "Bloomsbury"

    book = Book()
    print "To buy a book {0} by {1}. Publishing House: {2}, {3}, {4}.".\
        format(book.title, book.author, book.publishing_house, book.year, book.format)


if __name__ == "__main__":
    test()

