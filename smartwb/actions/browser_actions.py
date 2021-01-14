import os
import sys

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtGui import *

#from .. import settings

class BrowserProvider:
    """
    Creation of Tabs and attachement of basic controls.
    It requires a qtabwidget to which the tabs will be added.
    """
    def __init__(self, window, urlbar):
        if not issubclass(type(window), QMainWindow):
            raise Exception("window object must be of type QMainWindow")
        
        if type(urlbar) is not QLineEdit:
            raise Exception("urlbar must be an instance of QLineEdit")

        self.__window = window
        self.__urlbar = urlbar
        self.__create_tab_widget()
        self.create_new_tab()
    
    def __create_tab_widget(self):
        if self.__tabview is not None:
            return
        
        tabview = QTabWidget()
        tabview.setDocumentMode(True)
        tabview.setTabsClosable(True)
        tabview.tabBarDoubleClicked.connect(self.__on_add_tab)
        tabview.currentChanged.connect(self.__on_tab_changed)
        tabview.tabCloseRequested.connect(self.__on_close_tab)

        self.__tabview = tabview
    
    def create_new_tab(self, url=None, label="New Tab"):
        if url is None:
            url = QUrl('')
        elif type(url) is str:
            url = QUrl(url)
        else:
            if type(url) is not QUrl:
                raise Exception("Url should be a string or instance of QUrl")
        
        browser = QWebEngineView()
        browser.setUrl(url)
        index = self.__tabview.tabs.addTab(browser, label)
        self.__tabview.setCurrentIndex(i)

        browser.urlChanged.connect(lambda url, browser=browser: self.__update_url_bar(url, browser))
        browser.loadFinished.connect(lambda index=index, browser=browser: self.__update_load_finished(index, browser))

    def __update_load_finished(self, index, browser):
        self.__tabview.setTabText(index, browser.page().title())

    def __update_url_bar(self, url, browser):
        if browser != self.__tabview.currentWidget():
            return
        
        # TODO: Update window http icon

        self.__urlbar.setText(q.toString())
        self.__urlbar.setCursorPosition(0)
    
    def __on_add_tab(self, i):
        if i==-1:
            self.create_new_tab()
    
    def __on_tab_changed(self,i):
        browser = self.tabls.currentWidget()
        self.__update_url_bar(browser.url(), browser)
        self.__window.setWindowTitle(browser.page().title())

    def __on_close_tab(self, i):
        if self.__tabview.count() < 2:
            return
        self.__tabview.removeTab(i)

    def get_widget(self):
        return self.__tabview
    
    def get_current_browser(self):
        return self.__tabview.currentWidget()

    def nav_forward(self):
        self.__tabview.currentWidget().back()
    
    def nav_backward(self):
        self.__tabview.currentWidget().forward()
    
    def nav_reload(self):
        self.__tabview.currentWidget().reload()

    def nav_home(self):
        self.__tabview.currentWidget().setUrl(QUrl("http://www.google.com"))
    
    def navigate_to_url(self, url):
        q = QUrl(url)
        if q.scheme() == "":
            q.setScheme("http")

        self.__tabview.currentWidget().setUrl(q)

    def stop_load(self):
        self.__tabview.currentWidget().stop()

    def open_file(self, filename):
        if type(filename) is not str:
            raise Exception("Filename must be a string")
        
        with open(filename, 'r') as f:
            html = f.read()
        
        self.__tabview.currentWidget().setHtml(html)
        self.__urlbar.setText(filename)

    def print_page(self):
        dlg = QPrintPreviewDialog()
        dlg.paintRequested.connect(self.tabview.currentWidget().print_)
        dlg.exec_()



class BrowserControlProvider:
    """
    This class provides various navigation controls required by 
    a basic browser window: Print, Save etc
    """
    def __init__(self, window):
        if not issubclass(type(window), QMainWindow):
            raise Exception("window object must be of type QMainWindow")

        self.__window = window

    def open_file(self):
        filename, _ = filename, _ = QFileDialog.getOpenFileName(self.window, "Open file", "",
                                                  "Hypertext Markup Language (*.htm *.html);;"
                                                  "All files (*.*)")

    def save_file(self, file_data):
        filename, _ = QFileDialog.getSaveFileName(self.window, "Save Page As", "",
                                                  "Hypertext Markup Language (*.htm *html);;"
                                                  "All files (*.*)")
        with open(filename, 'w') as f:
            f.write(file_data.encode('utf8'))    



