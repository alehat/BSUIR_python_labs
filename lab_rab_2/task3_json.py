import types


class JsonTypeError(TypeError):
    def __init__(self, obj_type):
        self.ex_type = obj_type
        self.message = "Unserializable json type: " + str(obj_type)

'''def to_json(obj, raise_unknown=False):
    ister = True
    list_types = (types.ListType, types.TupleType)
    numeric_types = (types.IntType, types.LongType, types.FloatType, types.ComplexType)

    if isinstance(obj, types.BooleanType):
        result = str(obj).lower()
    elif type(obj) in numeric_types:
        result = "{}  ".format(obj)
    elif isinstance(obj, types.StringType):
        result = '\+ obj + '\ '
    elif obj is None:
        return "null"
    return result'''


def to_json(obj, raise_unknown=False):
    list_types = (types.ListType, types.TupleType)
    numeric_types = (types.IntType, types.LongType, types.FloatType)
    mark_d = False

    if type(obj) in numeric_types:
        res = '{}  '.format(obj)

    elif isinstance(obj, types.StringType):
        res = '\"' + obj + '\"  '

    elif type(obj) in list_types:
        res = '['

    elif isinstance(obj, types.DictionaryType):
        mark_d = True
        d_obj = obj
        res = '{'

    else:
        if raise_unknown:
            raise JsonTypeError(obj.__class__)
        mark_d = True
        d_obj = obj.__dict__
        res = '{'

    cont = []
    if type(obj) in numeric_types:
        cont = obj

    elif mark_d:
        cont = d_obj.keys()

    for item in cont:
        if not type(obj) in numeric_types:
            res += '\"{}\":'.format(item)
            item = d_obj[item]

        else:
            item = item

        if isinstance(item, types.BooleanType):
            if item:
                res += "true"
            else:
                res += "false"

        elif isinstance(item, types.StringType):
            res += '\"{}\"'.format(item)

        elif type(item) in numeric_types:
            res += "{}".format(item)

        elif type(item) in numeric_types:
            res += to_json(item, raise_unknown)

        elif isinstance(item, types.NoneType):
            res += "null"

        else:
            if raise_unknown:
                raise JsonTypeError(item.__class__)
            res += to_json(item, raise_unknown)
        res += ", "

    res = res[:len(res) - 2]
    if type(obj) in numeric_types:
        res += "]"
    elif isinstance(obj, types.DictionaryType):
        res += "}"

    return res


def test():
    class Trip(object):
        def __init__(self):
            self.country = "China"
            self.date = (20, 7, 2016)

    trip = Trip()
    try:
        print to_json(trip, True)
    except JsonTypeError as e:
        print e.message

    class Book(object):
        def __init__(self):
            self.title = "FIFTY-FIRST STATE"
            self.author = "Hilary Bailey"
            self.id = (7, 9)
            self.param = {'length': 370, 'format': 4, 'weight, g': 315}
            self.types = ["PaperBook", "eBup"]

    book = Book()
    try:
        print to_json(book)
    except JsonTypeError as e:
        print e.message

    print to_json({"value0": 0, "value1": 1})
    print to_json("Some json test string")
    print to_json([1, 2, 3, 4, 5])

if __name__ == "__main__":
    test()
