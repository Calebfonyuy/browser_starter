

class TabBarPlus(QTabBar):
    """Tab bar that has a plus button floating to the right of the tabs."""
    plusClicked = QtCore.Signal()

    def __init__(self):
        super().__init__()

        # Plus Button
        self.plusButton = QPushButton("+")
        self.plusButton.setParent(self)
        self.plusButton.setFixedSize(20, 20)  # Small Fixed size
        self.plusButton.clicked.connect(self.plusClicked.emit)
        self.movePlusButton() # Move to the correct location
    # end Constructor

    def sizeHint(self):
        """Return the size of the TabBar with increased width for the plus button."""
        sizeHint = QTabBar.sizeHint(self) 
        width = sizeHint.width()
        height = sizeHint.height()
        return QtCore.QSize(width+25, height)
    # end tabSizeHint

    def resizeEvent(self, event):
        """Resize the widget and make sure the plus button is in the correct location."""
        super().resizeEvent(event)

        self.movePlusButton()
    # end resizeEvent

    def tabLayoutChange(self):
        """This virtual handler is called whenever the tab layout changes.
        If anything changes make sure the plus button is in the correct location.
        """
        super().tabLayoutChange()

        self.movePlusButton()
    # end tabLayoutChange

    def movePlusButton(self):
        """Move the plus button to the correct location."""
        # Find the width of all of the tabs
        size = sum([self.tabRect(i).width() for i in range(self.count())])
        # size = 0
        # for i in range(self.count()):
        #     size += self.tabRect(i).width()

        # Set the plus button location in a visible area
        h = self.geometry().top()
        w = self.width()
        if size > w: # Show just to the left of the scroll buttons
            self.plusButton.move(w-54, h)
        else:
            self.plusButton.move(size, h)