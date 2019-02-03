from newsapi import NewsApiClient
import json
import csv
from nltk.corpus import sentiwordnet as swn
import os
import math
from time import gmtime,strftime, localtime

# string -> float
# description -> score

def score(lst):
    print(lst)
    if(lst == None):
        return 0
    if(lst[3] == "pos"):
        return lst[2]
    else:
        return lst[0]*-1

def scorer(desc):
    if(desc ==None):
        return None

    command = "curl -d " + '"text='+desc + '" http://text-processing.com/api/sentiment/ >  data.txt'
    os.system(command)
    print(command)

    f = open("data.txt","r")
    result = f.readline().strip()

    saving =False
    temp =""
    scores =[]
    
    for chars in result:
        if chars =="0":
            saving =True
        if saving and chars != "," and chars !="}":
            temp+= chars
        elif saving:
            scores.append(float(temp))
            saving = False
            temp=""
    try:
        scores.append(result.split('label')[1][4:7])
        if(scores[3]=="neu" and scores[0] >scores[2] ):
            scores[3]="neg"
        else:
            scores[3]="pos"
    except:
        print("NONE")
        return None

    return scores


def scrape(q=None, language=None, country = None, category= None, sources= None,from_param= None, to= None, pageSize= None, page= None, long = False, h_balance = 0.5):

    newsapi = NewsApiClient(api_key='2d4d70291f5548bb8c6776f5ddeefd25')

    everything = newsapi.get_everything (q=q,language=language,country=country,category=category,sources=sources,page_size=pageSize, page=page, from_param=from_param, to=to)

    #to = '%4d-%02d-%02dT%02d:%02d:%02d' % (year, month, day, hour, minute, second)
    #from_param = '%4d-%02d-%02dT%02d:%02d:%02d' % (year, month, yesterday, hour, minute, second)
    
    every_parsed =  json.dumps(everything, ensure_ascii=False)
    every_data = everything['articles']

    #print(strftime("%Y-%m-%dT%H:%M:%S" , (localtime()-86400)))
    csv_name = "CSVs/" + q+"-"+str((strftime("%Y-%m-%d-%H:%M:%S" , localtime())))+".csv"

    every_data = open(csv_name, "w")

    csvwriter = csv.writer(every_data)

    count = 0

    tot_t = []
    tot_d = []
    tot_date = []
    urls = []
    total =0
    for i in every_data:

        if count == 0:
            header = list(i.keys())

            lst2 = ["t_score", "d_score"]
            header.extend(lst2)

            csvwriter.writerow(header)

            count += 1
        if i['url'] in urls:
            pass
        else:
            total+=1
            urls.append(i['url'])
            t_score = score(scorer(i['title']))
            d_score = score(scorer(i['description']))
            date_score = score(scorer(i['from_param'])
            
            if t_score != 0:
                tot_t.append(t_score)
            if d_score !=0:
                tot_d.append(d_score)
            if date_score !=0:
                tot_date.append(date_score)
            
            lst2 = list(i.values())
            lst2.extend([t_score,d_score])

            csvwriter.writerow(lst2)
    title_score, descr_score = 0,0
    if len(tot_t) >0:
        title_score = sum(tot_t) / len(tot_t)
    if len(tot_d) >0:
        descr_score = sum(tot_d) / len(tot_d)
    avg_score = (title_score *h_balance + descr_score * (1- h_balance))

    
    label =""

    if avg_score > 0:
        label = "Positive"
    elif avg_score <0 :
        label = "Negative"
    else:
        label = "Neutral"

    if avg_score ==0 and title_score ==0 and descr_score ==0:
        print("Nothing found")
    else:
        print("Recent sentiment is %s with a score of %.5f.\nTotal Articles: %d\nTitle score: %.4f.\nDescription score: %.4f" % (label, avg_score, total, title_score, descr_score ))

        if long:
            return [label,avg_score, title_score, descr_score]
        else:
            return avg_score
    every_data.close()

def main():
    #print(scorer("your waifu is trash"))
     schedule.every(1).hour
     test = scrape("Tesla", category="business", from_param="2019-02-02T0:00:01" )
     
if __name__ == "__main__":
    main()
