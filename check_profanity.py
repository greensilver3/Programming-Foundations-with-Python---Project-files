import urllib
import urllib.request

def read_text():
 quotes = open("/Users/Mac/Documents/movie_quotes.txt")
 contents_of_file = quotes.read()
 print(contents_of_file)
 quotes.close()
 check_profanity(contents_of_file)

def check_profanity(text_to_check):
    query = urllib.parse.urlencode({'q': text_to_check})
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+query)
    output = connection.read()
    print (output)
    connection.close()
    #if (output == "true")
        #print("Profanity Alert !!")
    #elif (output == "false")
        #print("This document has no curse words !")
    #else: 
        #print("Could not scan the document properly.")
read_text()    
