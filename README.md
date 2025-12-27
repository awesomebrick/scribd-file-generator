# scribd_file_gen.py
v0.1.0 initial upload.

## about

a few years ago, i noticed that any time i wanted to download a file off of Scribd, they would be begging for you to upload a few files *first* (with some strange reccomendations/requirements) or instead pay a ridiculous cost of $12 a month (after the obligatory free month!!). i uploaded a few files that i had, and upon scribd telling me that those files were already on scribd and therefore not eligible, it became glaringly obvious to me that scribd was begging for any and every text-based file it could get its hands on... so that it could use it all as material for LLMs to scrape data from. this information is not made clear on the upload page, and is instead buried in the "Uploader Agreement", as shown below.

<img src="LLMrights.png" width="75%"/>

those who know me know how I feel about AI data scraping, especially with such a predatory model. it's as if they're holding a gun to your head saying, "either pay us money, or give us even more of your data to scrape." sure, maybe calling the downloading of some sheet music a gun to one's head is a bit of an overexaggeration, but that's how it feels in regards to the current AI-bubble-driven climate.

today (the date of the inital commit), i had to download another file and it appears that they now require less files, but longer files. i figured now was a good as time as any to upload this to a public repository for others to use. it's also probably nice to have on a public portfolio.

## usage
(v0.1.0)

as of now, the usage of the script is fairly easy. simply run
```
python3 scribd_file_gen.py
```
and the script will dunk 5 .txt files, each 2800 characters in length (scribd now requires 3 files 2700 in length) into the directory the script is in.

i'll be adding some more command line functionality, unique file naming, etc. in the next couple of days.

### todo
---
- argparse for cmdline args
- unique filenames
- files into seperate folder
  - clean that folder on next run