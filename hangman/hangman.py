import discord
import os
from datetime import datetime
from discord.ext import commands

from .utils.dataIO import dataIO
from .utils import checks

try: # check if BeautifulSoup4 is installed
    from bs4 import BeautifulSoup
    soupAvailable = True
except:
    soupAvailable = False
    
class hangman:
    def __init__(self, bot):
        self.bot = bot
        self.path = "data/Fox-Cogs/hangman"
        self.file_path = "data/Fox-Cogs/hangman/hangman.json"
        self.the_data = dataIO.load_json(self.file_path)
        #self.hanglist = ("_","H","HA","HAN","HANG","HANGM","HANGMA","HANGMAN")
        self.hanglist = (
        """
           _________
            |/        
            |              
            |                
            |                 
            |               
            |                   
            |___                 
            """,

        """
           _________
            |/   |      
            |              
            |                
            |                 
            |               
            |                   
            |___                 
            H""",

        """
           _________       
            |/   |              
            |   (_)
            |                         
            |                       
            |                         
            |                          
            |___                       
            HA""",

        """
           ________               
            |/   |                   
            |   (_)                  
            |    |                     
            |    |                    
            |                           
            |                            
            |___                    
            HAN""",


        """
           _________             
            |/   |               
            |   (_)                   
            |   /|                     
            |    |                    
            |                        
            |                          
            |___                          
            HANG""",


        """
           _________              
            |/   |                     
            |   (_)                     
            |   /|\                    
            |    |                       
            |                             
            |                            
            |___                          
            HANGM""",



        """
           ________                   
            |/   |                         
            |   (_)                      
            |   /|\                             
            |    |                          
            |   /                            
            |                                  
            |___                              
            HANGMA""",


        """
           ________
            |/   |     
            |   (_)    
            |   /|\           
            |    |        
            |   / \        
            |               
            |___           
            HANGMAN""")
    def save_data(self):
        dataIO.save_json(self.file_path, self.the_data)

    @commands.command(aliases=['h'], pass_context=True)
    async def hangman(self, ctx, guess : str=None):
        """Play a game of hangman against the bot!"""
        if guess is None:
            if self.the_data["running"] == True:
                await self.bot.say("Game of hangman is already running!\nEnter your guess!")
                await self._printgame()
                """await self.bot.send_cmd_help(ctx)"""
            else:
                await self.bot.say("Starting a game of hangman!")
                self._startgame()
                await self._printgame()
        else:
            self._guessletter(guess)
        """
        #self.the_data["WOAH"]["knarly"] = "Biiiiiitch"
        if "Yeah dude" not in self.the_data:
            self.the_data["Yeah dude"]={}
        self.the_data["Yeah dude"]["knarly"]= {"ur lyin" : True,
                                               "kick-ass" : { "no way!!!" : "Biiiiiitch" },
                                               "created_at" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                               }
        
        #self.the_data["Yeah dude"]["knarly"] = "ur lyin"
        #self.the_data["Yeah dude"]["knarly"]["kick-ass"]["no way!!!"] = "Biiiiiitch"
        self.save_data()
        """
        
    def _startgame(self):
        self.the_data["running"] = True
        self.save_data()
        
    def _stopgame(self):
        self.the_data["running"] = False
        self.save_data()
        
    def _getphrase(self):
        '''Get a new phrase for the game'''
        
    def _guessletter(self, guess : str = None):
        '''Checks the guess on a letter'''
        self.the_data["hangman"] += 1
        self.save_data()
    
    async def _printgame(self):
        '''Print the current state of game'''
        await self.bot.say(self.hanglist[self.the_data["hangman"]])
    
def check_folders():
    if not os.path.exists("data/Fox-Cogs"):
        print("Creating data/Fox-Cogs folder...")
        os.makedirs("data/Fox-Cogs")

    if not os.path.exists("data/Fox-Cogs/hangman"):
        print("Creating data/Fox-Cogs/hangman folder...")
        os.makedirs("data/Fox-Cogs/hangman")

        
def check_files():
    if not dataIO.is_valid_json("data/Fox-Cogs/hangman/hangman.json"):
        dataIO.save_json("data/Fox-Cogs/hangman/hangman.json" ,{"running" : False, "hangman" : 0 })

        
def setup(bot):
    check_folders()
    check_files()
    if soupAvailable:
        bot.add_cog(hangman(bot))
    else:
        raise RuntimeError("You need to run `pip3 install beautifulsoup4`")