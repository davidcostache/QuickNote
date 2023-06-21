# QuickNote
QuickNote is a simple note-taking application built using the Tkinter library in Python. It provides a user-friendly graphical interface for creating, opening, saving, and deleting notes.

## Features
- Create a new note: Allows the user to start a new note by clearing the text area.
- Open an existing note: Enables the user to choose and open an existing note file.
- Save the current note: Saves the current note to a file, either by choosing a new filename or overwriting an existing file.
- Delete the current note: Offers the option to delete the current note after confirming with the user.
- Prompt to save changes: Checks if there are unsaved changes before performing an action and prompts the user to save the note.
- Graceful exit: Checks if there are unsaved changes before closing the application and gives the option to save before exiting.

## Usage
1. Launch the QuickNote application.
2. Create a new note: Select "New Note" from the "File" menu or press Ctrl+N.
3. Open an existing note: Select "Open Note" from the "File" menu or press Ctrl+O. Choose the note file to open.
4. Save the current note: Select "Save Note" from the "File" menu or press Ctrl+S. Choose a new filename or overwrite an existing file.
5. Delete the current note: Select "Delete Note" from the "File" menu or press Ctrl+D. Confirm the deletion when prompted.
6. Prompt to save changes: QuickNote will prompt to save changes if there are any unsaved changes before performing an action.
7. Graceful exit: Click the close button or select "Exit" from the "File" menu or press Ctrl+Q. QuickNote will check for unsaved changes and prompt to save before exiting.

## Installation
To run the QuickNote application, perform the following steps:

1. Clone the repository:
```
git clone https://github.com/davidcostache/QuickNote/
```
2. Install the required dependencies (if not already installed):
```
pip install tkinter
```
3. Run the application:
```python
python main.py
```

## License
QuickNote is licensed under the MIT License. You can find detailed license information in the [LICENSE](LICENSE) file.

## Acknowledgments
- The application utilizes the Tkinter library for creating the graphical user interface.
- The application icon was sourced from [Flaticon](https://www.flaticon.com/free-icon/pencil_3075770?term=note&page=1&position=39&origin=search&related_id=3075770).



