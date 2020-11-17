#test of a browsing button, whitman spitzer 11/17/2020

import PySimpleGUI as sg 
import os.path

browse_file_column = [
    [
        sg.Text("FILE WINDOW"),
        sg.In(size=(50,2), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox
        (
            values=[], enable_events=True, size=(80, 40), key="-FILE LIST-"
        )
    ],
]
layout = [[sg.Column(browse_file_column)]]
window = sg.Window("File Browser", layout)

while True:
    event, values = window.read()
    if event=="EXIT" or event==sg.WIN_CLOSED:
        break