from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
import scipy.stats as stats
import random
import math 
import numpy as np
from itertools import islice
from scipy.stats import chi2

class randomGenerator():
    def __init__(self):
        self.cur_random = 1
    def generate_random_variable(self, low = 0, high = 100):
        # квадратичный конгуэнтный генератор псевдослучайных чисел
        m = 2.**31 - 1
        a1 = 75.
        a2 = 75.
        b = 75.
        self.cur_random = (self.cur_random**2 * a1 + self.cur_random * a2 + b) % m
        result = int(np.round(low + float(self.cur_random % (high - low))))
        return result
    

def randomness_criterion(sequence):
    # критерий серий + критерий частот (Джордж Марсалья)
    n = len(sequence) 
    d = 10
    sumAll1 = 0
    sumAll2 = 0
    p1 = 1 / d
    p2 = 1 / d**2
    flagFreqCrit = True
    for i in range(d):
        for j in range(d):
            y1 = 0
            y2 = 0
            for h in range(n - 1):
                if (sequence[h] == i and sequence[h + 1] == j):
                    y2 += 1
                if (flagFreqCrit) :
                    if (sequence[h] == j):
                        y1 += 1
            if (flagFreqCrit):
                sumAll1 += y1**2 / p1
            sumAll2 += y2**2 / p2
        flagFreqCrit = False
    sumAll1 = sumAll1 / n - n
    sumAll2 = sumAll2 / n - n
    crit = chi2.cdf(sumAll2 - sumAll1, d * (d - 1))
    return (1 - crit)

# print(randomness_criterion([1,2,3,4,5,6]))
# print(randomness_criterion([2,2,2,2,2,2]))
# print(randomness_criterion([0, 3, 3, 8, 6, 6, 5, 3, 2, 2]))

def alg_fill_calc_click(w):
    table = w.alg_table
    one_digit = [w.randomGenerator.generate_random_variable(0, 9) for i in range(w.num_of_elements)]
    two_digits = [w.randomGenerator.generate_random_variable(10, 99) for i in range(w.num_of_elements)]
    three_digits = [w.randomGenerator.generate_random_variable(100, 999) for i in range(w.num_of_elements)]
    for i in range(w.num_of_rows):
        item = QTableWidgetItem(str(one_digit[i]))
        table.setItem(i, 0, item)

    for i in range(w.num_of_rows):
        item = QTableWidgetItem(str(two_digits[i]))
        table.setItem(i, 1, item)

    for i in range(w.num_of_rows):
        item = QTableWidgetItem(str(three_digits[i]))
        table.setItem(i, 2, item)

    #table.resizeColumnsToContents()
    crit_for_one = randomness_criterion(one_digit[:w.num_of_rows])
    crit_for_two = randomness_criterion(two_digits[:w.num_of_rows]) 
    crit_for_three = randomness_criterion(three_digits[:w.num_of_rows])
    w.meas_alg_1.setText('{:.2%}'.format(crit_for_one))
    w.meas_alg_2.setText('{:.2%}'.format(crit_for_two))
    w.meas_alg_3.setText('{:.2%}'.format(crit_for_three))
    

def fill_table_calc_click(w):
    table = w.table_table
    numbers = set()
    
    with open('table.txt') as file: 

        lines = islice(file, w.line_num, None)
        for l in lines:
            numbers.update(set(l.rstrip().split(" ")))
            w.line_num += 1
            if len(numbers) >= w.num_of_elements * 3:
                break
        numbers = list(numbers)
    one_digit = [int(i)%9 + 1 for i in numbers[:w.num_of_elements]]
    two_digits = [int(i)%90 + 10 for i in numbers[w.num_of_elements:w.num_of_elements * 2]]
    three_digits = [int(i)%900 + 100 for i in numbers[2 * w.num_of_elements:3 * w.num_of_elements]]
    
    for i in range(w.num_of_rows):
        item = QTableWidgetItem(str(one_digit[i]))
        table.setItem(i, 0, item)

    for i in range(w.num_of_rows):
        item = QTableWidgetItem(str(two_digits[i]))
        table.setItem(i, 1, item)

    for i in range(w.num_of_rows):
        item = QTableWidgetItem(str(three_digits[i]))
        table.setItem(i, 2, item)

    crit_for_one = randomness_criterion(one_digit[:w.num_of_rows])
    crit_for_two = randomness_criterion(two_digits[:w.num_of_rows]) 
    crit_for_three = randomness_criterion(three_digits[:w.num_of_rows])
    w.meas_table_1.setText(' {:.2%}'.format(crit_for_one))
    w.meas_table_2.setText(' {:.2%}'.format(crit_for_two))
    w.meas_table_3.setText(' {:.2%}'.format(crit_for_three))

def manual_input_calc_click(w):
    input = w.manual_input
    measure = w.meas_manual
    sequence = input.text().split(" ")
    filtered_sequence = []
    for i in sequence:
        try:
            int(i)
        except ValueError:
            continue
        else:
            filtered_sequence.append(i)

    entropy = randomness_criterion(list(map(lambda x: int(x), filtered_sequence)))
    w.meas_manual.setText(' {:.2%}'.format(entropy))




class window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("window.ui", self)
        self.fill_alg.clicked.connect(lambda: alg_fill_calc_click(self))
        self.fill_table.clicked.connect(lambda: fill_table_calc_click(self))
        self.fil_manualy.clicked.connect(lambda: manual_input_calc_click(self))
        
        self.manual_input.returnPressed.connect(lambda: manual_input_calc_click(self))
        self.meas_alg_1.setReadOnly(True)
        self.meas_alg_2.setReadOnly(True)
        self.meas_alg_3.setReadOnly(True)
        self.meas_table_1.setReadOnly(True)
        self.meas_table_2.setReadOnly(True)
        self.meas_table_3.setReadOnly(True)
        self.meas_manual.setReadOnly(True)
        self.alg_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.num_of_elements = 1000
        self.num_of_rows = 10
        self.line_num = 0
        self.randomGenerator = randomGenerator()

        for i in range(10):
            self.alg_table.insertRow(i)

        for i in range(10):
            self.table_table.insertRow(i)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = window()
    w.show()
    sys.exit(app.exec_())