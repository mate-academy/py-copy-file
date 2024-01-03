def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) == 3 and parts[0] == "cp":
        coping_file, orig_file = parts[1], parts[2]

        if coping_file != orig_file:
            with (open(coping_file, "r") as file_old,
                  open(orig_file, "w") as file_new):
                file_new.write(file_old.read())


copy_file("cp file.txt file.txt")

copy_file("cp file.txt new_file.txt")
open("file.txt").read() == open("new_file.txt").read()
