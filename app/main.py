def copy_file(command: str) -> None:
    target_file, new_file = command.split()[1:]
    if target_file == new_file:
        return

    with open(target_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())


if __name__ == "__main__":
    copy_file(input(
        "Write a command with arguments "
        "[target_file, new_file] :"
    ))
