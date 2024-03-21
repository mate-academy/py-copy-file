def copy_file(command: str) -> None:
    list_of_words = command.split()
    if len(list_of_words) != 3:
        raise Exception("Invalid command format. Please provide exactly 3 arguments.")

    command, source_file, destination_file = list_of_words
    if command != "mv":
        raise Exception("Invalid command format. Please provide exactly")
    if source_file == destination_file:
        raise Exception("Invalid names. Please provide exactly")
    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):
        file_out.write(file_in.read())
