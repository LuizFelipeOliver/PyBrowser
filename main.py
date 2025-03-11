import tkinter
from Url import URL
from Browser import Browser

if __name__ == "__main__":
    import sys
    Browser().load(URL(sys.argv[1]))
    tkinter.mainloop()

