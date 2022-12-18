# write your code here
def copy_file(command: str) -> None:
     first_name, second_name = command.split()



    if first_name != second_name:

        with open(first_name, "r") as file_in, \
                open(second_name, "w") as file_out:
            file_out.write(file_in.read())
