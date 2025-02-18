from app.errors import CommandLineError


def copy_file(command: str) -> None:
    command_input = command.split()
    if len(command_input) != 3 or command_input[0] != "cp":
        raise CommandLineError("Command line is incorrect.")
    command_line, original_file, new_file = command_input

    if original_file != new_file:
        with (open(original_file) as file_in,
              open(new_file, "w") as file_out):
            file_out.write(file_in.read())
            print("The file successfully copied")
