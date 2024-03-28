import openai
from youtube_transcript_api import YouTubeTranscriptApi
import re
from openai import OpenAI


def get_video_id_from_url(url):
    video_id = None
    pattern = re.compile(r"(?:https?:\/\/)?(?:www\.)?youtu(?:\.be\/|be\.com\/watch\?v=)([\w\-]+)")
    match = pattern.match(url)

    if match:
        video_id = match.group(1)

    return video_id

def get_video_transcript(url):
    video_id = get_video_id_from_url(url)

    if not video_id:
        print("Invalid YouTube video URL.")
        return

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'en-GB'])
        transcript_text = " ".join([entry["text"] for entry in transcript])
        #print(transcript_text)
        return transcript_text
    except Exception as e:
        #print(f"Error: {str(e)}")
        return f"Error: {str(e)}"
    

def giveAnswers(transcript):
  completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "I am giving you a transcript of a Youtube video. Your task is to list the projects done in this video. Give a 3 to 5 word headline to the project and then one line explaining it.In the one line, always use the jargons in the video, remember to put the jargons."},
    {
      "role": "user", "content": transcript
    }
  ]
  )
  return completion.choices[0].message.content