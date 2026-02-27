#!/bin/sh
#
# phase1.sh
# Runs the scripts required to get a basic set of teletext pages.
# To automate this your crontab should look like this but change the file paths to match your system.
# */10 * * * * cd /home/peterk/news && phase1.sh
# or if you want to log everything
# GEMINI_API_KEY=<your key here if you are running summarise>
# */10 * * * * cd /home/peterk/news && ./phase1.sh   >> /home/peterk/news/cron_debug2.log 2>&1
# * 1 * * * cd /home/peterk/news && /home/peterk/news/news/bin/python3 summarisePage.py  >> /home/peterk/news/cron_debug.log 2>&1
# feed.py - reads the rss into the database
/home/peterk/news/news/bin/python3 feed.py
# updateService.py - Manages adding new teletext pages, removing old ones and allocating page numbers.
/home/peterk/news/news/bin/python3 updateService.py
# updateIndex.py - Rebuilds the teletext index page
/home/peterk/news/news/bin/python3 updateIndex.py
