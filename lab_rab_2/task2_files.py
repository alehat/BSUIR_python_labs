import random
import sys


class GenFiles(object):
    def __init__(self, out_f, num, col_count, field_sep, line_sep):
        self.out_file = out_f
        self.numeric = num
        self.word_sep = field_sep
        self.str_sep = line_sep
        self.cols = col_count

    def words_gen(self):
        if self.numeric:
            self.out_file.write(str(random.randint(-10000, 10000)))
        else:
            symb_count = random.randint(1, 5)
            for i in xrange(symb_count):
                self.out_file.write(chr((random.randint(0, 25) + random.choice([65, 97]))))

    def str_gen(self):
        for _ in xrange(self.cols):
            self.words_gen()
            if _ < self.cols - 1:
                self.out_file.write(self.word_sep)

    def generate(self, count):
        for _ in xrange(count):
            self.str_gen()
            self.out_file.write(self.str_sep)

    def close(self):
        self.out_file.close()

