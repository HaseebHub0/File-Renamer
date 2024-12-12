import os
import logging

# Configure logging to track renamed files
logging.basicConfig(filename='renamed_files.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def check_directory(directory):
    """Check if the given directory exists and is a valid directory."""
    if not os.path.exists(directory):
        print(f"Error: The directory {directory} does not exist.")
        return False
    elif not os.path.isdir(directory):
        print(f"Error: The path {directory} is not a valid directory.")
        return False
    return True

def bulk_rename_files(directory, prefix="New_"):
    """Bulk rename files in the specified directory."""
    try:
        # Step 1: Validate the directory path
        if not check_directory(directory):
            return
        
        # Step 2: List all files in the directory
        files = os.listdir(directory)
        
        # Step 3: Process each file
        renamed_files = []  # List to keep track of renamed files
        for filename in files:
            file_path = os.path.join(directory, filename)
            
            # Step 4: Skip directories and only process files
            if os.path.isfile(file_path):
                new_name = prefix + filename
                new_file_path = os.path.join(directory, new_name)
                
                # Step 5: Rename the file
                os.rename(file_path, new_file_path)
                renamed_files.append((filename, new_name))
                logging.info(f"Renamed: {filename} -> {new_name}")
                print(f"Renamed: {filename} -> {new_name}")
        
        # Step 6: Check if any files were renamed
        if not renamed_files:
            print("No files were renamed. Make sure the directory contains valid files.")
        else:
            print(f"\nRenaming completed. {len(renamed_files)} files were renamed.\n")
            print("Renamed files:")
            for old_name, new_name in renamed_files:
                print(f"{old_name} -> {new_name}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def get_user_input():
    """Get directory path and prefix from the user."""
    print("Welcome to the Bulk File Renamer!")
    
    # Get directory path from user
    directory = input("Enter the directory path where your files are located: ")
    
    # Ensure valid directory path is provided
    while not check_directory(directory):
        directory = input("Please enter a valid directory path: ")
    
    # Get file name prefix from user
    prefix = input("Enter the prefix you want to add to the files (default 'New_'): ")
    if not prefix:
        prefix = "New_"
    
    return directory, prefix

def main():
    """Main function to execute the program."""
    # Step 1: Get user input for directory and prefix
    directory, prefix = get_user_input()

    # Step 2: Call the bulk rename function
    bulk_rename_files(directory, prefix)

if __name__ == "__main__":
    main()
