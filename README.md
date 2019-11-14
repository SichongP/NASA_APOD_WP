# NASA_APOD_WP
Set Astronomy Picture Of the Day (APOD) as wallpaper on ubuntu

Simply run NASA_APOD_WP.py
It will create a directory `~/NASA_APOD` and download picture of the day to that directroy (named as `yyyy-mm--dd.jpg`) unless said file already exists, in which case it does nothing.
After downloading the file, it sets it as wallpaper on ubuntu system.
Windows support to come.

To automatically change wallpaper, consider adding following lines to `~/.bashrc`:
```
# Change Wallpaper
today=$(date --rfc-3339=date)
if [ ! -f ~/NASA_APOD/${today}.jpg ]; then
        echo "Getting today's Wallpaper? [Y/N]"
        read resp
        if [ "$resp" == "Y" ] || [ "$resp" == "y" ] || [ "$resp" == "yes" ] || [ "$resp" == "YES" ] || [ "$resp" == "Yes" ]; then
                NASA_APOD_WP.py
        fi
fi
```

This will invoke a prompt everytime you start a terminal (only) when your wallpaper if not up to date.
