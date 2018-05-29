print("Python File Creating Terminal by Mori")
pithon_folder=input("Please enter the location of your folder: ")
if pithon_folder == "1":
    pithon_folder="/Users/Wendy/Desktop/"
x = 1
while True:
    file=input("file@folder~$ ")
    while file == "restart":
        print("============= RESTART: /Users/Wendy/Documents/python/Terminal.py =============")
        print("Python File Creating Terminal by Mori")
        pithon_folder=input("Please enter the location of your folder: ")
        file=input("file@folder~$ ")
    print("Creating: " + pithon_folder + file)
    f= open(pithon_folder + file,"w+")
    f= open(pithon_folder + file,"r")
    f= open(pithon_folder + file)
    print(f)
 
