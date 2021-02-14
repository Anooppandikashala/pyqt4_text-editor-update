# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from croper import QExampleLabel

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def __init__(self,filePath):
        self.filePath = filePath

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.label = QExampleLabel(self.filePath,Form)
        # self.label =  QtGui.QLabel(Form)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.label.initUI(self.filePath)


    def initUI(self):
        self.label.setPixmap(QtGui.QPixmap(self.filePath))

    # def mousePressEvent (self, eventQMouseEvent):
    #     self.originQPoint = eventQMouseEvent.pos()
    #     self.currentQRubberBand = QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self)
    #     self.currentQRubberBand.setGeometry(QtCore.QRect(self.originQPoint, QtCore.QSize()))
    #     self.currentQRubberBand.show()
    #
    # def mouseMoveEvent (self, eventQMouseEvent):
    #     self.currentQRubberBand.setGeometry(QtCore.QRect(self.originQPoint, eventQMouseEvent.pos()).normalized())
    #
    # def mouseReleaseEvent (self, eventQMouseEvent):
    #     self.currentQRubberBand.hide()
    #     currentQRect = self.currentQRubberBand.geometry()
    #     self.currentQRubberBand.deleteLater()
    #     cropQPixmap = self.label.pixmap().copy(currentQRect)
    #     cropQPixmap.save('output.png')
    #     self.label.setPixmap(QtGui.QPixmap('output.png'))

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "TextLabel", None))

# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     Form = QtGui.QWidget()
#     ui = Ui_Form("example.jpg")
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())