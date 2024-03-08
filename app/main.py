def copy_file(command: str) -> None:
    list_of_words = command.split()
    if len(list_of_words) != 3:
        print("Invalid command format. Please provide exactly 3 arguments.")
        return

    source_file, destination_file = list_of_words[1:]
    if list_of_words[0] != "mv":
        return
    if source_file == destination_file:
        return
    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):
        file_out.write(file_in.read())
