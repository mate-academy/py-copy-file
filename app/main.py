# write your code here
def copy_file(command: str) -> None:
    command_word = command.split(" ")
    if command_word[0] != "cp":
        raise ValueError("Invalid command")
    if len(command_word) != 3:
        raise ValueError("Command should has 3 words")
    with (open(command_word[1], "r") as file_in,
          open(command_word[2], "w") as file_out):
        file_out.write(file_in.read())
