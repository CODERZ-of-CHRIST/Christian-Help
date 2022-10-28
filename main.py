print("© Copyright 2022 Ifeanyi Onuama. All rights reserved")
print("Welcome to Christian Help by Ifeanyi Onuama")
import webbrowser
import random
from pygame import mixer

#Instantiate mixer
mixer.init()

#Load audio file
mixer.music.load('intro.mp3')


#Set preferred volume
mixer.music.set_volume(0.2)

#Play the music
mixer.music.play()

def main():
    def about():
        print("This application was created by me, Ifeanyi Onuama, I got inspiration from St. Carlo Acutis, I love him and I aim to be like him by the Grace of God:\nHe got all the mysteries of the Eucharist and put the all together on one website, I hope to be like him.")
        
    def eucharist():
        import webbrowser
        webbrowser.open("http://www.miracolieucaristici.org/en/Liste/list.html")
    def exit():
        exit()
        
        
        
    def bible():
        bible = input("Choose Bible:\nJames, RSV, Good News: ")
        if bible == 'james':
            webbrowser.open("https://www.kingjamesbibleonline.org/")
        if bible == 'rsv':
            webbrowser.open("https://www.biblestudytools.com/rsv/")
        if bible == 'good news':
            webbrowser.open("https://www.biblestudytools.com/gnt/")
            
    def meditation():
        meditation = (
            "Sometimes the hardest part of the day is deciding to get out of bed. From the mundane — What am I going to have for breakfast? — to the major — Is this really where I want to be in my career? — every day is filled with one stressful decision after another. Start the day by choosing to lean on God’s wisdom for all the difficult questions you will face.",
            "As you start your day, you may be wondering how you’re going to get through it. The morning news show on TV lists yet another threat to your safety. And there’s a chance you might run into that one person you’ve been avoiding. Or maybe you just have an oppressive feeling of anxiety with no discernable cause but very noticeable effects. Taking some time to stop and consider what God has to say about anxiety can help bring you back to a place of peace.",
            "Just as you finally get moving to tackle the day, the slow-downs start. First, waiting in line at the café for a cup of coffee. Then traffic once again makes your commute an eternity. Instead of letting your impatience and anger take control, use the time to reflect and see if God is using the wait as an opportunity to speak to you and help remove your stress.",
            "Another day, another to-do list. Whether you’re a top account executive or a stay-at-home parent, a best-selling artist or a mom-and-pop store owner, you have an important role to play in the world. It’s easy to lose sight of this unique purpose that you have been given in the thick of the emails and phone calls and meetings. This meditation will help you get back on track with your calling to keep you motivated as you work.",
            "Bill from the office next door lost the quarterly report. You get the fourth call this week from your child’s school asking you to meet your child at the principal’s office. Your spouse’s boss once again passes them over for a promotion. Some people seem to enjoy making our life challenging, yet as Christians, we are called to love them. Talk about needing some peace?! When you find yourself getting angry at them, take a moment to remember that God still loves them and you can too.",
            )
        choice = random.randint(0, 5)
        print(meditation[choice])
        
    if action == 'about':
        about()

    if action == 'eucharist':
        eucharist()
        
    if action == 'bible':
        bible()
        
    if action == 'meditation':
        meditation()

        
while True:
    action =  input("\n|About| |Eucharist| |Songs| |Bible| |Meditation| |Exit|\nType here: ")
    main()
    if action == 'exit':
        exit()
        