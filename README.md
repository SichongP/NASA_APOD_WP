# NASA_APOD_WP
Set Astronomy Picture Of the Day (APOD) as wallpaper on ubuntu

Simply run NASA_APOD_WP.py
It will create a directory `~/NASA_APOD` and download picture of the day to that directroy (named as `yyyy-mm--dd.jpg`) unless said file already exists, in which case it does nothing.
After downloading the file, it sets it as wallpaper on ubuntu system.
Windows support to come.

Add `python /path/to/script/NASA_APOD_WP.py` to `~/.bash_profile` to automatically run this whenever a login shell is called. (Or add it to `~/.bashrc` if you so wish.)
