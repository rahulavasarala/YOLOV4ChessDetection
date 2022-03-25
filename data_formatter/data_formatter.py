import shutil, os

setName = "valid" #CHANGE THIS
annotation_switch_arr = [0,0,1,2,-1,4,5,6,7,8,9,10,11]#CHANGE THIS


##------------------Touch with your own Discretion---------------------------------##

f_folder_name = setName + "F"
os.mkdir("./{dest}".format(dest = f_folder_name))

jpgCount = 0
txtCount = 0

for file in os.listdir("./{dest}".format(dest = setName)):
    if file.endswith(".jpg"):
        shutil.copy("./{dest}/{filename}".format(dest = setName, filename = file), "./{dest}".format(dest = f_folder_name))
        os.rename("./{dest}/{filename}".format(dest = f_folder_name, filename = file), "./{dest}/{name}-{x}.jpg".format(dest = f_folder_name,name = setName, x = jpgCount))
        jpgCount += 1

    elif file.endswith(".txt"):
        annotFile = open("./{dest}/{name}-{x}.txt".format(dest = f_folder_name,name = setName, x = txtCount), 'w')
        #file is jst a string, to read from it we need to open a file

        readableFile = open("./{dest}/{filename}".format(dest = setName, filename = file), 'r')

        line = readableFile.readline()

        while line:
            
            splitArr = line.split(" ", 1)

            if annotation_switch_arr[int(splitArr[0])] == -1:
                line = readableFile.readline()
                continue
            modLine = str(annotation_switch_arr[int(splitArr[0])]) + " "
            modLine = modLine + splitArr[1]
            annotFile.write(modLine)
            line = readableFile.readline()
            

        annotFile.close()
        readableFile.close()
        txtCount += 1

##------------------Touch with your own Discretion---------------------------------##
    
