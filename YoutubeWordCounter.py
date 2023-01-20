import requests as req
import string
from youtube_transcript_api import YouTubeTranscriptApi

class FailedToGetID(Exception):
    ...
class FailedToGetTranscript(Exception):
    ...

charsIncludedInID = list(string.ascii_letters + string.digits)


print("-"*70+"\nWelcome to the youtube word counter where you give the video and I give you the number of times a word is said (approximatly)!")
youtubeURL = input("Youtube URL: ")
word = input("Enter the word you're looking for: ")

def getID(url):
    try:
        indexOfStart = url.index("v=") +2
        id = ""
        for char in url[indexOfStart:]:
            if char in charsIncludedInID:
                id += char
            else:
                return id
        return id
    except:
        raise FailedToGetID

def getTranscript(id):
    try:
        transcriptUnformatted = YouTubeTranscriptApi.get_transcript(id)
        transcriptFormatted = ""
        for elem in transcriptUnformatted:
            transcriptFormatted += (elem["text"] + " ")
        return transcriptFormatted
    except:
        raise FailedToGetTranscript


print(getTranscript(getID(youtubeURL)).count(word))