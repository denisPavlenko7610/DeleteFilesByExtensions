import os
import glob

deletedCount = 0
isStop = False


dir = input('Enter path: ')
dir = dir[1:-1]

while isStop == False:
    extension = input('Enter extention: [default - srt]: ')
    if extension == '':
        extension = 'srt'

    filelist = glob.glob(os.path.join(dir, "*." + extension))

    for f in filelist:
        os.remove(f)
        deletedCount += 1


    print(f'deleted: {deletedCount} files')
    questionToStop = input('You want to delete someone else?.. [Y/N]')
    if questionToStop == 'N':
        isStop = True
        
    elif questionToStop == 'Y':
        dir = input('Enter path: ')
        dir = dir[1:-1]
    deletedCount = 0

