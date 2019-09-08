# Parse-Amazon-Transcriptions

This script is used to convert raw Amazon Transcribe json format to a nice text format with timestamps

The Amazon Transcript raw doesnt have the identifying of individuals

# General overview: 
This parses the raw format from Amazon, splits up into each sentence is a line, then find
a time stamp for each line. It can be tricky to find a timestamp for each line, so we only have time stamps
for each line that has a unique word based on the whole transcript.

# Example output
[]			 All right

[0:06:16.3]  Good afternoon, everyone

[]			 And welcome back

[0:06:19.9]  I overheard some conversations of Dorian

[0:06:26.5]  I guess everybody was hopefully not strongly affected by it

[]			 It's good to see you again

[0:06:31.8]  A lot of work to get ready for it

[]			 Of course I know the feeling

