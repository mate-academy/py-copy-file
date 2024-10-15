import shutil


def copy_file(source_file: str, destination_file: str) -> None:
    try:
        shutil.copy(source_file, destination_file)
        print(f"File copied from {source_file} to {destination_file}")
    except FileNotFoundError:
        print(f"Error: {source_file} not found.")
    except PermissionError:
        print(f"Error: Permission denied while copying to {destination_file}.")
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    source_file = input("Enter the path of the source file: ")
    destination_file = input("Enter the name/path for the destination file: ")
    copy_file(source_file, destination_file)
