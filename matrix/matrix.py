class Matrix:
    def __init__(self, matrix_string):
        self.matrix =  [[int(num) for num in row.split(' ')] # split for column
            for row in matrix_string.split("\n")] # split for row

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
