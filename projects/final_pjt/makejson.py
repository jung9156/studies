import json
import requests


def color(n):
    color_data = {"28": "red", "12": "red", "99": "grey", "36": "grey", "35": "yellow", "10402": "yellow", "16": "yellow", "18": "mint", "10749": "mint", "878": "skyblue", "14": "skyblue", "10752": "skyblue", "53": "dark", "80": "dark", "9648": "dark", "27": "dark", "10751": "mint", "10770": "grey", "37": "grey"}
    return color_data[str(n)]


file_data = []




for i in range(1, 51):
    params = {'api_key': '9bd3393b06f6e8bd8002317b32184318', 'language': 'ko-KR', 'page': i}
    res = requests.get('https://api.themoviedb.org/3/movie/top_rated', params=params).json()
    
    


    r_g = res["results"]
    for r in r_g:

        results = {}
        results["model"] = "movies.movie"
        results["pk"] = r["id"]
        results["fields"] = r
        results["fields"]["red"] = 0
        results["fields"]["grey"] = 0
        results["fields"]["yellow"] = 0
        results["fields"]["mint"] = 0
        results["fields"]["skyblue"] = 0
        results["fields"]["dark"] = 0
        del results["fields"]["id"]
        for r_g2 in r["genre_ids"]:
            results["fields"][color(r_g2)] = 1
    
    
        file_data.append(results)



# print(json.dumps(file_data, ensure_ascii=False, indent="\t"))
with open("movie_data.json", "w", encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t") 