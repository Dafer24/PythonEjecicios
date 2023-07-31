class Triangle:
    def __init__(self, rows):
        self.rows = rows

    def showNumericTriangle(self):
        if self.rows < 1:
            print("The number of rows must be greater than or equal to 1.")
            return

        num = (self.rows * 2) - 1
        for i in range(1, self.rows + 1):
            num = (i * 2) - 1
            for j in range(1, i + 1):
                print(num, end=' ')
                num -= 2
            print()

numRows = int(input("Enter an integer for the number of rows in the numeric triangle: "))
tri = Triangle(numRows)
tri.showNumericTriangle()
