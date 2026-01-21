def copy_file(commands: str) -> None:
    parts = commands.split(" ")
    if len(parts) == 3 and parts[0] == "cp":
        try:
            course_file = parts[1]
            dei_file = parts[2]
            with (open(course_file, "r") as file1,
                  open(dei_file, "w") as file2):
                for line in file1:
                    file2.write(line)
        except FileNotFoundError:
            return
    else:
        return
