import sys
from PyQt4 import QtGui, QtCore

class QExampleLabel (QtGui.QLabel):
    def __init__(self, filePath, parentQWidget = None, ):
        # super(QExampleLabel, self).__init__(parentQWidget)
        super(QExampleLabel,self).__init__(parentQWidget)
        # self.initUI(filePath)

    def initUI (self,filePath):
        self.setPixmap(QtGui.QPixmap(filePath))


    def mousePressEvent (self, eventQMouseEvent):
        self.originQPoint = eventQMouseEvent.pos()
        self.currentQRubberBand = QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self)
        self.currentQRubberBand.setGeometry(QtCore.QRect(self.originQPoint, QtCore.QSize()))
        self.currentQRubberBand.show()

    def mouseMoveEvent (self, eventQMouseEvent):
        self.currentQRubberBand.setGeometry(QtCore.QRect(self.originQPoint, eventQMouseEvent.pos()).normalized())

    def mouseReleaseEvent (self, eventQMouseEvent):
        self.currentQRubberBand.hide()
        currentQRect = self.currentQRubberBand.geometry()
        self.currentQRubberBand.deleteLater()
        cropQPixmap = self.pixmap().copy(currentQRect)
        cropQPixmap.save('output.png')
        self.setPixmap(QtGui.QPixmap('output.png'))

#
# class CropWindow(QtGui.QMainWindow, QExampleLabel):
#     def __init__(self, filePath,parent=None):
#         super(CropWindow, self).__init__(filePath,parent)
#         # self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
#         self.setupUi(self)
#
# if __name__ == '__main__':
#     myQApplication = QtGui.QApplication(sys.argv)
#     myQExampleLabel = QExampleLabel()
#     myQExampleLabel.show()
#     sys.exit(myQApplication.exec_())