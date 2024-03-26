def copy_file(command: str) -> None:
    command, name_in, name_out = command.split()
    if command != "cp":
        print("I don't know this command")
    if name_in != name_out:
        with (open(name_in, "r") as file_in,
              open(name_out, "w") as file_out):
            file_out.write(file_in.read())
