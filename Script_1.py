class Matrix:
    def __init__(self, matr_1, matr_2, matr_3):
        maxlen = max(len(matr_1), len(matr_2), len(matr_3))
        for i in range(maxlen):
            if (len(matr_1) < maxlen):
                matr_1 += 0
            if len(matr_2) < maxlen:
                matr_2 += 0
            if len(matr_3) < maxlen:
                matr_3 += 0
        self.matr_1 = matr_1
        self.matr_2 = matr_2
        self.matr_3 = matr_3

    def __str__(self):
        return f'{self.matr_1} {self.matr_2} {self.matr_3}'

    def __add__(self, other):
        result_1 = []
        result_2 = []
        result_3 = []
        for i in range(len(self.matr_1)):
            result_1.append(self.matr_1[i] + other.matr_1[i])
        for i in range(len(self.matr_2)):
            result_2.append(self.matr_2[i] + other.matr_2[i])
        for i in range(len(self.matr_3)):
            result_3.append(self.matr_3[i] + other.matr_3[i])
        result = Matrix(result_1, result_2, result_3)
        return result


my_matr = Matrix([1, 2, 3], [2, 3, 4], [5, 6, 7])
print(my_matr)
print(my_matr+my_matr)