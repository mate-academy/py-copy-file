import shutil


def copy_file(command: str) -> None:
    try:
        instruction, file, new_file = command.split(" ")
        if instruction != "cp":
            print("Unsupported operation, try again!")
            return
        if file == new_file:
            return
        shutil.copyfile(file, new_file)
    except ValueError:
        print("Your command is incorrect")
    except FileNotFoundError as error:
        print(error)
