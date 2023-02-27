def copy_file(command: str) -> None:
    cp, current_file, copied_file = command.split()
    if cp != "cp":
        return
    with (open(f"{current_file}.txt", "r") as file_to_copy,
          open(f"{copied_file}.txt", "w") as file_result):
        file_result.write(file_to_copy.read())
