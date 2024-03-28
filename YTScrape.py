import serpapi
from googlesearch import *
from functions import *
from openpyxl import load_workbook

wb = load_workbook('example.xlsx')
ws = wb["Sheet1"]

total = 5
iter_num = 0

params = {
  "q": "mit maker portfolio",
  "engine": "google_videos",
  "hl": "en",
  "gl": "us",
  "api_key": "",
  "num": total
}

final = []
adder = []

search = serpapi.search(params)
results = search.as_dict()
video_results = results["video_results"]

#print(video_results)

#iter_num = 15

for i in range(total-iter_num):
    final.append({"Title": video_results[i+iter_num]["title"], "Link": video_results[i+iter_num]["link"]})
    final[i]["Transcript"] = get_video_transcript(final[i]["Link"])
    final[i]["Projects"] = giveAnswers(final[i]["Transcript"])
    adder = [final[i]["Title"], final[i]["Link"], final[i]["Transcript"], final[i]["Projects"]]
    ws.append(adder)
    print("Row number is2 ")

wb.save("example.xlsx")

#print(final[0])



#taking the json value and the whole loop of getting results
#just a link to result 1
# transcript = get_video_transcript("https://youtu.be/aIgVOJqYMWo?si=1qxQ8uEtgzjnDAc_")
# print(giveAnswers(transcript))


#exporting to excel

