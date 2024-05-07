def copy_file(command: str) -> None:
    new_list = command.split(" ")
    old_name = new_list[1]
    new_name = new_list[2]

    if old_name == new_name:
        return

    with (open(f"{old_name}", "r") as file_in,
          open(f"{new_name}", "w") as file_out):
        content = file_in.read()
        file_out.write(content)
