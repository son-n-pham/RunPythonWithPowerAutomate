import os
import time

def scan_folder(folder):
    """
    Scan a folder, return a list of items and a list of items' paths in the folder
    """

    items = list(os.scandir(folder))
    items_path = [item.path for item in items]
    return items, items_path

def do_something(new_files, folder_path):
    """
    Do something
    """
    for file in new_files:
        # Create a new txt file with the name as the time that file is copied into with the extension of txt
        print(f'*** New file detected: {file.name} ***')
        file_name = os.path.splitext(file.name)[0]
        file_extension = os.path.splitext(file.name)[1]
        new_file_name = time.strftime("%Y%m%d-%H%M%S") + ".txt"
        new_file_path = os.path.join(folder_path, new_file_name)
        with open(new_file_path, "w") as f:
            f.write(file_name)
        print(f"New file created: {new_file_name}")

def monitor_folder(folder_path):
  
    print(f'Monitoring {folder_path} ...')

    # Get the initial state of the folder
    initial_state, initial_state_path = scan_folder(folder_path)

    while True:
        # Get the current state of the folder
        current_state, current_state_path = scan_folder(folder_path)

        # Check if there are any new files
        
        if len(current_state_path) != len(initial_state_path):
          new_files = [item for item in current_state if item.path not in initial_state_path]
        else:
          new_files = []

        if len(new_files) != 0:

            # Just do something with the new files
            do_something(new_files, folder_path)
          
            # Update the initial state of the folder
            initial_state, initial_state_path = scan_folder(folder_path)
            
        # Wait for 7 second before checking again
        time.sleep(7)
        print(f'Monitoring {folder_path} ...')

if __name__ == '__main__':
    monitor_folder('C:/development/RunPythonWithPowerAutomate/test_folder')