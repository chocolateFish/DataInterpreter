#persistence layer for DataInterpreter CLI App
import csv
import sys


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
                raise Exception('file {}, line {}: {}'.format(filename, reader.line_num, e))from e
            except FileNotFoundError:
                raise
