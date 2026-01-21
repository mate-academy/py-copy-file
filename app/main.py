# write your code here
def copy_file(command: str) -> None:

    try:
        file_list = command.split(" ")
        if file_list[0] != "cp" or len(file_list) != 3:
            print("Wrong command use cp filename1 filename2!")
            return
        if file_list[1] == file_list[2]:
            print("filename1 filename2 are the same!")
            return
        else:
            original_f = file_list[1]
            copy_f = file_list[2]

            with open(original_f, "r") as original, open(copy_f, "w") as copy:
                copy.write(original.read())
    except FileNotFoundError:
        print("Error: The source file does not exist.")
