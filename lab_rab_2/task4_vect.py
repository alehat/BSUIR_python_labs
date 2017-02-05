import exceptions
import types


class Vector(object):
    def __init__(self, vector_value_list):
        self.vector_value_list = vector_value_list
        self.dimension = len(vector_value_list)

    def __add__(self, other):
        if isinstance(other, Vector):
            if self.dimension != len(other):
                raise exceptions.\
                    ValueError("Vectors must have the same dimensions!")

        new_vector_value_list = []
        for i in xrange(self.dimension):
            new_vector_value_list.\
                append(self.vector_value_list[i] + other.vector_value_list[i])
        return Vector(new_vector_value_list)

    def __sub__(self, other):
        if isinstance(other, Vector):
            if self.dimension != len(other):
                raise exceptions.\
                    ValueError("Vectors must have the same dimensions!")

        new_vector_value_list = []
        for i in xrange(self.dimension):
            new_vector_value_list.\
                append(self.vector_value_list[i] - other.vector_value_list[i])
        return Vector(new_vector_value_list)

    def __mul__(self, other):
        new_value_list = []

        numeric_types = (types.IntType, types.LongType, types.FloatType)
        if isinstance(other, numeric_types):
            for i in xrange(self.dimension):
                new_value_list.append(self.vector_value_list[i] * other)
            return Vector(new_value_list)
        elif isinstance(other, Vector):
            if self.dimension != len(other):
                raise exceptions.\
                    ValueError("Vectors must have the same dimensions!")
            else:
                for i in xrange(self.dimension):
                    new_value_list.\
                        append(self.vector_value_list[i] * other.vector_value_list[i])
                return Vector(new_value_list)
        else:
            raise exceptions.TypeError("You can multiply a vector by "
                                       "a vector or vector by the number only!")

    def __eq__(self, other):
        if not isinstance(other, Vector):
            raise exceptions.\
                TypeError("Vector can be compared only with another vector!")
        if self.dimension != len(other):
            return False

        for i in range(self.dimension):
            if self.vector_value_list[i] != other.vector_value_list[i]:
                return False
        return True

    def __len__(self):
        return self.dimension

    def __getitem__(self, item):
        numeric_types = (types.IntType, types.LongType, types.FloatType)
        if not isinstance(item, numeric_types):
            raise exceptions.\
                TypeError("Vector's must have an numerical (int, float) type!")
        if 0 < item < len(self):
            print("No such element! Input correct index.")
        return self.vector_value_list[item]

    def __str__(self):
        return "(" + ", ".join([str(x) for x in self.vector_value_list]) + ")"


def test():
    vector_1 = Vector([1, -3, 5, 7])
    vector_2 = Vector([-2, 10, -9, -3])
    eq_vector = Vector((-14, 70, -63, -21))

    print "Vector1 Value = " + str(vector_1)
    print "Vector2 Value = " + str(vector_2)

    vector_3 = vector_1 + vector_2
    print "Addition Result: " + str(vector_3)

    vector_3 = vector_1 - vector_2
    print "Subtraction Result: " + str(vector_3)

    vector_3 = vector_1 * vector_2
    print "Scalar Multiplication Vectors Result: " + str(vector_3)

    vector_3 = vector_2 * 7
    print "Multiplication Vector2 by the Const 7: " + str(vector_3)

    print "Vector1 is Equal to Vector2 (True/False): " + str(vector_1 == vector_2)
    print "Vector3 is Equal to Vector = (-14, 70, -63, -21) (True/False): " + str(vector_3 == eq_vector)

    print "Vector2 Length: " + str(len(vector_2))

    print "Vector3 Value: " + str(vector_3)
    print "Index[3]: " + str(vector_3[3])


if __name__ == "__main__":
    test()
