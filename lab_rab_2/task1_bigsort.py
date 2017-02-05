import tempfile
import sys


def delimited_readl(f, new_str):
    buf = ""
    while True:
        while new_str in buf:
            pos = buf.index(new_str)
            yield buf[:pos] + new_str
            buf = buf[pos + len(new_str):]
        piece = f.read(4096)
        if not piece:
            yield buf
            break
        buf += piece


def check_mem(string):
    return int(string)


class Sorter(object):
    def __init__(self, cur_buf_size, config):
        self.buf_size = cur_buf_size
        self.config = config
        self.part_of_f = list()
        if config.keys is not None:
            self.sort_keys = [int(x.strip()) for x in config.keys.split(",")]
        else:
            self.sort_keys = None

    def split_parts(self, file_object):
        self.part_of_f[:] = []
        with file_object:
            cur_size_of_part = 0
            str_buf = list()
            for str in delimited_readl(file_object, self.config.line_separator):
                if str == "":
                    continue

                cur_size_of_part += len(str)
                if cur_size_of_part > self.buf_size:
                    cur_temp_file = tempfile.TemporaryFile(prefix="tmp_sort_")
                    str_buf.sort(key=self.key_sort, reverse=self.config.reverse)
                    cur_temp_file.write("".join(str_buf))
                    str_buf[:] = []
                    self.part_of_f.append(cur_temp_file)
                    cur_size_of_part = len(str)
                str_buf.append(str)

            if cur_size_of_part > 0:
                cur_temp_file = tempfile.TemporaryFile(prefix="tmp_sort_")
                str_buf.sort(key=self.key_sort, reverse=self.config.reverse)
                cur_temp_file.write("".join(str_buf))
                str_buf[:] = []
                self.part_of_f.append(cur_temp_file)

    def merge(self):
        for i in range(len(self.part_of_f) // 2):
            file1 = self.part_of_f[i]
            file2 = self.part_of_f[i + 1]
            file1.seek(0)
            file2.seek(0)
            f_out = tempfile.TemporaryFile(prefix="tmp_sort_")
            gen_file1 = delimited_readl(file1, self.config.line_separator)
            gen_file2 = delimited_readl(file2, self.config.line_separator)
            file1_str = next(gen_file1, "")
            file2_str = next(gen_file2, "")
            while file1_str != "" and file2_str != "":
                if self.key_sort(file1_str) < self.key_sort(file2_str) or self.config.reverse:
                    f_out.write(file1_str)
                    file1_str = next(gen_file1, "")
                else:
                    f_out.write(file2_str)
                    file2_str = next(gen_file2, "")

            while file1_str != "":
                f_out.write(file1_str)
                file1_str = next(gen_file1, "")

            while file2_str != "":
                f_out.write(file2_str)
                file2_str = next(gen_file2, "")

            file1.close()
            file2.close()
            del self.part_of_f[i:i + 2]
            self.part_of_f.insert(i, f_out)

    def sort(self, f_obj, f_obj_out):
        self.split_parts(f_obj)
        while len(self.part_of_f) > 1:
            self.merge()
        f_in = self.part_of_f[0]
        f_in.seek(0)
        for line in delimited_readl(f_in, self.config.line_separator):
            f_obj_out.write(line)
        f_in.close()

    def key_sort(self, item):
        words = item.strip(self.config.line_separator).split(self.config.field_separator)
        cmp_list = list()
        if self.sort_keys is not None:
            for key in self.sort_keys:
                if self.config.numeric:
                    cmp_list.append(int(words[key - 1]))
                else:
                    cmp_list.append(words[key - 1])

        else:
            for key in words:
                if self.config.numeric:
                    cmp_list.append(int(key))
                else:
                    cmp_list.append(key)

        return cmp_list

    def checking(self, file_object):
        f_gen = delimited_readl(file_object, self.config.line_separator)
        str1 = next(f_gen, "")
        while str1 != "":
            str2 = next(f_gen, "")
            if str2 != "" and self.key_sort(str1) > self.key_sort(str2):
                return False
            str1 = str2
        return True


