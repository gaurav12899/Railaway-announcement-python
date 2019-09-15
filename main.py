import pyaudio
import pandas as pd
import os
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text,filename):
    mytext= str(text)
    language="hi"
    myobj=gTTS(text=mytext,lang=language,slow=False)
    myobj.save(filename)

#this function returns pydub's audio segment
def mergeAudios(audios):
    combined=AudioSegment.empty()
    for audio in audios:
        combined+=AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    #1.generate krippya dhyan dijiye
    audio= AudioSegment.from_mp3("announcement.mp3")
    start=2000
    finish=7340
    audioProcessed=audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format="mp3")

    #2.generate train_no
    #3.generate train name

    #4.generate thodi der me platform no.
    audio= AudioSegment.from_mp3("announcement.mp3")
    start=12950
    finish=15000
    audioProcessed=audio[start:finish]
    audioProcessed.export("4_hindi.mp3",format="mp3")

    #5.generate platform num

    #6.generate aa rhi h 
    audio= AudioSegment.from_mp3("announcement.mp3")
    start=15500
    finish=17000
    audioProcessed=audio[start:finish]
    audioProcessed.export("6_hindi.mp3",format="mp3")







def generateAnnouncement(filename): 
    df = pd.read_excel(filename)
    print(df)
    for index,item in df.iterrows():
        #2. generate train num
        textToSpeech(item["train_no"],'2_hindi.mp3')
        #3. generate train name
        textToSpeech(item["train_name"],'3_hindi.mp3')
        #3. generate platform num
        textToSpeech(item["platform"],'5_hindi.mp3')

        audios=["{}_hindi.mp3".format(i) for i in range(1,7)]

        announcement = mergeAudios(audios)
        announcement.export("announcement_{}_{}.mp3".format("train_no",index+1),format="mp3")


if __name__ == "__main__":
    print("generating skeleton...")
    generateSkeleton()
    print("Now generating announcements...")
    generateAnnouncement("announce_hindi.xlsx")
