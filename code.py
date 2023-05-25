import json
with open('jsonstuff.json', 'r') as f:
    data = json.load(f)
#print(data)
questions = []
answer  = []

for file in
for x in range(len(data['questions'])):
    
    questions.append(data['questions'][x]["question"])
    answer.append(data['questions'][x]["answer"])
for x in range(len(questions)):
    print(questions[x], answer[x])

promptss = ["answer this latin", "latin am i right?"]
outerdict = {}
outerdict["stuff"] = []


for x in range(len(questions)):
    innerdict = {}
    innerdict["question"] = questions[x]
    innerdict["answer"] = answer[x]
    innerdict["prompt"] = []
    innerdict["code"] = []
    for prompts in promptss:
        stringg = (prompts + " " + questions[x]) 
        string = (prompts + " " + questions[x] + " " + "[ANSWER] ") 
        newstring = 'argmax"' + string + '" from "openai/text-ada-001"'
        #create json file for code
        finalname = str(x) + prompts + ".lmql"
        f = open(finalname, "w")
        f.write(newstring)
        innerdict["prompt"].append(stringg)
        innerdict["question"] = questions[x]
        innerdict["code"].append(newstring)
        #finalname = str(x) + prompts + ".txt"
        #f = open(finalname, "w")
        #f.write(newstring)
    outerdict["stuff"].append(innerdict)  
with open("sample.json", "w") as outfile:
    json.dump(outerdict, outfile)


    #to do list
    #match prompts w types of questions (type a gets type a prompts) and then when we extract we need to preserve that
    #add for loop to iterate thru the prompts and the quiz jsons 
    #more pseudocode added to iraj's version, variable names n stuff commented out as well. use that version for future work 
