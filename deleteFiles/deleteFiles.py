import os, glob

deletedCount = 0
isStop = False

dir = input('Enter path: ')
dir = dir.replace('[', '[[]')
dir = dir[1:-1]

while isStop == False:
    print()
    extension = input('Enter extention: [default - srt]: \n')
    if extension == '':
        extension = 'srt'

    filelist = glob.glob(os.path.join(dir, "*." + extension))

    for f in filelist:
        os.remove(f)
        deletedCount += 1


    print(f'deleted: {deletedCount} files \n')
    questionToStop = input('You want to delete someone else?.. [Y/N] ')
    if questionToStop == 'N':
        isStop = True
        
    elif questionToStop == 'Y':
        print()
        dir = input('Enter path: ')
        dir = dir[1:-1]
    deletedCount = 0

