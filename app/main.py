def copy_file(command: str) -> None:
    command_list = command.split()

    if command_list[1] == command_list[2]:
        return

    if len(command_list) != 3 or "cp" != command_list[0]:
        print("there must be command 'cp', 'the file to clone',"
              " 'file to which we create and clone, or file where to copy'\n"
              "example: 'cp file.txt new_file.txt'")
        return

    with (open(command_list[1], "r") as file_in,
          open(command_list[2], "w") as file_out):
        text = file_in.read()
        file_out.write(text)
