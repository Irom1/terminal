import os

print("Python File Creating Terminal by irom1")
pithon_folder=input("Please enter the location of your folder: ")
if pithon_folder == "":
    pithon_folder="myfolder"
#os.makedir('text');
while True:
    file=input("file@" + pithon_folder + "~$ ")
    while file == "restart":
        print("Python File Creating Terminal by Mori")
        pithon_folder=input("Please enter the location of your folder: ")
        file = '';
    else:
      print("Creating: " + pithon_folder + '/' + file)
      f= open(pithon_folder + '/' + file,"w+")
      f.write(input('Edit the file: '))
      f= open(pithon_folder + '/' + file,"r")
      f= open(pithon_folder + '/' + file)
      print(f.read())
      f.close()