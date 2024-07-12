from app.errors import CommandLineError


def copy_file(command: str) -> None:

    if len(command.split(" ")) != 3 or command.split(" ")[0] != "cp":
        raise CommandLineError("Command line is incorrect.")

    command_line, original_file, new_file = command.split(" ")

    if original_file != new_file:
        with (open(original_file) as file_in,
              open(new_file, "w") as file_out):
            file_out.write(file_in.read())
            print("The file successfully copied")
