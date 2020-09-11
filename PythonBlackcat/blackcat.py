import os

homeFolder = 'C:/Users/xi.wu/Desktop/MY/new/black cat/Level1/'

albumList = [
'06.Great Expectations',
'07.Rip Van Winkle and The Legend of Sleepy Hollow',
'08.The Happy Prince and The Selfish Giant',
'09.The American West',
'10.Halloween Horror',
'11.The Adventures of Tom Sawyer',
'12.The Adventures of Huckleberry',
'13.The Wonderful Wizard of Oz',
'14.The Secret of the Stones',
'15.The Wind in the Willows',
'16.The Black Arrow',
'17.Around the World in Eighty Days',
'18.Little Women',
'19.Beauty and the Beast',
'20.Black Beauty'
]

for albumName in albumList:
    folder = homeFolder + albumName

    # files = os.listdir(folder)
    # for filename in files:
    #     fileNameFull = folder + '/' + filename

    #     length = len(filename)
    #     trackNo = filename[length-6:length-4]
        
    #     newFileName = albumName[3:] + '-' + trackNo + ".mp3"
    #     newFileNameFull = folder + '/' + newFileName

    #     os.rename(fileNameFull, newFileNameFull)

    newFolder = folder[3:]
    os.rename(folder, newFolder)
