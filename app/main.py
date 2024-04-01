import shutil


def copy_file(command: str) -> None:
    copied_file = new_file = None
    try:
        cp, copied_file, new_file = command.split()

        if cp == "cp" and copied_file != new_file:
            shutil.copyfile(copied_file, new_file)
    except FileNotFoundError:
        print(f"Error: One of the files '{copied_file}' or '{new_file}' does not exist.")
    except ValueError:
        print("Error: Command format is incorrect. Expected format: 'cp <source> <destination>'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
