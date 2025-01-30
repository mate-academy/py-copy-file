# write your code here
def copy_file(command: str) -> None:
    command_word = command.split(" ")
    with (open(command_word[1], "r") as file_in,
          open(command_word[2], "w") as file_out):
        file_out.write(file_in.read())
