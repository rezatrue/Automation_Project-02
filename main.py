# This is a sample Python script.
from base import Base
from gui import Gui
from registerUser import RegisterUser


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi I\'m , {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # Gui(Base())

    registerUser = RegisterUser()
    registerUser.verifyPageIsvisible()
    registerUser.verifyNewUserSignUp()
    registerUser.verifyAccountInformation()
    registerUser.verifyAccountInformationFormSubimision()
    registerUser.deleteAccount()
    registerUser.closeBrowser()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Stating Selenium Python Project by the Name of Allah')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/