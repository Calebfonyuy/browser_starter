from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

from widgets.buttons import ButtonProvider
from actions.browser_actions import *

import os
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        self.urlbar = QLineEdit()

        bprovider = BrowserProvider(self,self.urlbar)
        cprovider = ControlProvider(self,bprovider)
        self.bprovider = bprovider
        self.cprovider = cprovider
        
        self.setCentralWidget(bprovider.get_widget())

        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(16, 16))
        self.addToolBar(navtb)
        
        btn_source = ButtonProvider(self)

        back_btn = btn_source.get_back_button(bprovider.nav_backward)
        navtb.addAction(back_btn)

        next_btn = btn_source.get_next_button(bprovider.nav_forward)
        navtb.addAction(next_btn)

        reload_btn = btn_source.get_reload_button(bprovider.nav_reload)
        navtb.addAction(reload_btn)

        home_btn = btn_source.get_home_button(bprovider.nav_home)
        navtb.addAction(home_btn)

        navtb.addSeparator()

        self.httpsicon = QLabel()  # Yes, really!
        self.httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-nossl.png')))
        navtb.addWidget(self.httpsicon)

        navtb.addWidget(self.urlbar)

        stop_btn = btn_source.get_stop_button(bprovider.stop_load)
        navtb.addAction(stop_btn)

        # Uncomment to disable native menubar on Mac
        # self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu("&File")

        new_tab_action = btn_source.get_ntab_button(bprovider.create_new_tab)
        file_menu.addAction(new_tab_action)

        open_file_action = btn_source.get_ofile_button(cprovider.open_file)
        file_menu.addAction(open_file_action)

        save_file_action = btn_source.get_save_button(cprovider.save_file)
        file_menu.addAction(save_file_action)

        print_action = btn_source.get_print_button(cprovider.print_page)
        file_menu.addAction(print_action)

        self.setWindowIcon(QIcon(os.path.join('images', 'ma-icon-64.png')))

