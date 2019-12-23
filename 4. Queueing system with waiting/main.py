from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import sys
import modeller


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = uic.loadUi("window.ui", self)

    @pyqtSlot(name='on_pushButton_clicked')
    def _parse_parameters(self):
        try:
            ui = self.ui
            a = float(ui.lineEdit_generator_a.text())
            b = float(ui.lineEdit_generator_b.text())
            m = float(ui.lineEdit_servicemachine_m.text())
            d = float(ui.lineEdit_servicemachine_d.text())
            req_count = int(ui.lineEdit_request_count.text())
            reenter_prob = float(ui.lineEdit_reenter_probability.text())
            delta_t = float(ui.lineEdit_deltat.text())
            modelT = modeller.Model(delta_t, req_count, reenter_prob)
            results1 = modelT.time_based_modelling(a, b, m, d)
            modelEvent = modeller.Model(delta_t, req_count, reenter_prob)
            results2 = modelEvent.event_based_modelling(a, b, m, d)
            self._show_results(results1, results2)
            
        except ValueError:
            QMessageBox.warning(self, 'Ошибка', 'Ошибка в данных!')
        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', e)

    def _show_results(self, results1, results2):
        ui = self.ui
        queue_len_max1, req_done_count1, reenter1 = results1
        ui.lineEdit_res_reentered_count.setText(str(reenter1))
        ui.lineEdit_res_max_queue_size.setText(str(queue_len_max1))
        queue_len_max2, req_done_count2, reenter2 = results2
        ui.lineEdit_res_reentered_count_2.setText(str(reenter2))
        ui.lineEdit_res_max_queue_size_2.setText(str(queue_len_max2))

    @pyqtSlot(int)
    def on_comboBox_method_currentIndexChanged(self, index):
        if index == 1:
            # Δt
            visibility = True
        else:
            visibility = False
            # events
        self.ui.lineEdit_deltat.setEnabled(visibility)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == '__main__':
    sys.exit(main())
