from tkinter import Tk
from inventory.front import LibraryGUI


def __main() -> None:
    root_window = Tk()
    LibraryGUI(root_window)
    root_window.mainloop()


if __name__ == '__main__':
    __main()
