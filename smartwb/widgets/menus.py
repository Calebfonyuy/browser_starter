from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtCore import QObject

from actions.browser_actions import BrowserProvider, ControlProvider
from widgets.buttons import ButtonProvider


class MenuProvider:
    """
    This class creates and returns menu items for a
    pyqt5 GUI
    
    The slot parameter requested by factory methods 
    refers to the pyqt slot to which it button will
    be connected
    """
    def __init__(self, browser_provider, control_provider, menubar, parent):
        if type(browser_provider) is not BrowserProvider:
            raise Exception("browser_provider must be an instance of BrowserProvider")

        if type(control_provider) is not ControlProvider:
            raise Exception("browser_provider must be an instance of ControlProvider")

        if type(menubar) is not QMenuBar:
            raise Exception("browser_provider must be an instance of QMenuBar")

        if not issubclass(type(parent) , QObject):
            raise Exception("Parent attribute must be subclass of QtObject")

        self.__bprovider = browser_provider
        self.__cprovider = control_provider
        self.__menubar = menubar
        self.__btn_source = ButtonProvider(parent)
    
    def create_all_menus(self):
        self.create_browser_menu()
        self.create_file_menu()
        self.create_bookmark_menu()
        self.create_history_menu()
        self.create_user_menu()
        self.create_help_menu()

    def create_file_menu(self):
        file_menu = self.__menubar.addMenu("&File")

        open_file_action = self.__btn_source.get_ofile_button(self.__cprovider.open_file)
        file_menu.addAction(open_file_action)

        save_file_action = self.__btn_source.get_save_button(self.__cprovider.save_file)
        file_menu.addAction(save_file_action)

        print_action = self.__btn_source.get_print_button(self.__cprovider.print_page)
        file_menu.addAction(print_action)
    
    def create_help_menu(self):
        help_menu = self.__menubar.addMenu("&Help")

        help_btn = self.__btn_source.get_help_button()
        help_menu.addAction(help_btn)

        about_btn = self.__btn_source.get_about_button()
        help_menu.addAction(about_btn)
    
    def create_bookmark_menu(self):
        bmk_menu = self.__menubar.addMenu("&Bookmarks")

        bmk_btn = self.__btn_source.get_bookmark_button(self.__bprovider.bookmark_page)
        bmk_menu.addAction(bmk_btn)

        bmk_lbtn = self.__btn_source.get_list_bookmark_button(self.__cprovider.show_bookmarks)
        bmk_menu.addAction(bmk_lbtn)

        bmk_ubtn = self.__btn_source.get_user_bookmark_button()
        bmk_menu.addAction(bmk_ubtn)

        bmk_fbtn = self.__btn_source.get_bookmark_folder_button(self.__cprovider.show_bookmarks)
        bmk_menu.addAction(bmk_fbtn)

        bmk_menu.addSeparator()

        addfav_btn = self.__btn_source.get_add_favorites_button(self.__bprovider.add_favourite_page)
        bmk_menu.addAction(addfav_btn)

        fav_btn = self.__btn_source.get_favorites_button(self.__cprovider.show_favourites)
        bmk_menu.addAction(fav_btn)


    def create_history_menu(self):
        hist_menu = self.__menubar.addMenu("&History")

        list_btn = self.__btn_source.get_history_button(self.__cprovider.show_history)
        hist_menu.addAction(list_btn)

    def create_user_menu(self):
        usr_menu = self.__menubar.addMenu("&User")

        user_btn = self.__btn_source.get_user_button()
        usr_menu.addAction(user_btn)

        login_btn = self.__btn_source.get_login_button()
        usr_menu.addAction(login_btn)

        logout_btn = self.__btn_source.get_logout_button()
        usr_menu.addAction(logout_btn)

    def create_browser_menu(self):
        tabs_menu = self.__menubar.addMenu("&Browser")

        new_tab_action = self.__btn_source.get_ntab_button(self.__bprovider.create_new_tab)
        tabs_menu.addAction(new_tab_action)
