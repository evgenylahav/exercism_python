class Matrix(object):
    def __init__(self, matrix_string):
        self._prepare_data(matrix_string)

    def _prepare_data(self, matrix_string):
        self.matrix = [
            [int(x) for x in row.split()]
            for row in matrix_string.splitlines()
        ]
        self.transposed_matrix = list(map(list, zip(*self.matrix)))

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return self.transposed_matrix[index - 1]
