import os
import shutil

def classfiyLabel(dataDict):
    for key in dataDict:
        for file in dataDict[key]:
            if os.path.splitext(file)[1] == '.hea':
                txtread = open(file)
                txtbuffer = txtread.read()
                index = txtbuffer.find('Reason for admission')
                txtbuffer = txtbuffer[index:]
                indexBegin = txtbuffer.find(':')
                indexEnd = txtbuffer.find('#')

                path = './' + txtbuffer[indexBegin + 1:indexEnd].strip()
                floder = os.path.exists(path)
                if not floder:
                    os.makedirs(path)
                for temp_file in dataDict[key]:
                    shutil.copy(temp_file,path)
                break

def readData(path):
    files = os.walk(path)
    for rootP,dirs,_ in os.walk(path):
        for dir in dirs:
            dataDict = dict()
            for rootS,_,files in os.walk(rootP + '/' + dir):
                fileList = []
                for file in files:
                    dictKey = os.path.splitext(file)[0]
                    if dictKey != 'index':
                        file = rootS + '/' + file
                        if dictKey in dataDict:
                            dataDict[dictKey].append(file)
                        else :
                            dataDict[dictKey] = file.split()
            classfiyLabel(dataDict)


if __name__ == '__main__':
    path = './ptbdb'
    readData(path)