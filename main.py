DEFAULT = object()

map = [
    "ajrenlbnvsvesys",
    "hieeiaretigntel",
    "srtgiemnlibaone",
    "twhttnewnlpccmi",
    "wtenemdgorbykig",
    "slaeaseeenjdihh",
    "flbntrnsersnncn",
    "murabseijrvagao",
    "cokronpboancnkb",
    "sseltfireplaceb",
    "vawsreloractahi",
    "deldnacwreathir",
    "sualcatnascardu",
    "ppoekgklnottwbd",
    "hnqwvpmlzxiwhlp"
]

def start(map, schar):
    '''first letter'''
    matches = []
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char is schar:
                matches.append((x,y))
    return matches

def lookAround(map, x, y, schar, dirs):
    #[7][0][1]
    #[6][x][2]
    #[5][4][3]
    matches=[]
    newDirs =[]
    if type(dirs) is not list:
        dirs = [dirs]
    for diR in dirs:
        if diR is 0:
            try:
                if map[y-1][x] is schar:
                    matches.append((x, y-1))
                    newDirs.append(0)
            except:
                pass
        elif diR is 1:
            try:
                if map[y-1][x+1] is schar:
                    matches.append((x+1, y-1))
                    newDirs.append(1)
            except:
                pass
        elif diR is 2:
            try:
                if map[y][x+1] is schar:
                    matches.append((x+1, y))
                    newDirs.append(2)
            except:
                pass
        elif diR is 3:
            try:
                if map[y+1][x+1] is schar:
                    matches.append((x+1, y+1))
                    newDirs.append(3)
            except:
                pass
        elif diR is 4:
            try:
                if map[y+1][x] is schar:
                    matches.append((x, y+1))
                    newDirs.append(4)
            except:
                pass    
        elif diR is 5:
            try:
                if map[y+1][x-1] is schar:
                    matches.append((x-1, y+1))
                    newDirs.append(5)
            except:
                pass
        elif diR is 6:
            try:DEFAULT = object()

map = [
    "ajrenlbnvsvesys",
    "hieeiaretigntel",
    "srtgiemnlibaone",
    "twhttnewnlpccmi",
    "wtenemdgorbykig",
    "slaeaseeenjdihh",
    "flbntrnsersnncn",
    "murabseijrvagao",
    "cokronpboancnkb",
    "sseltfireplaceb",
    "vawsreloractahi",
    "deldnacwreathir",
    "sualcatnascardu",
    "ppoekgklnottwbd",
    "hnqwvpmlzxiwhlp"
]

def start(map, schar):
    '''first letter'''
    matches = []
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char is schar:
                matches.append((x,y))
    return matches

def lookAround(map, x, y, schar, dirs):
    #[7][0][1]
    #[6][x][2]
    #[5][4][3]
    matches=[]
    newDirs =[]
    if type(dirs) is not list:
        dirs = [dirs]
    for diR in dirs:
        if diR is 0:
            try:
                if map[y-1][x] is schar:
                    matches.append((x, y-1))
                    newDirs.append(0)
            except:
                pass
        elif diR is 1:
            try:
                if map[y-1][x+1] is schar:
                    matches.append((x+1, y-1))
                    newDirs.append(1)
            except:
                pass
        elif diR is 2:
            try:
                if map[y][x+1] is schar:
                    matches.append((x+1, y))
                    newDirs.append(2)
            except:
                pass
        elif diR is 3:
            try:
                if map[y+1][x+1] is schar:
                    matches.append((x+1, y+1))
                    newDirs.append(3)
            except:
                pass
        elif diR is 4:
            try:
                if map[y+1][x] is schar:
                    matches.append((x, y+1))
                    newDirs.append(4)
            except:
                pass    
        elif diR is 5:
            try:
                if map[y+1][x-1] is schar:
                    matches.append((x-1, y+1))
                    newDirs.append(5)
            except:
                pass
        elif diR is 6:DEFAULT = object()

