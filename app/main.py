import os


def get_full_path(file_name: str) -> str:
    dir_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(dir_path, file_name)


def copy_file(command: str) -> None:
    arguments = command.split(" ")
    if (arguments[1] != arguments[2]):
        with (open(get_full_path(arguments[1]), "r")
              as file_in, open(get_full_path(arguments[2]), "w") as file_out):
            if (file_in.name != file_out.name):
                content = file_in.read()
                file_out.write(content)
