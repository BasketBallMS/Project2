from PyQt6.QtWidgets import QMainWindow,QApplication
from Project2 import Ui_MainWindow


class Vote(QMainWindow, Ui_MainWindow):
    """
    A class representing a basic voting registration
    """
    def __init__(self)->None:
        """
        Initializes a Vote object with default values
        """
        super().__init__()
        self.__voting_list = []
        self.__voting_dictionary = {'Jane': 0, 'John': 0}

        self.setupUi(self)
        self.save.clicked.connect(lambda: self.vote_id())

    def vote_id(self)-> int | None:
        """
        Check for valid ID and if the ID has voted
        :return: Vote_ID
        """
        try:
            Vote_ID = int(self.Vote_ID.toPlainText().strip())
            if Vote_ID not in self.__voting_list:
                self.__voting_list.append(Vote_ID)
                self.person_voted_for(Vote_ID)
            else:
                self.Submitted_Label.setText('You already Voted')
                self.Submitted_Label.setStyleSheet('color: red')
                self.clear_answer()
                return None

        except ValueError:
            self.Submitted_Label.setText("Invalid Voting ID")
            self.Submitted_Label.setStyleSheet("color: red;")
            self.clear_answer()
            return None
        return Vote_ID

    def person_voted_for(self,Vote_ID)->None:
        """
        Marks which candidate the Voter voted for and writes it into c csv file
        :param Vote_ID:
        """
        try:
            if self.John.isChecked():
                self.__voting_dictionary['John'] += 1
                chosen = 'John'
            elif self.Jane.isChecked():
                self.__voting_dictionary['Jane'] += 1
                chosen = 'Jane'
            elif self.Fill_In_Button.isChecked():
                chosen = self.valid_vote()
            else:
             raise TypeError
        except TypeError:
            self.Submitted_Label.setText("Please Select an Option")
            self.Submitted_Label.setStyleSheet("color: red;")
            self.__voting_list.remove(Vote_ID)
            self.clear_answer()
            return


        with open('data.csv', 'a') as file:
            file.writelines(f'Voter {Vote_ID} voted for {chosen}\n')
        self.Submitted_Label.setText("Saved")
        self.Submitted_Label.setStyleSheet("color: green;")

        self.total_votes()

    def valid_vote(self)-> str | None:
        """
        Checks to see if the fill-in candidate is valid
        :return: Fill_Text
        """
        Fill_text = self.Fill_In_Text.toPlainText().strip()
        try:
            if Fill_text.isalpha():
                if Fill_text not in self.__voting_dictionary:
                    self.__voting_dictionary[Fill_text] = 1

                else:
                    self.__voting_dictionary[Fill_text] += 1
            else:
                raise ValueError
        except ValueError:
            self.Submitted_Label.setText("Invalid Fill IN")
            self.Submitted_Label.setStyleSheet("color: red;")
            self.clear_answer()
            return None
        return Fill_text

    def total_votes(self)->None:
        """
        Writes into a csv file how many votes each candidate got
        """
        with open('data.csv', 'a') as file:
            for names, votes in self.__voting_dictionary.items():
                file.writelines(f'{names} = {votes}' + " ")
            file.write('\n')
        self.clear_answer()

    def clear_answer(self)->None:
        """
        Clears the GUI once the vote is submitted
        """
        self.Vote_ID.clear()
        self.Fill_In_Text.clear()
        self.Candidates.setExclusive(False)
        for button in self.Candidates.buttons():
            button.setChecked(False)
        self.Candidates.setExclusive(True)









