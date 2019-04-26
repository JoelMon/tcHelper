#!/usr/bin/env python3.7
from PySide2.QtWidgets import QApplication
from PySide2 import QtGui
from PySide2.QtCore import QFile, QObject
from PySide2.QtUiTools import QUiLoader
from PySide2 import QtWidgets
from tchelperlib import Brother
import main_window
import database
import yam
import sys


def check_first_run():
    """Return *True* if it's the first time tcHelper runs.

    :return: Value for [APP] [first_time_running]
    :rtype: bool

    """

    return yam.getValue('first_run')


def set_first_run(value):
    """Sets the first_run value in config.ini

    Sets `False` in `[APP]: first_time_running` to mark that the tcHelper program has run before.

    :param value: The value to set *first_time_running*
    :type value: str

    """

    yam.setValue('first_run', value)


def set_database_location(location):
    """Sets the location of the database in config.ini

    :param location: The location of the database
    :type location: str
    :return:

    """

    yam.setValue('db_location', location)


def main():
    """Entry point for the tcHelper program."""

    if check_first_run():
        # Show the Save File QFileDialog
        QtWidgets.QApplication()
        file_name = QtWidgets.QFileDialog.getSaveFileName(None,
                                                          "Save New Database",
                                                          "New_Database.tcd",
                                                          "tcHelper Database *.tcd")

        # If user doesn't doesn't enter a file name then print message
        if file_name == '':
            print('Please run tcHelper again and select a location to save the database')
            quit()

        set_database_location(file_name[0])
        set_first_run(False)

        db = database.DB()
        db.initDB()

        main_window.run()

    else:
        main_window.run()


if __name__ == '__main__':
    main()
