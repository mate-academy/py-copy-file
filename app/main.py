def copy_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) != 3 or command_list[0] != "cp":
        print("Something wrong. "
              "Command example: "
              "'cp old_file.txt new_file.txt'")
        return

    if command_list[1].lower() == command_list[2].lower():
        print("Can't save a new file with the same name as input file."
              " Does nothing")
        return

    try:
        with (open(command_list[1], "r") as file_in,
              open(command_list[2], "w") as file_out):
            file_out.write(file_in.read())
    except Exception:
        print(Exception)
        raise
    else:
        print(f"Created file {command_list[2]} "
              f"with content of {command_list[1]}")


if __name__ == "__main__":
    copy_file("Hello world")
    copy_file("cp world world")
    copy_file("cp hello_world.txt test_hello.txt")
