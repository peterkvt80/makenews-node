############################# OLD VERSION. Only does one page
############################# Use createPage2.py
# createIndex.py>
# Creates a new index page
from textwrap import wrap

# function
def createIndex(storyList):
  txt = "SP,Source and date go here TBA\n"
  txt = txt + "DE,News index page\n"
  txt = txt + "PN,10100\n" # TODO [!] Should cope with multiple subpages  
  txt = txt + "PS,8000\n"
  txt = txt + "OL,0,TemplateXENOFAX  %%# %%a %d %%bC%H:%M/%S\n"
  txt = txt + "OL,1,Wj#3kj#3kj#3kT]S   |hh4|,|h<l4| h<l0    \n"
  txt = txt + 'OL,2,Wj $kj $kj \'kT]S   ozz%pj7k4pjuz%    \n'
  txt = txt + "OL,3,W\"###\"###\"###T/////-,,/,,,-.-.,,-,,/////\n"
  txt = txt + "OL,4,                                       \n"
  # For now lets just use the description for testing
  # In future we will...
  # Fetch the story from the link, translate it and format it into a story
  # TODO[!] Teletext escapes
  line = 5
  lineLength = 0
  for title, pageNumber in storyList:
    titleText = wrap(title + " nnn", width=39)
    # record the length of this line so we can backtrack if we go over
    storyLength = len(txt)
    for titleLine in titleText:
      txt = txt + "OL," + str(line) + ",C" + titleLine + "\n" # yellow title
      line = line + 1
      lineLength = len(titleLine)
    print("LineLength = " + str(lineLength) + " titleLine = <" + titleLine + ">")
    txt = txt + "\n"    
    if line > 20:
      txt = txt[0:storyLength] # truncate the story so we don't crash into the footer
      # todo Wrap onto another page
      break
    line = line + 1
    print("LineLength = " + str(lineLength))
    # add the page number
    textLength = len(txt) # how long is txt so far?
    txt = txt[0:textLength - 6] # chop the last five characters " nnn\n" (because the last character is also a space?)
    # pad the line to 35 characters
    padding = "                                        "[0:39 - lineLength]    
    txt = txt + padding + "G" + str(pageNumber) + "\n"
  #line = 4
  #for storyLine in storyText:
    #txt = txt + "OL," + str(line) + ",C" + storyLine+"\n"
    #line = line + 1
#  
  #line = line + 1
  #storyText = wrap(description, width=39)
  #for storyLine in storyText:
    #txt = txt + "OL," + str(line) + ",F" + storyLine+"\n"
    #line = line + 1
    # TODO [1] If line > 23 or whatever, then exit loop or better still start the next subpage
  txt = txt + "OL,22,D]CHome news digestG141CWorld digestG142\n"
  txt = txt + "OL,23,D]CNews IndexG102CFlashG150CRegionalG160\n"
  txt = txt + "OL,24,ANext NewsBNews IndxCHeadlinesFMain Menu\n"
  txt = txt + "FL,102,100,8ff,8ff,8ff,8ff\n"
  print(txt)
  with open("/var/www/private/onair/xenofax/p101.tti", "w") as f:
    f.write(txt)
    
  #print(txt)
  return txt