


from ui_mainwindow import Ui_Form
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import sys
import modeller
from PyQt5 import uic


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = uic.loadUi("mainwindow.ui", self)


    def on_pushButton_model_clicked(self):
        u = self.ui
        parameters = {
            'client_m': float(u.le_client_m.text()),
            'client_d': float(u.le_client_d.text()),
            'op0_m':    float(u.le_op0_m.text()),
            'op0_d':    float(u.le_op0_d.text()),
            'op1_m':    float(u.le_op1_m.text()),
            'op1_d':    float(u.le_op1_d.text()),
            'op2_m':    float(u.le_op2_m.text()),
            'op2_d':    float(u.le_op2_d.text()),
            'comp0_m':  float(u.le_comp0_m.text()),
            'comp1_m':  float(u.le_comp1_m.text()),
            'c_count':  float(u.le_client_count.text())
        }
        miss, prob = modeller.event_based_modelling(**parameters)
        self.ui.le_lost_clients.setText('{:.4f}'.format(prob))
        self.ui.lost.setText(str(miss))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == '__main__':
    sys.exit(main())
