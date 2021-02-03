import json
from difflib import SequenceMatcher
from difflib import get_close_matches

loadfile=open("data.json")
data = json.load(loadfile)
loadfile.close()


def SearchWord(word):
    try:
        
        if word in data:
            return data[word]

        elif get_close_matches(word , data.keys()):
            newWord=get_close_matches(word , data.keys())[0]

            inputs= input( "Are you looking for word : %s  Y/N : " %newWord).upper()

            if(inputs=="Y"):
              return data[newWord]
            elif inputs=="N":
              return "Please try again with new word"
            else:
                return   "We did not understand your response. Please try again from the start"
                
        else:
            "No matches found for your word"
    except:

        return "some error occured"
i="Y"
while i =="Y":

        output=SearchWord(input("Enter word to search :").lower())

        if type(output)== list:
            for s in output:
               print(s)
        else:
             print(output) 

        i = input("To continue press Y :") .upper()






