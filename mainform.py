from PyQt4 import QtCore, QtGui, uic, QtWebKit
from PyQt4.QtGui import QVBoxLayout

import requests

import data_rc
import ui_rc


class SearchButton(QtCore.QObject):
    def __init__(self):
        super(SearchButton, self).__init__()
        self.__data = None

    @QtCore.pyqtSlot(str)
    def showMessage(self, msg):
        QtGui.QMessageBox.information(None, "Info", msg)


    @QtCore.pyqtSlot(str, str)
    def search(self, lat, lon):
        print lat, lon
        url = 'https://api.vk.com/method/photos.search?lat=%s&long=%s&radius=%s' % (lat, lon, 50000)
        r = requests.get(url)
        self.__data = r.text


    def _data(self):
        return self.__data

    def _pyVersion(self):
        return '1234'

    pyVersion = QtCore.pyqtProperty(str, fget=_pyVersion)
    pyData = QtCore.pyqtProperty(str, fget=_data)


class WebPage(QtWebKit.QWebPage):
    def __init__(self):
        super(WebPage, self).__init__()

    def javaScriptConsoleMessage(self, msg, line, source):
        print '%s line %d: %s' % (source, line, msg)



class MainForm(QtGui.QDialog):

    def __init__(self):
        self.myObj = SearchButton()
        super(MainForm, self).__init__()

        uic.loadUi('main.ui', self)

        web_view = self.findChild(QtWebKit.QWebView, 'webView')
        web_page = web_view.page()
        web_page.currentFrame().addToJavaScriptWindowObject("pyObj", self.myObj)

        web_view.setPage(web_page)
        web_view.load(QtCore.QUrl('qrc:///index.html'))