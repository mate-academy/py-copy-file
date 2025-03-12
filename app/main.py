from os import path


def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        command_name, file_name_out, file_name_in = command.split()
        print(command_name, file_name_out, file_name_in)
        if command_name == "cp":
            if path.exists(file_name_out):
                if file_name_out != file_name_in:
                    with (
                        open(file_name_out, "r") as file_from,
                        open(file_name_in, "w") as file_to
                    ):
                        content = file_from.read()
                        file_to.write(content)
