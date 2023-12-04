def copy_file(command: str) -> None:
    user_command, user_file, copy_user_file = command.split(" ")
    if user_command == "cp":
        with (open(user_file, "r") as file_in,
              open(copy_user_file, "w") as file_out):
            if user_file != copy_user_file:
                file_out.write(file_in.read())
