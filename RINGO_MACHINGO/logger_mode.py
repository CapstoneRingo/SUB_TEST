# This script runs python in a logging mode, writing out each of your commands
# to a file.

# Open file to write out to
filename = raw_input("Name for log file (with extension): ")
loggerFile = open(filename,"w")
cmd_input = ''
prev_cmd = ''

# Logger loop
while(1):

    # Get next python command
    cmd_input = raw_input(">>")

    # Handle commands
    if cmd_input == 'exit':
        break # exit for loop
    elif len(cmd_input) > 0:
        if cmd_input[len(cmd_input)-1] == ':' or (len(cmd_input) > 0 and cmd_input[0] == '\t'):
            # add appropriate returns
            prev_cmd += cmd_input + ' \r'

    else:
        # execute command
        exec (cmd_input+prev_cmd)
        # write command out to file
        #loggerFile.write(cmd_input + ' \r')
        # clear long_cmd
        prev_cmd = ''

    loggerFile.write(cmd_input + ' \r')

print "exited for loop"
loggerFile.close()
print "closed file %s" % (loggerFile.name)
exit()
