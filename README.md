# FindErase
A Python Command Line  Tool for locating Files and Folders and optionally Erasing or Renaming Them

## Introduction

The Folder Search and Delete Tool is a Python script that allows you to search for and optionally delete specified folders or files within a directory. It is a versatile utility that can help you quickly locate specific folders and, if needed, remove them from your file system.

## Usage

To use the Folder Search and Delete Tool, follow these steps:

1. **Installation:**

   There's no need for installation as it's a standalone Python script. However, make sure you have Python installed on your system.

2. **Running the Script:**

   Open your command-line terminal and navigate to the directory where you have saved the FINDERASE folder then run the `main.py` script.

   To search for a specific folder within the current directory, use the following command:

   ```bash
   python main.py  folder_name_to_search

3. **Alternatively**
   Let's make the script executable 
   

   Add this shebang line to finderase.py. Alter to point to your usr bin

   ```bash
   #!/usr/bin/env python3
   
   Make the script executable

   ```bash
   chmod +x finderase.py
   ```

   Run the script
   
   ```bash
   ./finderase.py folder_name


You can create a symbolic link (symlink) to make your Python script executable from anywhere in your system. To do this, follow these steps:

    Navigate to a directory that is in your system's PATH. Common directories for user-specific scripts include ~/bin or ~/.local/bin. If you don't have these directories, you can create one. For this example, let's create a bin directory in your home folder:

    bash

mkdir -p ~/bin

Move your Python script to this directory or create a symlink in this directory. For example, let's create a symlink to myscript.py:

bash

ln -s /path/to/your/script/myscript.py ~/bin/myscript

Replace /path/to/your/script/ with the actual path to your Python script, and myscript is the name of the symlink in your ~/bin directory.

Make sure that the bin directory is in your PATH. You can add the following line to your ~/.bashrc or ~/.zshrc file to include the bin directory in your PATH. Replace ~/.local/bin with the actual path to your bin directory:

bash

export PATH="$HOME/.local/bin:$PATH"

Then, refresh your terminal or run:

bash

source ~/.bashrc  # or source ~/.zshrc if you use Zsh

You can now run your Python script from anywhere in the terminal by simply typing its name:

bash

    myscript

    The symlink allows you to execute the script as if it were in your PATH. Make sure the symlink name does not conflict with any existing system command or application.

This method allows you to create a symlink to your Python script, making it easily executable from anywhere in your system.
ChatGPT can make mistakes. Consider checking important information.


