# summarisePage.py
# Summarises one page at a time
# This is to avoid hitting the rate limit of Gemini 2.5 Flash
import datetime
import sqlite3
from google import genai

# Connect to the database connection and get the cursor
connection = sqlite3.connect('teletextai.db')
cursor = connection.cursor()

# Find if there is a page that has not yet been summarised
cmd = '''SELECT pageNumber, plaintext FROM service
WHERE service.plaintext IS NOT NULL AND service.summary IS NULL
LIMIT 1
'''
cursor.execute(cmd)
result = cursor.fetchone()

# Is there anything to do?
if not result:
  print("None " + str(datetime.datetime.now()))
  exit()
  
# We have a page to do
pageNumber = result[0]
title = "BBC News at " + str(datetime.datetime.now())
txt = "SP,BBC News reformatted by TeletextAI\n"
txt = txt + "DE,"+title+"\n"
txt = txt + "PN,"+str(pageNumber)+"00\n" # TODO [!] Should cope with multiple subpages  
txt = txt + "PS,8000\n"
txt = txt + "OL,0,TemplateXENOFAX  %%# %%a %d %%bC%H:%M/%S\n"
txt = txt + "OL,1,Wj#3kj#3kj#3kT]S   |hh4|,|h<l4| h<l0    \n"
txt = txt + 'OL,2,Wj $kj $kj \'kT]S   ozz%pj7k4pjuz%    \n'
txt = txt + "OL,3,W\"###\"###\"###T/////-,,/,,,-.-.,,-,,/////\n"
txt = txt + "OL,4,                                       \n"

#print(result[1]) 
print("Summarising page = " + str(pageNumber))

# Summarise the story using AL

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

request = '''Summarise the story that follows the colon. 
Use natural upper and lower case text and preserve the capitalization of proper nouns.
Reduce it to fit 15 lines of 39 columns suitable for a teletext page.
The last sentence should be finished and not truncated.
The first sentence should be a paragraph on its own. In the rest of the text there should be one or two more paragraphs to break up the text:
'''+result[1]
response = client.models.generate_content(
    model="gemini-2.5-flash-lite", contents=request
)

# Put the response text into the database
# Actually we don't care about keeping the response once we have made the page.
# For now just store a small bit of it.
# It needs to be not NULL so it won't make the AI repeat the summary.
cmd = '''UPDATE service
SET summary = ?
WHERE pageNumber = ?
'''
cursor.execute(cmd, (response.text[0:40], str(pageNumber)) )

# Commit the changes in database and close the connection
connection.commit()
connection.close()

print(response.text)
lineNumber = 5
colour = "G"
for line in response.text.splitlines():
  print("line = " + line)
  txt = txt + "OL," + str(lineNumber) + "," + colour + line + "\n"
  if line == "":
    colour = "F"
  lineNumber = lineNumber + 1
  if lineNumber > 21:
    break

txt = txt + "OL,22,D]CHome news digestG141CWorld digestG142\n"
txt = txt + "OL,23,D]CNews IndexG102CFlashG150CRegionalG160\n"
txt = txt + "OL,24,ANext NewsBNews IndxCHeadlinesFMain Menu\n"
txt = txt + "FL,"+str(pageNumber+1)+",101,8ff,100,8ff,8ff\n"
with open("/var/www/private/onair/xenofax/p" + str(pageNumber)+ ".tti", "w") as f:
  f.write(txt)
# print(txt)

print("summarisePage.py finished run at " + str(datetime.datetime.now()) + "  Added page " + str(pageNumber))
