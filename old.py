import discord
import requests
from bs4 import BeautifulSoup
from keys import * # File that contains my Discord Bot Token

class serverStatus:
        
    def __init__(self):
        
        self.embedTitleText = 'Website unreachable' # Title text, without formatting
        self.embedTitleEmoji = '❌' # Emoji to describe the current embedTitleText
        self.embedDescription = 'For more visit the [Official VRC Status Page](https://status.vrchat.com/).' # A description item in the embed
        self.embedColor = 0xDD2E44 # Hex color used for the vertical stripe on Discord embeds
        self.embed = None
        self.serviceStatusItems = []
        #Since this is static, and does not change, it should be moved outside of this class as instanceation will potentially eat up memory
        self.knonwLocations = {"USA, West (San José)": "🇺🇸",
                              "USA, East (Washington D.C.)": "🇺🇸",
                              "Europe (Amsterdam)": "🇪🇺",
                              "Japan (Tokyo)": "🇯🇵"}

    def getEmbedTitleText(self):
        return self.embedTitleText

    def setEmbedTitleText(self,title):
        self.embedTitleText = title

    def getEmbedTitleEmoji(self):
        return self.embedTitleEmoji

    def setEmbedTitleEmoji(self,emoji):
        self.embedTitleEmoji = emoji

    def getEmbedDescription(self):
        return self.embedDescription

    def setEmbedDescription(self,description):
        self.embedDescription = description

    def getEmbedColor(self):
        return self.embedColor

    def setEmbedColor(self,hexcolor):
        self.embedColor = hexcolor

    def getSubStatusItems(self):
        return self.serviceStatusItems

    def addSubStatusItem(self,item):
        self.serviceStatusItems.append(item)

    def getEmbed(self):
        return self.embed

    def generateEmbed(self): # Generate the Discord.py Embed object and add relevant formatting, fields, etc.
        self.embed = discord.Embed(
                title=f'{self.embedTitleEmoji} VRC Status: __ {self.embedTitleText} __ {self.embedTitleEmoji}', description=self.embedDescription, color=self.embedColor)
        for serviceAndStatus in self.serviceStatusItems: # Foreach of the services or server locations, loop through and apply proper formatting, then append their field to the Embed object
            if serviceAndStatus[1] != 'Operational':         
                serviceAndStatus[1] = f'😹 {serviceAndStatus[1]}'
            if serviceAndStatus[0] in self.knonwLocations.keys():
                self.embed.add_field(name=f'{self.knonwLocations[serviceAndStatus[0]]} {serviceAndStatus[0]}', value=f'• {serviceAndStatus[1]}', inline=False)
            else:
                self.embed.add_field(name=serviceAndStatus[0], value=f'• {serviceAndStatus[1]}', inline=False)

print("Starting bot...")
client = discord.Client()

@client.event
async def on_ready():
    print("Bot running...")

@client.event
async def on_message(message):

    if message.content.casefold().startswith('/vrcstat'):
        status = serverStatus()
        uri = "https://status.vrchat.com/"
        # This try seems pretty jank, might try to find a more pythonic way to work with this?
        try:
            webresponse = requests.get(uri)
            statuscode = webresponse.status_code
        except:
            statuscode = 0
        if statuscode == 200: 
            soup = BeautifulSoup(webresponse.content, "html.parser")
            # Get the primary status text
            status.setEmbedTitleText((soup.find("div", class_="section-status").text.strip()))
            if status.getEmbedTitleText() == 'All systems are operational':
                status.setEmbedColor(0x77B255)
                status.setEmbedTitleEmoji('✅')
            elif status.getEmbedTitleText() == "Some systems are experiencing issues":
                status.setEmbedColor(0xFFCC4D)
                status.setEmbedTitleEmoji('⚠️')
            else:
                status.setEmbedColor(0xDD2E44)
                status.setEmbedTitleEmoji('❌')
            # Get all sub-item names and statuses
            serviceStatuses = soup.find_all("li", class_="list-group-item sub-component")
            for service in serviceStatuses:
                itemToAdd = ((service.text.strip()).replace("\n", "")).split("            ")
                status.addSubStatusItem(itemToAdd)
        status.generateEmbed()
        await message.channel.send(embed=status.getEmbed()) # Always called, will use the default serverStatus attribs. if the webrequest fails
    
client.run(clientToken)