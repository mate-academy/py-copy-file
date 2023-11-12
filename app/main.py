def copy_file(command: str) -> None:
    temp_arr = command.split()
    if len(temp_arr) == 3 and temp_arr[1] != temp_arr[2]:
        with (open(temp_arr[1], "r") as source, open(temp_arr[2], "w") as copied_file):
            copied_file.write(source.read())
