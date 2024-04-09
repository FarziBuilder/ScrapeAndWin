import json
from functions import *

target_date = '2023-05-06'

totalLearnings = ""

link = input("Enter the link of the video:")

transcript = get_video_transcript(link)
last_reply = "0"
print("hi")
#print(transcript)

"""
var_messages = [
    {"role": "system", "content": f"I am giving you a transcript of a Youtube video. Your task is to give short meaningful answers to my questions.Preferrably give 1 sentence description and then 3 bullet points (-) to convey the answer. Always use less words and mention the jargons said in the video. Here is the transcript for your review:- {transcript}"},{"role": "user","content": "By watching this video what all will I learn, give a 1 sentence description and then 3 bullet points. After the bullet points,in a single sentence, first declare an suggest 2 short questions I can ask to learn more"}    
    ]
"""

#Remove these comments after transcript work is done
#print(transcript)
var_messages = [
    {"role": "system", "content": f"This is a transcript of a Youtube video. You have to answer questions on it, using maximum 2 to 3 lines per answer. Keep it short, quote the exact phrases used in the transcript. Go straight to the answer. Tell the exact words used in the transcript. Don't dabble, just give straight answers. Here is the transcript:- {transcript}"},{"role": "user","content": "Tell me what is taught in this video"}    
    ]


response = YTConvo(var_messages)
print(f"\nYTBuddy: {response}")
var_messages.append({"role":"assistant", "content": response})

while(True):
  user_text = input("\nUser:")
  if user_text == "quit":
    break
  var_messages.append({"role":"user", "content": user_text})
  response = YTConvo(var_messages)
  print(f"\nYTBuddy: {response}")
  last_reply = response
  var_messages.append({"role":"assistant", "content": response})