import sys
from PyQt5.QtWidgets import QApplication
from browser import MainWindow


class Launcher:
    """
    This class simply launches the app
    """
    def __init__(self):
        app = QApplication(sys.argv)
        app.setStyle('Oxygen')
        app.setApplicationName("SmartWB")
        app.setOrganizationName("SmartWB")
        app.setOrganizationDomain("SmartWB.org")
        # Launch the application window
        self.__setup_main_application()
        # Start the main application
        app.exec_()
        
    def __setup_main_application(self):
        window = MainWindow()
        window.setWindowTitle('SmartWB')
        window.show()


if __name__ == "__main__":
    Launcher()
