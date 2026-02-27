# createIndex2.py>
# Creates a BBC style index page
# Called from updateIndex.py
from textwrap import wrap

# function
def createIndex2(storyList):
  pageTotal = pass1(storyList) # how many pages?
  currentPage = 1 
  txt = metaHeader() #
  line = 5
  MAXLINE = 20
  # TODO[!] Teletext escapes
  lineLength = 0 # The length of the last line in a story (is there enough space for the page number?)
  txt = txt + pageHeader(currentPage, pageTotal)  
  for title, pageNumber in storyList:

    titleText = wrap(title + " nnn", width=39) # The next title. The nnn gets chopped off later.

    storyLines = len(titleText) # how many lines in this title?
    if line + storyLines > MAXLINE: # Next carousel page
      txt = txt + footer() # finish this page
      currentPage = currentPage + 1
      txt = txt + pageHeader(currentPage, pageTotal)
      line = 5
    for titleLine in titleText:
      txt = txt + "OL," + str(line) + ",C" + titleLine + "\n" # yellow title
      line = line + 1
      lineLength = len(titleLine) 
    # add the page number
    textLength = len(txt) # how long is txt so far?
    if lineLength < 40:
      txt = txt[0:textLength - 5] # chop the last five characters " nnn\n" (because the last character is also a space?)
      # pad the line to 35 characters
      padding = "                                        "[0:39 - lineLength]    
    else:
      line = line + 1
      padding = "                                   "
      txt = txt + "OL," + str(line) + ",C"
    txt = txt + padding + "G" + str(pageNumber) + "\n"
    line = line + 1
  txt = txt + footer()
    
  print(txt)
  with open("/var/www/onair/p101.tti", "w") as f:
    f.write(txt)
    
  #print(txt)
  return txt
  
# @brief pass1 - Work out number of carousel pages
# @param storyList - Array of story titles
# @return Number of carousel pages in this list
def pass1(storyList):
  pages = 1
  line = 5
  MAXLINE = 20
  for title, pageNumber in storyList:
    titleText = wrap(title + " nnn", width=39)
    if (line + len(titleText) ) > MAXLINE: # Did we run out of lines?
      pages = pages + 1 # skip to the next page
      line = 5 + len(titleText) + 1 # add the lines of this story to the next page
    else:
      line = line + len(titleText) + 1 # Keep on accumulating lines on this page
  print("pass1 - total number of pages in this carousel = " + str(pages))
  return pages

# The initial per file lines at the top of a tti.
def metaHeader():
  txt = "SP,Source and date go here TBA\n"
  txt = txt + "DE,News index page\n"
  return txt

# The top part of the page down to the page index
def pageHeader(currentPage, pageTotal):
  if pageTotal <= 1:
    currentpage = 0
  txt = "PN,101{:02d}".format(currentPage) + "\n"
  #txt = "PN,10100\n" # mppss. ss = Current subpage starting from 01
  txt = txt + "CT,11,T\n"
  txt = txt + "PS,8000\n"
  txt = txt + "OL,0,TemplateXENOFAX  %%# %%a %d %%bC%H:%M/%S\n"
  txt = txt + "OL,1,Wj#3kj#3kj#3kT]S   |hh4|,|h<l4| h<l0    \n"
  txt = txt + 'OL,2,Wj $kj $kj \'kT]S   ozz%pj7k4pjuz%    \n'
  txt = txt + "OL,3,W\"###\"###\"###T/////-,,/,,,-.-.,,-,,/////\n"
  if pageTotal <= 1:
    txt = txt + "OL,4,                                       \n" # one page
  else:
    txt = txt + "OL,4,                                     " # one page
    # assume pageTotal is less than 10
    txt = txt + str(currentPage) + "/" + str(pageTotal) + "\n"
  return txt

# The bottom part of the page  
def footer():
  txt = "OL,22,D]CHome news digestG141CWorld digestG142\n"
  txt = txt + "OL,23,D]CNews IndexG102CFlashG150CRegionalG160\n"
  txt = txt + "OL,24,AFirst News  BTriumphs  CDuties  FHome\n"
  txt = txt + "FL,102,130,200,100,8ff,8ff\n"
  return txt
  
