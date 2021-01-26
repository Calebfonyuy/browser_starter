from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# Imports for the main section meant for tests
import sys, os
import faker

def get_base_window(widget, title=""):
    window = QMainWindow()
    window.setCentralWidget(widget)
    window.setWindowTitle(title)
    return window


def get_list_view(items=[]):
    model = QStandardItemModel()
    for item in items:
        entry = QStandardItem(str(item))
        model.appendRow(entry)

    listv = QListView()
    listv.setModel(model)
    return listv


def get_list_window(items=[], win_title="", list_title=""):
    wlist = get_list_view(items)
    window = get_base_window(wlist)
    return window


if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle('Oxygen')
    app.setApplicationName("SmartWB")
    app.setOrganizationName("SmartWB")
    app.setOrganizationDomain("SmartWB.org")
    
    fake = faker.Faker()
    items = [fake.name() for i in range(20)]
    listv = get_list_view(items)
    window = get_base_window(listv, title="Custom window title")
    window.show()

    app.exec_()
