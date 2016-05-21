import os

file_list = []
questions = []
for root, dirs, files in os.walk('treasure_hunt'):
  for file in files:
    if file.startswith('win'):
    	ans = os.path.join(root, file)
    elif file.startswith('q') and file not in file_list:
    	file_list.append(file)
    	file_path = os.path.join(root,file)
    	questions.append(open(file_path,'r').readline())

answers = ans.split("/")

for x in xrange (0, len(questions)):
	print questions[x] + answers[x+1] + "\n"

