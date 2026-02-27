# makenews-node

Node scripts to generate teletext news pages from an RSS feed. On the tenth anniversary of the makenews, this is a rewrite for Node.js.

# Files
```
createDB.py - Create the database
phase1.sh - make the simple teletext pages from the rss feed
  |-- feed.py - Read the rss feed into the database
  |-- updateService.py - Take the RSS data from the database and make summary teletext pages
         |-- CreatePage2.py - Make a simple teletext page directly from the RSS data.   
         |-- extract_bbc_story.py - Loads the full story from the RSS link into the database
updateIndex.py - Write the teletext index page
   |-- createIndex.py - Old single page version, not used
   |-- createIndex2.py - Generate BBC style index page, carouselling if needed
summarisePage.py - Summarises a single teletext page. Converts a simple summary page into a full story using AI.
```
# Installing on Linux
(Installing on Windows is pretty much the same using Powershell)

Required packages among others are git, python3.
Check that python 3 is at least 3.11.2 and install other packages. Create the python3 environment that we will use for this project.
```
sudo apt update
sudo apt upgrade
python3 --version
sudo apt install python3-bs4
```
## Install makenews-node source code
Install the source code in the home directory and set up the python3 environment
```
cd ~
git clone https://github.com/peterkvt80/makenews-node.git
cd makenews-node
python3 -m venv newsenv
```
When we want to use this environment we can use the source command first. Always remember to source the environment before running python. Here we install some packages 
```
# Before running any code, always do these two instructions
cd ~/makenews-node
source newsenv/bin/activate
# Install these packages
pip install beautifulsoup4
pip install google-genai
pip install feedparser
```
# First time run

Create the database. When you run this it will wipe all data. Only run this once when setting up, or to reset things during development.
```python3 createDB.py```
This will create the SQLite database file ```teletextai.db```
Then make this script executable for later.
```chmod +x phase1.sh```
# Set up the feed
To specify which feed you are using, edit url in feed.py. For the BBC UK edition you can use
ls /var/www
```url = 'https://feeds.bbci.co.uk/news/rss.xml?edition=uk'```
Check that the feed works.
```python3 feed.py```
This should show a list of the decoded RSS feed.python3 

# Make simple service
To set up the destination for the pages, edit updateService.py. The call to createPage2 has the destination directory as the first parameter.
```  teletext = createPage2("/var/www/onair/",slotNumber, guid, title, description, link)```
and then make sure that the destination exists. Because this location is owned by root we need to sudo it.
```sudo mkdir /var/www/onair```
Check that this runs. (sudo because root owns it)
```sudo python3 updateService.py```
This will show what is being generated and there should be no errors.

The destination folders should have the generated teetext pages.
# Make the index
Specify the output file by editing createIndex2.py.
```with open("/var/www/onair/p101.tti", "w") as f:```
Test that it works
```sudo python3 updateIndex.py```
# Automate the simple service
If those scripts worked then we can arrange to automate it.

Edit phase1.sh and put in the full path to your python3 interpreter. Then you can run it.
```sudo ./phase1.sh```
If there are no errors then you can create a crontab to run them automatically.
*/10 * * * * cd /home/peterk/makenews-node && ./phase1.sh
* 1 * * * cd /home/peterk/makenews-node && /home/peterk/makenews-node/newsenv/bin/python3 summarisePage.py


# Make full pages

This requires AI. You'll need to sign up and get a certificate and maybe pay if you are going to be doing more than a couple of pages per day.
```summarisePage.py```
# Get a certificate
