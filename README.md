# Python-Week-Four-Assignment
📂 File Read & Write Challenge with Error Handling (Python)
📖 Overview

This Python program demonstrates file handling operations with error handling.
It shows how to:

Create and write to a file (w mode).

Append new content to the same file (a mode).

Read the content of a file (r mode).

Handle errors gracefully (e.g., missing or restricted files).

Generate a modified file where the content is converted to uppercase.

The project is designed to help beginners understand safe file operations in Python.

⚙️ How It Works

The program first creates a text file named myFile.txt and writes some content to it.

It then appends additional lines to the file.

The user is prompted to enter a filename to read.

If the correct filename (myFile.txt) is entered, the program reads and displays its content.

If the wrong filename is entered, an error message is shown.

The program also creates a new file called modified_myFile.txt, containing the uppercase version of the original file’s content.

🖥️ Example Run
✅ Correct Filename
✅ File of text type was created and written in 'w' mode.
✅ Extra two lines were added in 'a' mode to the file.

Enter the filename to read: myFile.txt

✅ File found! Here is its content:

This is Python programming.
The topic today was File Handling
After the class, the tutor gave us an assignment.
We need to complete the assignment by Tuesday next week.

✅ File processed successfully! Modified content saved as modified_myFile.txt

❌ Wrong Filename
Enter the filename to read: wrongname.txt
❌ Error: The file does not exist. Please check the filename and try again.