map = [
    "ajrenlbnvsvesys",
    "hieeiaretigntel",
    "srtgiemnlibaone",
    "twhttnewnlpccmi",
    "wtenemdgorbykig",
    "slaeaseeenjdihh",
    "flbntrnsersnncn",
    "murabseijrvagao",
    "cokronpboancnkb",
    "sseltfireplaceb",
    "vawsreloractahi",
    "deldnacwreathir",
    "sualcatnascardu",
    "ppoekgklnottwbd",
    "hnqwvpmlzxiwhlp"
]

def start(map, schar):
    '''first letter'''
    matches = []
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char is schar:
                matches.append((x,y))
    return matches

def lookAround(map, x, y, schar, dirs):
    #[7][0][1]
    #[6][x][2]
    #[5][4][3]
    matches=[]
    newDirs =[]
    if type(dirs) is not list:
        dirs = [dirs]
    for diR in dirs:
        if diR is 0:
            try:
                if map[y-1][x] is schar:
                    matches.append((x, y-1))
                    newDirs.append(0)
            except:
                pass
        elif diR is 1:
            try:
                if map[y-1][x+1] is schar:
                    matches.append((x+1, y-1))
                    newDirs.append(1)
            except:
                pass
        elif diR is 2:
            try:
                if map[y][x+1] is schar:
                    matches.append((x+1, y))
                    newDirs.append(2)
            except:
                pass
        elif diR is 3:
            try:
                if map[y+1][x+1] is schar:
                    matches.append((x+1, y+1))
                    newDirs.append(3)
            except:
                pass
        elif diR is 4:
            try:
                if map[y+1][x] is schar:
                    matches.append((x, y+1))
                    newDirs.append(4)
            except:
                pass    
        elif diR is 5:
            try:
                if map[y+1][x-1] is schar:
                    matches.append((x-1, y+1))
                    newDirs.append(5)
            except:
                pass
        elif diR is 6:
            try:
                if map[y][x-1] is schar:
                    matches.append((x-1, y))
                    newDirs.append(6)
            except:
                pass
        elif diR is 7:
            try:
                if map[y-1][x-1] is schar:
                    matches.append((x-1, y-1))
                    newDirs.append(7)
            except:
                pass
    return matches, newDirs

def followPath(map, startPos, word, diR, isFound, layer, found):
    '''rest of the letters'''
    if len(word)>0:
        matches, diR = lookAround(map, startPos[0], startPos[1], word[0], diR)
        
        if len(matches)>0:
            found.append(matches[0])
        if len(matches)==0:
            isFound = False
        elif len(matches)>0 and len(word[1:])==0:
            isFound = True

    if isFound == None:
        isFound, found = followPath(map, matches[0], word[1:], diR, isFound, layer+1, found)
    return isFound, found

def choosePath(map, startPos, word):
    '''2nd letter'''
    matches, dirs = lookAround(map, startPos[0], startPos[1], word[0], dirs = [0,1,2,3,4,5,6,7])
    foundlist=[]
    for d, diR in enumerate(dirs):
        foundlist.append([startPos, matches[d]])
        foundlist[d].extend(followPath(map, matches[d], word[1:], diR, isFound=None, layer=1, found=[])[1])
    return foundlist

if __name__ == "__main__":
    word = input("Enter your word: ")
    startPoses = start(map, word[0])
    matches = []
    for pos in startPoses:
        guesses = choosePath(map, pos, word[1:])
        if len(guesses)>0:
            for guess in guesses:
                if len(word)==len(guess):
                    ismatch = True
                    for i, gPos in enumerate(guess):
                        if word[i] != map[gPos[1]][gPos[0]]:
                            ismatch = False
                    if ismatch:
                        matches.append(guess)
    if len(matches) > 0:
        print("FOUND", len(matches), "MATCHES:")
        for m in matches:
            print(m)
    else:
        print("WORD NOT FOUND!")
            try:
                if map[y][x-1] is schar:
                    matches.append((x-1, y))
                    newDirs.append(6)
            except:
                pass
        elif diR is 7:
            try:
                if map[y-1][x-1] is schar:
                    matches.append((x-1, y-1))
                    newDirs.append(7)
            except:
                pass
    return matches, newDirs

