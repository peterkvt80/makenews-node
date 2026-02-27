# updateService.py
# Manages the service table
# The basic pages are written out using the headings.
import datetime
import sqlite3
import json
from createPage2 import *
from extract_bbc_story import *


# Connect to the database connection and get the cursor
connection = sqlite3.connect('teletextai.db')
cursor = connection.cursor()

###################### STAGE 1
# Delete slots that are no longer used
# Find service.guid that is not in story.guid 
# and service.guid IS NOT NULL but story.guid IS NULL

print("STAGE 1\n")
cmd = '''SELECT pageNumber FROM service
    LEFT JOIN story ON service.guid = story.guid
WHERE story.guid IS NULL AND service.guid IS NOT NULL
'''
cursor.execute(cmd)

#################### STAGE 1A
# delete the service pages that no longer exist in the rss feed

# probably could do this in a compound statement if I studied SQL for a bit
pagesToDelete=(cursor.fetchall())
pn = 0
for page in pagesToDelete:
  pn = page[0]
  print(pn)
  cmd = '''UPDATE service
  SET guid = NULL, summary = NULL
  WHERE pageNumber='''
  cmd = cmd + str(pn)
  print("deleting:" + cmd)
  cursor.execute(cmd)

######################## STAGE 2
# Are there story.guids that are not in service.guid?
print("STAGE 2\n")
cmd = '''SELECT story.guid,title,description,link FROM story
LEFT JOIN service ON service.guid = story.guid
WHERE service.guid IS NULL
'''
cursor.execute(cmd)
newPages=cursor.fetchall()
print(newPages)

##################### STAGE 2A
# Find the available slots
print("STAGE 2A\n")
cmd = '''SELECT pageNumber FROM service
WHERE service.guid IS NULL
'''
cursor.execute(cmd)
freeSlots=cursor.fetchall()
print(freeSlots)
slot=0

#################### STAGE 3
# Put pages in available slots
# TODO. Probably a SQLite way of populating service that isn't a bit of python
print("STAGE 3\n")
for (guid, title, description, link) in newPages:
  # find an empty page slot number
  slotNumber = freeSlots[slot][0]
  slot=slot+1
  # TODO [!] quit if we run out of slots
  
  story = extract_bbc_story(link) # Fetch the plain text story from the web link
    
  # make and save a tti page based on page number, title, description and link 
  # We create the teletext page in two stages.
  # The first just shows the RSS description
  # Later the plaintext story processed by AI for translation, summarising and formatting.
  # Why? Because we are using the free tier of Gemini 2.5 Flash Lite and we need to do rate limiting.
  # especially requests per minute
  
  teletext = createPage2("/var/www/onair/",slotNumber, guid, title, description, link)
  
  cmd = '''UPDATE service
  SET guid = ?,
  plaintext = ?,
  summary = NULL
  WHERE pageNumber = ?
  '''
  #cmd = 'UPDATE service '
  #cmd = cmd + 'SET guid  = \'' + guid  + '\', '
  #cmd = cmd + 'plaintext = ' + json.dumps(story) + ', ' # plaintext story is saved here for later
  #cmd = cmd + 'summary = NULL ' # summary will be generated later from plaintext
  #cmd = cmd + 'WHERE pageNumber = ' + str(slotNumber)
  #print("cmd = " + cmd)
  cursor.execute(cmd, (guid, story, str(slotNumber)) )
  
  # update guid and teletext into service 
  #print(str(freeSlots[slot][0])+': '+guid)
  #print("\n")


# Get a list of free transmission slots

# Get a list of unpublished stories

# For each free slot:
#   Allocate a story to the slot
#   Render the story and give it a slot based filename eg. RUSNEWS100.tti
#   Skip if out of slots or out of stories

# Make an index page

# What does the service table look like now?
#cmd = ''' SELECT pageNumber, guid FROM service WHERE guid IS NOT NULL'''
#cursor.execute(cmd)
#result=cursor.fetchall()
#print(result)

# Commit the changes in database and close the connection
connection.commit()
connection.close()

print("updateService.py finished run at " + str(datetime.datetime.now()) + "  Added " + str(slot) + " new pages")

