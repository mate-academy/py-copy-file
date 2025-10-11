import os.path


def copy_file(command: str) -> None:
    divided_command = command.split()
    if not divided_command:
        return
    user_command = divided_command[0]

    if user_command == "cp" and len(divided_command) == 3:
        source_filename = divided_command[1]
        target_filename = divided_command[2]
        if source_filename == target_filename:
            return

        if not os.path.isfile(source_filename):
            return

        with (open(source_filename, "r") as file_in,
              open(target_filename, "w") as file_out):
            file_out.write(file_in.read())
