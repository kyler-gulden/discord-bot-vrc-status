Code used to get VRChat server status, then format it as a Discord embed when `/vrcstat` is called.

Using Rapptz's Discord.py https://github.com/Rapptz/discord.py and Crummy Beautiful Soup https://www.crummy.com/software/BeautifulSoup/

old.py is the first version of the file, so please be gentle when reviewing it. I'm going to try and make the server status loop and check for changes, then notify appropriate channels when the status changes.

Depending on the status of the service, the status will be displayed differently.

Example of output:

![image](https://user-images.githubusercontent.com/44349780/166114024-40096d43-dff3-4656-ac63-9f8b796f190a.png)

![image](https://user-images.githubusercontent.com/44349780/184271777-b1f0b8ce-202a-4e01-9ffd-f4336c52193c.png)

![image](https://user-images.githubusercontent.com/44349780/184271989-e43debd3-edcc-4c4f-81d0-c8b017644560.png)
