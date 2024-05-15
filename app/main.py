def copy_file(file_name: str) -> None:
    words_of_file_name = file_name.split()
    if len(words_of_file_name) > 1:
        old_file_name = words_of_file_name[1]
        new_file_name = words_of_file_name[2]
        if not old_file_name == new_file_name:
            with (open(old_file_name, "r") as read_file,
                  open(new_file_name, "w") as writ_file):
                for line in read_file:
                    writ_file.write(line)
