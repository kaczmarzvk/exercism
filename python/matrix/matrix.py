class Matrix:
    def __init__(self, matrix_string: str):
        self.rows = matrix_string.split('\n')

    def row(self, index):
        return [int(i) for i in self.rows[index-1].split(' ')]
        

    def column(self, index):
        return [int(row.split(' ')[index-1]) for row in self.rows]