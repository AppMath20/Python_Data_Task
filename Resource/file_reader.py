seq_pos_in_line = 5


def check_line(line):
    seq = line.split()[seq_pos_in_line]  # Look at the consistency
    if seq.count(seq[0]) == len(seq):  # If it consists of repeated characters we return the string
        yield line


def file_reader_generator(file):
    for line in file:
        if check_line(line):
            yield line


class FileReader(object):
    def __init__(self, file_name):
        self.file_name = file_name  # We received the file we are working with

    def __enter__(self):
        self.file_obj = open(self.file_name, "r")  # Opened the file that we are working with for reading
        ln = self.file_obj.readline()  # Read one line
        return file_reader_generator(self.file_obj)  # Returned the generator to read the correct lines

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()
