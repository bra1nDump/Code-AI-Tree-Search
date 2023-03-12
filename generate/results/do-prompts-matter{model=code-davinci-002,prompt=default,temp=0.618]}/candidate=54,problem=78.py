
#DONE

def songGenreCount(n, t):
    """
    n = number of songs
    t = number of minutes

    """
    #dictionary for song minutes and genre for each song
    songList = {}
    for i in range(n):
        songMinutes, songGenre = map(int, input().split())
        songList[i+1] = [songMinutes, songGenre]
    #convert to list
    songList = list(songList.values())
    #number of songs within the time range
    songList = [x for x in songList if x[0] <= t]
    #sort by minutes
    songList.sort(key=lambda x: x[0])
    #print(songList)
    #total number of sequences
    numberOfSequences = 0
    #save all sequences
    sequences = []
    #check each song
    for i in range(len(songList)):
        #check if song can play
        if (t-songList[i][0]) >= 0:
            #subtract the song from time
            t -= songList[i][0]
            #check for other songs
            for j in range(i+1, len(songList)):
                #check if song can play
                if (t-songList[j][0]) >= 0:
                    #subtract the song from time
                    t -= songList[j][0]
                    #check for other songs
                    for k in range(j+1, len(songList)):
                        #check if song can play
                        if (t-songList[k][0]) >= 0:
                            #subtract the song from time
                            t -= songList[k][0]
                            #check if genres are different
                            if (songList[i][1] != songList[j][1] and songList[i][1] != songList[k][1] and songList[j][1] != songList[k][1]):
                                #add sequence to sequence list
                                sequences.append([songList[i], songList[j], songList[k]])
                                #add to number of sequences
                                numberOfSequences += 1
                            #return time to check other songs
                            t += songList[k][0]
                    #return time to check other songs
                    t += songList[j][0]
            #return time to check other songs
            t += songList[i][0]
    #print(sequences)
    #return number of sequences
    return numberOfSequences

#test
n, t = map(int, input().split())
print(songGenreCount(n, t))