def copy_file(command: str) -> None:
    names_files = command.split()

    if len(names_files) != 3:
        return

    if names_files[1] == names_files[2]:
        print("Does nothing")
        return

    with (open(names_files[1], "r") as file_in,
          open(names_files[2], "w") as file_out):
        text = file_in.read()
        file_out.write(text)
