from Voting_Logic import *


def main():
    app = QApplication([])
    window = Vote()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()