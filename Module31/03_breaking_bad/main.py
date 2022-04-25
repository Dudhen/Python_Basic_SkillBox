import requests
import json

req = requests.get("https://breakingbadapi.com/api/deaths")

data = json.loads(req.text)

info = dict()

for i_elem in data:
    string = "season: " + str(i_elem["season"]) + " , episode: " + str(i_elem["episode"])
    if string not in info.keys():
        info[string] = i_elem["number_of_deaths"]
    else:
        info[string] += i_elem["number_of_deaths"]

most_deaths_series = {"season: 0 , episode: 0": 0}

for i in info:
    if info[i] > list(most_deaths_series.values())[0]:
        most_deaths_series.clear()
        most_deaths_series[i] = info[i]

req = requests.get("https://breakingbadapi.com/api/episodes")

data_2 = json.loads(req.text)

for i_elem in data_2:
    if int(i_elem["season"]) == int(list(most_deaths_series.keys())[0].split()[1]) \
            and int(i_elem["episode"]) == int(list(most_deaths_series.keys())[0].split()[4]):
        most_deaths_series["id"] = i_elem["episode_id"]
        for i_value in data:
            if int(i_value["season"]) == int(i_elem["season"]) and int(i_value["episode"]) == int(i_elem["episode"]):
                most_deaths_series["Умершие"] = i_value["death"]

with open("file.json", "w", encoding="utf8") as file:
    file.write(str(most_deaths_series))

print("id эпизода: {}".format(most_deaths_series["id"]))
print("Номер сезона: {}".format(list(most_deaths_series.keys())[0].split()[1]))
print("Номер эпизода: {}".format(list(most_deaths_series.keys())[0].split()[4]))
print("Общее количество смертей в серии: {}".format(list(most_deaths_series.values())[0]))
print("Список погибших: {}".format(most_deaths_series["Умершие"]))

# зачтено
