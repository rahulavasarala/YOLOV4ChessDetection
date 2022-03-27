import shutil, os

setName = "train" #CHANGE THIS
annotation_switch_arr = [0,1,2,3,4,5,6,7,8,9,10,11,12]#CHANGE THIS


##------------------Touch with your own Discretion---------------------------------##

f_folder_name = setName + "F"
os.mkdir("./{dest}".format(dest = f_folder_name))

jpgCount = 0

for file in os.listdir("./{dest}".format(dest = setName)):
    if file.endswith(".jpg"):
        print(file)
        shutil.copy("./{dest}/{filename}".format(dest = setName, filename = file), "./{dest}".format(dest = f_folder_name))
        os.rename("./{dest}/{filename}".format(dest = f_folder_name, filename = file), "./{dest}/{name}-{x}.jpg".format(dest = f_folder_name,name = setName, x = jpgCount))


        #extract the beginning of the file without the .jpg
        #append .txt to it 
        #open the .txt  file in read only mode
        #read each line and do the switch annotation arr logic on it
        #write the lines to the new annotation file

        stem = file[0:-4]
        print(stem)
        annotFile = open("./{dest}/{name}-{x}.txt".format(dest = f_folder_name,name = setName, x = jpgCount), 'w')
        readableFile = open("./{dest}/{filename}.txt".format(dest = setName, filename = stem), 'r')
        print("This runs")

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



        jpgCount += 1
        print(jpgCount)
        annotFile.close()
        readableFile.close()

##------------------Touch with your own Discretion---------------------------------##



    
