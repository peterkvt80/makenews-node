# createPage.py>
# Creates a teletext page
# Reads the link then summarises it to fit
# This is an intermediate stage where just the summary text is shown.
# Later we replace the RSS summary text with an AI summary of the whole story.
from textwrap import wrap
import os

# function
def createPage2(dir_path, slotNumber, guid, title, description, link):
  print("THIS IS CREATE PAGE 2")
  txt = "SP,"+guid+"\n"
  txt = txt + "DE,"+title+"\n"
  txt = txt + "PN,"+str(slotNumber)+"00\n" # TODO [!] Should cope with multiple subpages  
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
  storyText = wrap(title, width=39)
  line = 4
  for storyLine in storyText:
    txt = txt + "OL," + str(line) + ",C" + storyLine+"\n"
    line = line + 1
  
  line = line + 1
  storyText = wrap(description, width=39)
  for storyLine in storyText:
    txt = txt + "OL," + str(line) + ",F" + storyLine+"\n"
    line = line + 1
    # TODO [1] If line > 23 or whatever, then exit loop or better still start the next subpage
  txt = txt + "OL,22,D]CHome news digestG141CWorld digestG142\n"
  txt = txt + "OL,23,D]CNews IndexG102CFlashG150CRegionalG160\n"
  txt = txt + "OL,24,ANext NewsBNews IndxCBack     FMain Menu\n"
  txt = txt + "FL," + str(slotNumber + 1) + ",101," + str(slotNumber - 1) + ",100,8ff,8ff\n"
  print(txt)
  if not os.path.exists(dir_path):
      os.makedirs(dir_path)
      print("Directory created successfully!")  
  filename = dir_path + "p" + str(slotNumber) + ".tti"
  print("filename = " + filename)
  with open(filename, "w") as f:
    f.write(txt)
    
  #print(txt)
  return txt