# Bulk File Renamer

This program allows you to bulk rename files in a specified directory by adding a prefix to each file. It logs the renaming process and can be used to easily rename multiple files at once.

## Features:
- **Bulk Rename**: Adds a specified prefix to all files in a given directory.
- **Error Handling**: Validates if the directory exists and contains files.
- **Logging**: Keeps a log of all renamed files with timestamps for tracking purposes.
- **Interactive Interface**: Prompts the user to input the directory path and prefix for the renaming process.

## Requirements:
- Python 3.x

## Installation:

1. Install Python 3.x from [here](https://www.python.org/downloads/).

## Usage:

### 1. Run the Program:
   - Run the script `bulk_file_renamer.py` in your terminal or command prompt.
   - The program will prompt you to enter the directory path where your files are located.
   - It will also ask you for a prefix to add to the files. If no prefix is provided, the default prefix is `New_`.

### 2. Example:
```bash
Enter the directory path where your files are located: /path/to/your/directory
Enter the prefix you want to add to the files (default 'New_'): MyPrefix_
