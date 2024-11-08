import os
# Deletes Unessecary Files From Video/Audio Directory
def delete_files(file1, file2):
    print("Deleting Files...")
    for file_path in [file1, file2]:
        try:
                os.remove(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")