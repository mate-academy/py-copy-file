def copy_file(command: str) -> str:
    command = command.split()
    if command[0] != "cp":
        return "the file does not contain 'cp'"
    elif len(command) != 3:
        return "must have three arguments"
    file_in, file_out, *_ = command

    if file_in == file_out:
        return "cannot be copied to the same file"

    with (open(f"{file_in}", "r") as file,
          open(f"{file_out}", "w") as new_file):
        new_file.write(file.read())
