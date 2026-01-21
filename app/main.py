def copy_file(input_str: str) -> None:
    command_list: list = input_str.split()
    if len(command_list) == 3:
        command, file_name, new_file_name = input_str.split()
    if command == "cp" and file_name != new_file_name:
        with (open(file_name, "r") as file,
              open(new_file_name, "w") as new_file):
            new_file.write(file.read())


if __name__ == "__main__":
    copy_file("cp main.py main1.py")
