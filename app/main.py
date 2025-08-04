def copy_file(command: str) -> None:
    arr_command = command.split(" ")

    if len(arr_command) != 3 or arr_command[0] != "cp":
        print("Invalid command")
        return
    if arr_command[0] == arr_command[1]:
        print("Do nothing")
        return

    source_file = arr_command[1]
    destination_file = arr_command[2]

    try:
        with (open(source_file, "r") as source,
              open(destination_file, "w") as destination):
            destination.write(source.read())
    except FileNotFoundError:
        print("File not found")
