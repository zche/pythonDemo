import requests
import json
import os

indexName ="tmdb"
mappingFolder ="/Users/zhaoruifei/Study/python/elasticsearch/tmdb-search/mapping"
headers={"Content-Type":"application/json","Accept":"application/json"}

def extract():
    f = open('/Users/zhaoruifei/Study/python/elasticsearch/tmdb-search/tmdb.json')
    if f:
         return json.loads(f.read());
    return {}


def reindex(settings, movieDict={}):

    resp = requests.delete("http://localhost:9200/"+indexName) #D
    data = json.dumps(settings,indent=4, sort_keys=True)
    print("settings:\n{data}".format(data=data))
    resp = requests.put("http://localhost:9200/"+indexName,headers=headers, data=data)

    print("Response for createing the index with the settings and mappings.{text}".format(text=resp.text))

    bulkMovies = ""
    for id, movie in movieDict.items():
        addCmd = {"index": {"_index": indexName,
                            "_type": "_doc",
                            "_id": movie["id"]}}
        bulkMovies += json.dumps(addCmd) + "\n" + json.dumps(movie) + "\n"

    print("Start ingesting data......")
    resp = requests.post("http://localhost:9200/_bulk", headers={"content-type":"application/json"}, data=bulkMovies)
    #print resp.content

def select_mapping():
    print("\r\n>> Please select the mapping file. Choose 0 for empty mapping\r\n")
    mappingList=os.listdir(mappingFolder)
    print("[0] empty mapping. It will use dynamic mapping with default settings")
    for idx, mappingItem in enumerate(mappingList):
        print("[{index}] {item}".format(index = idx+1,item=mappingItem))
    userInput = input()
    selectIndex = int(userInput)
    # try:
    #     selectIndex = int(userInput)
    # except ValueError:
    #     selectIndex =-1

    if(selectIndex==-1 or selectIndex > len(mappingList)+1):
        print('\033[31mPlease provide a valid integer \033[0m')
        msg = "from 0 to {len}.".format(len=len(mappingList))
        print(msg)
        exit()
    if selectIndex == 0:
        print("return empty")
        return {}
    mappingName = mappingList[selectIndex-1]
    fileName="{dirName}/{fName}".format(dirName=mappingFolder,fName=mappingName)
    f = open(fileName)
    mapping = {}
    if f:
        mapping = json.loads(f.read());
    return mapping


def main():
    movieDict = extract()
    mapping = select_mapping()
    reindex(settings=mapping, movieDict=movieDict)
    print("Done for ingesting TMDB data into Elasticsearch")

if __name__== "__main__":
  main()
