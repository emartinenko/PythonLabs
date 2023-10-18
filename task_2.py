volume = 1.44
countPage = 100
countRow = 50
countChar = 25
BYTE_CHAR = 4

volumeBookInByte = BYTE_CHAR * countChar * countRow * countPage
volumeInByte = volume * (1024**2)

countBook = int(volumeInByte // volumeBookInByte)

print("Количество книг, помещающихся на дискету:", countBook)
