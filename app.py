from inventory.back import create_table
from inventory.front import window


def __main() -> None:
    create_table()
    window.mainloop()


if __name__ == '__main__':
    __main()
