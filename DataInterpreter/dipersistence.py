#persistence layer for DataInterpreter CLI App
import csv


class DiPersistence(object):

    def __init__(self, default_save):
        self.default_save_path = default_save

    def load_csv(self, filename):
        all_data= []
        # try:
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            try:
                for row in reader:
                    all_data.append(row)
                return all_data
            except csv.Error as e:
                raise('file {}, line {}: {}'.format(filename, reader.line_num, e))
        # except FileNotFoundError as no_file_e:
        #   raise('file {}: {}'.format(filename, no_file_e))

