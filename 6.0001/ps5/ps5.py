# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):

    def __init__(self,phrase):
        self.phrase = phrase.lower()

    def is_phrase_in(self,text):
        text = text.lower()

        #Not very efficient O(N^2)
        for i in string.punctuation:
            text = text.replace(i," ")
        text = text.split(" ")

        #Method iterates though list and clear consequtive spaces
#         for i,x in enumerate(text):
#             if x == " ":
#                 while text[i + 1] == " "
#                     del text[i + 1]

        text = [i for i in text if i != ""]
        text = " ".join(text)

        #ERROR 1 was returning true for purple cows simply add a space to the end
        # add " " to end of each - pretty elegent I recon
        if (self.get_phrase() + " ") in (text + " "):
            return True
        else:
            return False

    def get_phrase(self):
        return self.phrase

    def evaluate(self, story):
        #Phrase = one or more words separated by a single space between the words
        #assume no punctuation
        print("called Phrase trigger directly")
        pass




# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
#     def __init__(self,phrase):
#         self.phrase = phrase.lower() #####################DOES THIS NEED TO BE DEFINED???

    def evaluate(self,story):
        return self.is_phrase_in(story.get_title())

# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
#     def __init__(self,phrase):
#         self.phrase = phrase.lower() #####################DOES THIS NEED TO BE DEFINED???

    def evaluate(self,story):
        return self.is_phrase_in(story.get_description())

####################################
# test = PhraseTrigger("Purple COW")
# print(test.is_phrase_in('Purple cows are cool!'))

# titletest = TitleTrigger("purple COW")
# print(titletest.get_phrase())
# sys.exit()
####################################

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
class TimeTrigger(Trigger):
    def __init__(self,timestr):
        # Constructor:
        #        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
        #        Convert time from string to a datetime before saving it as an attribute.
        ### ATRRIBTUE SAVED AS AWARE DT

        #"3 Oct 2016 17:00:10
        self.dt = datetime.strptime(timestr, "%d %b %Y %H:%M:%S")
        self.dt = self.dt.replace(tzinfo=pytz.timezone("EST"))
#         print("TIME ZONE:",self.dt.tzinfo)

    def get_datetime(self):
        return self.dt

    #Make it an abstract class - *already is one as it inherits this from Trigger*
#     def evaluate(self,story):
#         raise NotImplementedError


# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def evaluate(self,story):

        storytime = story.get_pubdate()
        storytime = storytime.replace(tzinfo=pytz.timezone("EST"))

#         print("COMPARISON")
#         print(self.get_datetime().tzinfo)
#         print(storytime)
#         print(storytime.tzinfo)

        if self.get_datetime() > storytime:
            return True
        else:
            return False

class AfterTrigger(TimeTrigger):
    def evaluate(self,story):
        storytime = story.get_pubdate()
        storytime = storytime.replace(tzinfo=pytz.timezone("EST"))

#         print("COMPARISON")
#         print(self.get_datetime().tzinfo)
#         print(storytime)
#         print(storytime.tzinfo)

        if self.get_datetime() < storytime:
            return True
        else:
            return False

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self,othertrigger):
        self.othertrigger = othertrigger

    def evaluate(self,x):
        return not self.othertrigger.evaluate(x)


# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self,trigger1,trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self,x):
        return (self.trigger1.evaluate(x) and self.trigger2.evaluate(x))

# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self,trigger1,trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self,x):
        return (self.trigger1.evaluate(x) or self.trigger2.evaluate(x))


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)

    #return stories

    #fs = filtered stories
    fs = []
    print(type(fs))
    for trigger in triggerlist:
        for story in stories:
            if trigger.evaluate(story):
                fs.append(story)
    return fs


#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)
    # lines is the list of lines that you need to parse and for which you need
    # to build triggers

    triggerlist = {}
    triggerout = []

    #Could implement this method directly after reading but have kept seperate
    #For easier debugging
    for line in lines:
        temp = line.split(",")
        if temp[0] == "ADD":
            for trigger in temp[1:]:
                triggerout.append(triggerlist[trigger])
                print("ADDED TO TRIGGER OUT")
        else:
            trigger_name = temp[0]
            #BE VERY CAREFUL USING EVAL
            #use globals() instead
            trigger_obj = globals()[temp[1].title()+"Trigger"]

            print("TEMP:", temp)
            print(trigger_name)
            print(trigger_obj)

            #NUmber of arguments depends on type of trigger1
            #ASSUMING THAT TRIGGERS ARE PASSED IN ORDER (EASY TO FIX CODE
            # IS JUST CLUNKIER)
            #e.g. AND WILL ALWAYS INCLUDE TRIGGERS THAT COME BEFORE IT AND ADD WILL DO THE SAME
            if temp[1] in ["AND", "OR"]:
                arg1 = triggerlist[temp[2]]
                arg2 = triggerlist[temp[3]]
                triggerlist[trigger_name] = trigger_obj(arg1,arg2)
            elif temp[1] == "NOT":
                arg = triggerlist[temp[2]]
                print(arg)
                triggerlist[trigger_name] = trigger_obj(arg1,arg2)
            else:
                print(temp[2])
                triggerlist[trigger_name] = trigger_obj(temp[2])

            print("TRIGGER LIST ADDITION:",triggerlist[trigger_name])

    return triggerout

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        # t1 = TitleTrigger("Elon")
        # t2 = DescriptionTrigger("New Zealand")
        # t3 = DescriptionTrigger("COVID")
        # t4 = AndTrigger(t2, t3)
        # triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line
        triggerlist = read_trigger_config('triggers.txt')

        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy )
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

#             # Get stories from Yahoo's Top Stories RSS news feed
#             stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
