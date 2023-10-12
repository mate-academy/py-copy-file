def copy_file(command: str) -> None:
    time_result = command.split(" ")
    if time_result[0] == "cp" and len(time_result) == 3:
        with (open(time_result[1], "r") as current_file,
              open(time_result[2], "w+") as new):
            content = current_file.read()
            new.write(content)
