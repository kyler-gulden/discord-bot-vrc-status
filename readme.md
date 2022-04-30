Code used to get VRChat server status, then format it as a Discord embed when /vrcstat is called.

Using Rapptz's Discord.py https://github.com/Rapptz/discord.py
Also using Beautiful Soup https://www.crummy.com/software/BeautifulSoup/

old.py is the first version of the file, so please be gentle when reviewing it. I'm going to try and make the server status loop and check for changes, then notify appropriate channels when the status changes.

Example of output:

![image](https://user-images.githubusercontent.com/44349780/166114024-40096d43-dff3-4656-ac63-9f8b796f190a.png)
