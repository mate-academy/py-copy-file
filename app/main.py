def copy_file(command: str) -> None:
    cmd, target_file, new_file = command.split()
    if cmd != "cp":
        raise ValueError("Command not found.")
    if not target_file:
        raise FileNotFoundError("File is not found."
                                f"No such file or directory '{target_file}'")
    if not new_file:
        raise ValueError("Name of copy_file is not found")
    if target_file != new_file:
        with (open(target_file, "r") as file_in,
              open(new_file, "w") as file_out):
            file_out.write(file_in.read())


if __name__ == "__main__":
    copy_file(input(
        "Write a command with arguments "
        "[target_file, new_file] :"
    ))
