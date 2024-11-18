import rasterio
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QMessageBox
from gis_form import Form_Gis
import sys

class Form_main_Programm(QtWidgets.QMainWindow,Form_Gis):

    def __init__(self):
        '''
           def __init__(self) предназначен для инициализации класса
           Последние две команды метода связывают кнопки начала и завершения с нажатием на них.
        '''
        super().__init__()
        self.setupUi(self)

        self.pushButton_load_map.clicked.connect(self.load_map)
        self.pushButton_close_program.clicked.connect(self.close_program)

    def load_map(self):
        path = 'srtm_46_01/srtm_46_01.tif'
        with rasterio.open(path) as dataset:
            image = dataset.read(1)  # Чтение первого канала
            img = Image.fromarray(image)
            img.save('temp_image.png')  # Сохранение временного изображения
            pixmap = QPixmap('temp_image.png')
            self.label_main_map.setPixmap(pixmap)
    def close_program(self):
        'Функция отвечающая за закрытие программы'
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Form_main_Programm()
    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(QPixmap("picture_fon.jpg")))
    form.setPalette(palette)
    form.show()
    sys.exit(app.exec_())