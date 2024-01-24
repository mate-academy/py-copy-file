def copy_file() -> None:

    command = input("Enter command: ")
    parts = command.split()

    with (open(parts[1], "r") as file_origin,
          open(parts[2], "w") as file_copy):

        text = file_origin.read()

        while True:

            if parts[1] == parts[2]:
                print("Copy cannot have the same name!")
                break

            if len(parts) != 3 or parts[0] != "cp":
                print("Error: Invalid command format. "
                      "Please use 'cp file copy_file'")
                return

            file_copy.write(text)


if __name__ == "__main__":
    copy_file()
