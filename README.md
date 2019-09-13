# Parse-Amazon-Transcriptions

This script is used to convert raw Amazon Transcribe json format to a nice text format with timestamps

The Amazon Transcript raw doesnt have the identifying of individuals

# General overview: 
This parses the raw format from Amazon, splits up into each sentence is a line, then find
a time stamp for each line. It can be tricky to find a timestamp for each line, so we only have time stamps
for each line that has a unique word based on the whole transcript.


# Capturing Mediasite Lecture downloads
This project was inspired by trying to get transcripts for classes university. My university uses 
mediasite to stream & playback their lectures. At some point in time they disabled downloading the lectures
so I will go into how to download the lectures even if they are disabled.
1. When the mediasite services is loaded into chrome, right click and open up the "inspect"
2. Go to the Network tab
3. Filter on mp4 ![][./images/mp4_filter.PNG]
4. Press the play  
5. Look for "Fragments(video=0,format=isoff)" ![network_tab][https://github.com/AdamCorbinFAUPhD/Parse-Amazon-Transcriptions/blob/master/images/network_tab.PNG]
6. Right click -> Copy -> Copy Link address
7. It will be a long link but you want trim off the same part at the end of the url "Fragments(video=i,format=isoff)"
8. With this link you can then go to the standard player. Depending on your University capture sometimes there is a slide video
and a video camera video. You might need to select a different one from the list from step 5 untill you find the right one.
9. Once you open up the link from 7-8, there will have the standard ... settings in the video player which has a download opetion

# Stripping the audio from an MP4 file
In this section I will go into how to get the audio from an MP4(and maybe other file types as well) so we can run the mp3
in the Amazon transcribe service. You will need VLC player 
1. Open up VLC player
2. Go to Media -> Convert and Save
3. Select the mp4(or over movie types) by pressing the Add... button ![][./images/add_media.PNG]
4. Click Convert/Save
5. Click Browse to pick the filename and destination where you want to save the file
6. Click Start



