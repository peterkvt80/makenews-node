# makenews-node

Node scripts to generate teletext news pages from an RSS feed.

# Files

   createDB.py
   createIndex.py
   createIndex2.py
   extract_bbc_story.py
   feed.py
   pages1.sh
   summarisePage.py
   summarisePage.sh
   updateIndex.py
   updateService.py

# Installing

[How to install the scripts and the python environment]

# First time run

Create the database. When you run this it will wipe all data. Only run this once when setting up, or to reset things during development.
   python createDB.py
# Set up the feed
To specify which feed you are using, edit url in feed.py. For the BBC UK edition you can use

    url = 'https://feeds.bbci.co.uk/news/rss.xml?edition=uk'

# Make simple service

The simple service just makes summary pages using the RSS feed only.
./phase1.sh


# Make full pages

This requires AI. You'll need to sign up and get a certificate and maybe pay if you are going to be doing more than a couple of pages per day.
