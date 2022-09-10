import os

# list data from folder_path
os.system('clear')
folderPath = input('enter folder_path: ')
myFonts = os.listdir(folderPath)

def doCompress(srcFile, outFile):
    os.system('pyftsubset {} --output-file={} --unicodes=U+0020-007E'.format(srcFile, outFile))
    os.remove(srcFile)
    os.rename(outFile, srcFile)


# looping
for x in myFonts:
    # do something
    doCompress(folderPath+'/'+x, folderPath+'/'+'_compressed'+x)