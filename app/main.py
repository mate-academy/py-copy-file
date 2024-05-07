def copy_file(command: str) -> None:
    new_list = command.split(" ")
    if len(new_list) != 3:
        return
    old_name, new_name = new_list[1:]

    if old_name == new_name:
        return

    with (open(f"{old_name}", "r") as file_in,
          open(f"{new_name}", "w") as file_out):
        content = file_in.read()
        file_out.write(content)
