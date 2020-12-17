import os, time
from termcolor import colored

def message(mess):
  print(colored('>> ' + mess,'yellow'))
  time.sleep(1)
def error(mess):
  print(colored('>> ' + mess,'red'))
  time.sleep(1)

print(colored("--------- Python File Creating Terminal by irom1 ---------",'blue'))
print('')
pithon_folder=input(colored('>> Please enter the location of your folder: ','green'))
if pithon_folder == "":
  pithon_folder="myfolder"
  message("Choosing defult folder 'myfolder' because no other folder was specified.")
try:
  os.mkdir(pithon_folder)
except:
  message('Folder opened!')
else:
  message('Folder created!')
finally:
  message("Type 'help' for more information on this project!")
  x = True
while x == True:
  print()
  file=input(colored("file@" + pithon_folder + "~$ ",'green'))
  if file == "restart":
    #print("Python File Creating Terminal by Mori")
    #pithon_folder=input("Please enter the location of your folder: ")
    file = ''
  elif file == "exit":
    x = False
  elif file == "help":
    message("Help Menu:")
    message("create [file] = create and edit a file")
    message("read [file] = get file contents")
    message("delete [file] = delete a file")
    message("exit = end script")
    message("help = show this help menu")
  elif file.startswith('read '):
    file = file.replace("read ",'')
    try:
      f= open(pithon_folder + '/' + file)
      print(f.read())
      f.close()
    except:
      error("File not found")
  elif file.startswith("create ") or file.startswith("edit "):
    file = file.replace("create ",'').replace("edit ",'')
    print(colored(">> Creating: " + pithon_folder + '/' + file,'yellow'))
    f= open(pithon_folder + '/' + file,"w+")
    print(colored('>> Edit the file below: ','yellow'))
    f.write(input(''))
    f.close()
    message("File " + file + " created/edited")
  elif file.startswith("delete "):
    file = pithon_folder + '/' + file.replace("delete ",'')
    if os.path.exists(file):
      os.remove(file)
      message("File " + file + " deleted!")
    else:
      error("The file does not exist")
  else:
    error("Command not reconized (maybe it is typed wrong?)")