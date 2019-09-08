# Parse-Amazon-Transcriptions

This script is used to convert raw Amazon Transcribe json format to a nice text format with timestamps

The Amazon Transcript raw doesnt have the identifying of individuals

# General overview: 
This parses the raw format from Amazon, splits up into each sentence is a line, then find
a time stamp for each line. It can be tricky to find a timestamp for each line, so we only have time stamps
for each line that has a unique word based on the whole transcript.
