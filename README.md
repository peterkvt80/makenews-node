# makenews-node

Node scripts to generate teletext news pages from an RSS feed.

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
# Installing

[How to install the scripts and the python environment]

# First time run

Create the database. When you run this it will wipe all data. Only run this once when setting up, or to reset things during development.
```python createDB.py```
# Set up the feed
To specify which feed you are using, edit url in feed.py. For the BBC UK edition you can use

```url = 'https://feeds.bbci.co.uk/news/rss.xml?edition=uk'```

# Make simple service

The simple service just makes summary pages using the RSS feed only.
```./phase1.sh```


# Make full pages

This requires AI. You'll need to sign up and get a certificate and maybe pay if you are going to be doing more than a couple of pages per day.
