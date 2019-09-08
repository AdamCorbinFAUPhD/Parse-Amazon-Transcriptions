import json
from typing import List
import math
import datetime

# This script is used to convert raw Amazon Transcribe json format to a nice text format with timestamps
# The Amazon Transcript raw doesnt have the identifying of individuals
# General overview: This parses the raw format from Amazon, splits up into each sentence is a line, then find
# a time stamp for each line. It can be tricky to find a timestamp for each line, so we only have time stamps
# for each line that has a unique word based on the whole transcript.


input_file_name = "lecture_3_output_RAW.json"
input_file_name = "data_science_leccture_3_raw.json"

output_file_name = "CEN_5035_SW_ENG_lecture_2.txt"
output_file_name = "CAP5768_data_science_lecture_3.txt"
fh_json = open(input_file_name)

datastore = json.load(fh_json)
list_of_lines = []

word_occurrence = {}  # key word, value = count. This is used to keep track of unique words

for item in datastore:
    print(item + " " + str(type(datastore[item])))
    if isinstance(datastore[item], str):
        print("\t" + datastore[item])
    else:
        for i in datastore[item]:
            print("\t" + i + " " + str(type(datastore[item][i])))
            if i == "transcripts":
                print(datastore[item][i][0]['transcript'])
                list_of_lines = str(datastore[item][i][0]['transcript']).split(".")
                # for sen in list_of_sen:
                #     print(sen.lstrip())
            else:
                for word_data in datastore[item]["items"]:
                    # word_data['alternatives'].content
                    # print(json.dumps(word_data))
                    word = word_data['alternatives'][0]['content']
                    # print(word)
                    if word not in word_occurrence:
                        word_occurrence[word] = 1
                    else:
                        word_occurrence[word] += 1

# Create a dict of word to time. Its ok that the time gets over written because we wont use them for the final result
# because we will be using only times where the word occurrence is 1
time_dict = {}
print(datastore["results"]["items"])
for item in datastore["results"]["items"]:
    word = item["alternatives"][0]["content"]
    start_time = 0
    if "start_time" in item:
        start_time = float(item["start_time"])
    #print("Word:", word, "Time:", start_time)
    time_dict[word] = start_time

fh_output = open(output_file_name, "w")
for sen in list_of_lines:
    # print(sen)
    old_sen = sen
    sen = sen.lstrip()
    word_list = sen.split(" ")
    word_list.sort(reverse=True, key=len)
    final_chosen_word = ""
    final_chosen_word_ocurance = math.inf
    for word in word_list:
        # print(word_list)
        chosen_word = word.replace(",", "")
        chosen_word = chosen_word.replace("?", "")
        chosen_word = chosen_word.replace(".", "")
        # print(chosen_word)
        if len(chosen_word) > 0 and chosen_word in word_occurrence:
            # print(chosen_word, word_count[chosen_word])
            if final_chosen_word_ocurance > word_occurrence[chosen_word]:
                final_chosen_word_ocurance = word_occurrence[chosen_word]
                final_chosen_word = chosen_word
    if len(final_chosen_word) > 0:
        start_time = 0
        if final_chosen_word in time_dict and word_occurrence[final_chosen_word] == 1:
            start_time = time_dict[final_chosen_word]

        date_time = str(datetime.timedelta(seconds=start_time))[0:9]
        time_and_sen = ""
        if start_time > 0:
            time_and_sen = "[" + str(date_time) + "] " + old_sen
            print(time_and_sen + " chosen word: '" + final_chosen_word + "' count:" + str(word_occurrence[final_chosen_word]))

        else:
            time_and_sen = "[]\t\t\t" + old_sen
            print(time_and_sen + " chosen word: '" + final_chosen_word + "' count:" + str(
                word_occurrence[final_chosen_word]))
        fh_output.write(time_and_sen + "\n")
fh_output.close()
# def print_dict(index, _dict):
