
import sys

def main():
    #read in data
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split(' ')
    numSongs = int(line[0])
    totalTime = int(line[1])
    songList = []
    for i in range(numSongs):
        song = sys.stdin.readline()
        song = song.strip()
        song = song.split(' ')
        song = [int(x) for x in song]
        songList.append(song)
    #print("songList:",songList)

    #sort songs by length
    songList.sort(key=lambda x: x[0])
    #print("songList:",songList)

    #create list of songs for each length
    songDict = {}
    for i in range(1,16):
        songDict[i] = []
    for i in range(numSongs):
        songDict[songList[i][0]].append(songList[i])
    #print(songDict)

    #determine if any song has length that is greater than totalTime
    for i in range(len(songList)):
        if songList[i][0] > totalTime:
            print(0)
            return

    #create dictionary of songs for each genre
    songGenreDict = {1:[],2:[],3:[]}
    for i in range(1,4):
        for j in range(1,16):
            for song in songDict[j]:
                if song[1] == i:
                    songGenreDict[i].append(song)
    #print(songGenreDict)

    #create dictionary of songs of each length for each genre
    songGenreDictLength = {1:{},2:{},3:{}}
    for i in range(1,4):
        for j in range(1,16):
            songGenreDictLength[i][j] = []
    for i in range(1,4):
        for j in range(1,16):
            for song in songGenreDict[i]:
                if song[0] == j:
                    songGenreDictLength[i][j].append(song)
    #print(songGenreDictLength)

    #initialize songList for each length and genre
    songListLengthGenre = {}
    for i in range(1,16):
        songListLengthGenre[i] = {}
        for j in range(1,4):
            songListLengthGenre[i][j] = []
    #print(songListLengthGenre)

    #determine # of songs of each length and genre
    for i in range(1,16):
        if songDict[i] != []:
            for song in songDict[i]:
                songListLengthGenre[i][song[1]].append(song)
    #print(songListLengthGenre)

    #determine if any song of a particular genre has length that is greater than totalTime
    for i in range(1,4):
        for song in songGenreDict[i]:
            if song[0] > totalTime:
                print(0)
                return

    #determine if totalTime is divisible by any length
    for i in range(1,16):
        if songDict[i] != []:
            if totalTime % i == 0:
                print(1)
                return

    #initialize list of songs that can be played
    songListPlayable = []
    for i in range(1,16):
        for song in songDict[i]:
            songListPlayable.append(song)
    #print(songListPlayable)

    #initialize list of songs that cannot be played
    songListNotPlayable = []
    for i in range(1,16):
        for song in songDict[i]:
            if song[0] > totalTime:
                songListNotPlayable.append(song)
    #print(songListNotPlayable)

    #initialize list of songs that can be played for each genre
    songListPlayableGenre = {1:[],2:[],3:[]}
    for i in range(1,4):