def followPath(map, startPos, word, diR, isFound, layer, found):
    '''rest of the letters'''
    if len(word)>0:
        matches, diR = lookAround(map, startPos[0], startPos[1], word[0], diR)
        
        if len(matches)>0:
            found.append(matches[0])
        if len(matches)==0:
            isFound = False
        elif len(matches)>0 and len(word[1:])==0:
            isFound = True

    if isFound == None:
        isFound, found = followPath(map, matches[0], word[1:], diR, isFound, layer+1, found)
    return isFound, found

def choosePath(map, startPos, word):
    '''2nd letter'''
    matches, dirs = lookAround(map, startPos[0], startPos[1], word[0], dirs = [0,1,2,3,4,5,6,7])
    foundlist=[]
    for d, diR in enumerate(dirs):
        foundlist.append([startPos, matches[d]])
        foundlist[d].extend(followPath(map, matches[d], word[1:], diR, isFound=None, layer=1, found=[])[1])
    return foundlist

if __name__ == "__main__":
    word = input("Enter your word: ")
    startPoses = start(map, word[0])
    matches = []
    for pos in startPoses:
        guesses = choosePath(map, pos, word[1:])
        if len(guesses)>0:
            for guess in guesses:
                if len(word)==len(guess):
                    ismatch = True
                    for i, gPos in enumerate(guess):
                        if word[i] != map[gPos[1]][gPos[0]]:
                            ismatch = False
                    if ismatch:
                        matches.append(guess)
    if len(matches) > 0:
        print("FOUND", len(matches), "MATCHES:")
        for m in matches:
            print(m)
    else:
        print("WORD NOT FOUND!")
                if map[y][x-1] is schar:
                    matches.append((x-1, y))
                    newDirs.append(6)
            except:
                pass
        elif diR is 7:
            try:
                if map[y-1][x-1] is schar:
                    matches.append((x-1, y-1))
                    newDirs.append(7)
            except:
                pass
    return matches, newDirs

def followPath(map, startPos, word, diR, isFound, layer, found):
    '''rest of the letters'''
    if len(word)>0:
        matches, diR = lookAround(map, startPos[0], startPos[1], word[0], diR)
        
        if len(matches)>0:
            found.append(matches[0])
        if len(matches)==0:
            isFound = False
        elif len(matches)>0 and len(word[1:])==0:
            isFound = True

    if isFound == None:
        isFound, found = followPath(map, matches[0], word[1:], diR, isFound, layer+1, found)
    return isFound, found

def choosePath(map, startPos, word):
    '''2nd letter'''
    matches, dirs = lookAround(map, startPos[0], startPos[1], word[0], dirs = [0,1,2,3,4,5,6,7])
    foundlist=[]
    for d, diR in enumerate(dirs):
        foundlist.append([startPos, matches[d]])
        foundlist[d].extend(followPath(map, matches[d], word[1:], diR, isFound=None, layer=1, found=[])[1])
    return foundlist

if __name__ == "__main__":
    word = input("Enter your word: ")
    startPoses = start(map, word[0])
    matches = []
    for pos in startPoses:
        guesses = choosePath(map, pos, word[1:])
        if len(guesses)>0:
            for guess in guesses:
                if len(word)==len(guess):
                    ismatch = True
                    for i, gPos in enumerate(guess):
                        if word[i] != map[gPos[1]][gPos[0]]:
                            ismatch = False
                    if ismatch:
                        matches.append(guess)
    if len(matches) > 0:
        print("FOUND", len(matches), "MATCHES:")
        for m in matches:
            print(m)
    else:
        print("WORD NOT FOUND!")
