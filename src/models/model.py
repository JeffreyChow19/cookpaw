class Model:
    @classmethod
    def from_row(cls, row):
        return cls(*row)