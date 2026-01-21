from os.path import isfile


def copy_file(command: str) -> None:
    if len(command.split(" ")) == 3:

        copy, file_to_copy, copied_file = command.split(" ")
        if (file_to_copy != copied_file and copy == "cp"
                and isfile(file_to_copy)):

            with (open(file_to_copy, "r")
                  as file_in, open(copied_file, "w") as file_out):
                for line in file_in:
                    file_out.write(line)
        else:
            print("Invalid command")
    else:
        print("Invalid command")
