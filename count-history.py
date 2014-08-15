import json
import os
import pprint

history = {}
home = os.path.expanduser('~')
history_directory = home + "/.bash_history"

history_file = open(history_directory, 'r')

for command in history_file:
	#sanitize command and split into arguments
	command = command.strip("\n")
	args = command.split(" ")
	args = [arg for arg in args if arg != '']
	
	command = args[0]
	if len(args) > 1:
		args = args[1:]
	else:
		args = ['']

	if command in history: 
		history[command]["count"]+=1
	else:
		history[command] = {
			"count": 1,
			"args": {},
		}

	for arg in args: 
		if arg in history[command]["args"]:
			history[command]["args"][arg]["count"]+=1
		else:
			history[command]["args"][arg] = {
				"count": 1,
			}
data = json.dumps(history)
print data
# pp = pprint.PrettyPrinter()
# pp.pprint(history)