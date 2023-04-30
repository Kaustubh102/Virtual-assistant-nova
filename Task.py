import datetime
from speak import Say

def Time():
    time=datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date=datetime.date.today()
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)


def NonInputExecution(query):

    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()
    elif "day" in query:
        Day()    
    

def InputExecution(tag,query):
    if "wikipedia" in tag:
      name =str(query).replace("who is","").replace("about","").replace("who is","").replace("what is","").replace("Tell me about","").replace("what is the meaning of","").replace("What is meant by","")
      import wikipedia
      result = wikipedia.summary(name)
      Say(result)

    elif "google" in tag:
        query =str(query).replace("google","")
        query=query.replace("search","")
        import pywhatkit
        pywhatkit.search(query)















