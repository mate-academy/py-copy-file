def parse_command(command):
    splitted = command.split()
    return {'command': splitted[0], 'file': splitted[1], "copy_file": splitted[2]}


def copy_file(command):
    parsed_command = parse_command(command)
    if parsed_command['file'] != parsed_command['copy_file']:
        with open(parsed_command['file'], mode='r') as fin:
            with open(parsed_command['copy_file'], mode='w') as fout:
                for line in fin:
                    fout.write(line)
