def copy_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 or command[0] != "cp":
        print("You need to include 'cp' ")
        return
    _, file_name, new_file_name = command
    if file_name != new_file_name:
        with (open(file_name, "r") as file_in,
              open(new_file_name, "w") as file_out):
            file_out.write(file_in.read())
