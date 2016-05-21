import os

#Reading input.txt file content
file_input=open("input.txt",'r')
lines = file_input.readlines()

#declaring arrays and variables
questions=[]
answers=[]
options=[]

no_of_questions=0
cue=0

print lines
#Read lines into respective arrays
#cue to keep track of line number
while (cue<len(lines)):
        questions.append(lines[cue])
        cue+=1
        #opt is an array containing options per level
        opt=[]
        while(lines[cue]!="\n"):
                opt.append(lines[cue])
                cue+=1
        #options is an array of all opt arrays (options per level)
        options.append(opt)
        cue+=1
        answers.append(lines[cue])
        cue+=2
        no_of_questions+=1

'''
#Display questions, options and answers
for n in range (0,no_of_questions):
	print questions[n]
	print options[n]
	print answers[n]
'''

#Get current working directory and create a folder treasure_hunt
directory= os.getcwd()+"/treasure_hunt"
if not os.path.exists(directory):
        os.makedirs(directory)

folders=0
paths=1

#create a recursive function which makes level at directory with given list of folders(opt)
#level is indexed from 1, opt is indexed from 0

def make_level(directory, level, opt):
        #print "Creating level "+str(level) +" at "+directory
        #Create question file on creating a new directory
        text_file = open(directory+"/q"+str(level)+".txt", "w")
        text_file.write(questions[level-1])
        text_file.close()
        global folders
        #Create all folders as per provided opt array
        for x in range (0,len(opt)):
                #print "Created " +directory+"\\"+opt[x][:-1]
                if not os.path.exists(directory+"/"+opt[x][:-1]):
                        os.makedirs(directory+"/"+opt[x][:-1])
                folders+=1
                if(level+1<=no_of_questions):
                        make_level(directory+"/"+opt[x][:-1],level+1,options[level])

#Call the recursive function make_level
make_level(directory,1,options[0])

#Find directory of where win.txt is to be created
for x in range (0, len(answers)):
        global paths
        paths*=len(options[x])
        if answers[x].endswith("\n"):
                answers[x] = answers[x][:-1]
        directory=directory+"/"+answers[x]

#Create win.txt
text_file = open(directory+"/win.txt", "w")
text_file.write("You win!")
text_file.close()

print "No of folders created= "+ str(folders)
print "No of paths possible= "+ str(paths)
