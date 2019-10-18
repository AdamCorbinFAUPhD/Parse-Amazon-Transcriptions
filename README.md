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
3. Filter on mp4 

![](/images/mp4_filter.PNG)

4. Press the play  
5. Look for "Fragments(video=0,format=isoff)"

![GitHub Logo](/images/network_tab.PNG)


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
3. Select the mp4(or over movie types) by pressing the Add... button ![](/images/add_media.PNG)
4. Click Convert/Save
5. Click Browse to pick the filename and destination where you want to save the file
6. Click Start

# Uploading mp3 to Amazon S3
1. Go to [https://s3.console.aws.amazon.com](https://s3.console.aws.amazon.com)
2. Watch the video here to create a Bucket and upload the file. You only need to create a bucket 1 time [Uploading mp3 to Amazon S3](https://youtu.be/1ZDbvHZKgiU)
3. Once the video has been uploaded, copy that direct link to that file. It will be used in the Amazon Transcribe

# Running Amazon Transcribe
1. Go to AWS Console: [https://console.aws.amazon.com/console](https://console.aws.amazon.com/console)
2. Find Amazon Transcribe
3. Click on Create Job
4. Add in the job name(I think it needs to be unique)
5. In the Imput Data section add in your S3 link to you mp3 file from step 3 in Uploading mp3 to Amazon S3
6. Hit Create. This job will now kick off and transcribe your mp3 file. It can take about 30min for a full 2:30 lecture.

# Creating nice output with timestamps
Once the Amazon Transcribe job finishes you can download the json output but its really hard for a human to parse it. 
I also wanted to get timestamps so I could go back and watch the important parts. This is where the python script comes into play.
1. On the completed job, you can click the Download full transcript button to save the output.
2. In the python file you can update the input_file_name to this new file and the output_file_name to what you want. That should be it.

# Improvments
If you look at the output you can see some lines dont have timestamps. Thats becuase the script looks for unique words within the line and when there is a unique name its really easy to get the timestamp. 
If there are no unique names then it just puts blank brackets. I found that this would good enough but it could be improved upon if someone wanted full timestamps.


