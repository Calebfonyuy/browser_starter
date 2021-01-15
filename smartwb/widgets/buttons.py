import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon

image_location = "./images"


class ButtonProvider:
    """
    This class produces and returns buttons for a 
    PyQt GUI equiped with a browser widget.
    
    The slot parameter requested by factory methods 
    refers to the pyqt slot to which it button will
    be connected
    """
    def __init__(self, parent):
        if not issubclass(type(parent) , QObject):
            raise Exception("Parent attribute must be subclass of QtObject")
        self.parent = parent
        
    def get_button(self, icon, label, tip="", slot=None):
        if type(icon) is not QIcon:
            raise Exception("Icon must be an instance of QIcon")
        if type(label) is not str:
            raise Exception("Label Must be a string")
        
        btn = QAction(icon, label, self.parent)
        btn.setStatusTip(tip)
        if slot is not None:
            btn.triggered.connect(slot)
        
        return btn
    
    def get_back_button(self, slot=None):
        return self.get_button(
            QIcon(os.path.join(image_location, 'arrow-180.png')),
            "Back",
            "Back to previous page",
            slot
        )
    
    def get_next_button(self, slot=None):
        return self.get_button(
            QIcon(os.path.join(image_location, 'arrow-000.png')),
            "Forward",
            "Forward to next page",
            slot
        )
    
    def get_reload_button(self, slot=None):
        return self.get_button(
            QIcon(os.path.join(image_location, 'arrow-circle-315.png')),
            "Reload",
            "Reload page",
            slot
        )
    
    def get_home_button(self, slot=None):
        return self.get_button(
            QIcon(os.path.join(image_location, 'home.png')),
            "Home",
            "Go to Home page",
            slot
        )
    
    def get_stop_button(self, slot=None):
        return self.get_button(
            QIcon(os.path.join(image_location, 'cross-circle.png')),
            "Stop",
            "Stop loading page",
            slot
        )
    
    def get_ntab_button(self, slot=None):
        return self.get_button(
            QIcon(os.path.join(image_location, 'ui-tab--plus.png')),
            "New Tab",
            "Open a new tab",
            slot
        )
    
    def get_ofile_button(self, slot=None):
        return self.get_button(
            QIcon(os.path.join(image_location, 'disk--arrow.png')),
            "Open File",
            "Open from file",
            slot
        )
    
    def get_save_button(self, slot=None):
        return self.get_button(
            QIcon(os.path.join(image_location, 'disk--pencil.png')),
            "Save Page As...",
            "Save current page to file",
            slot
        )
    
    def get_print_button(self, slot=None):
        return self.get_button(
            QIcon(os.path.join(image_location, 'printer.png')),
            "Print",
            "Print current page",
            slot
        )
