How to Play

Click on the monkSimulator.py file and run it somehow. 

The Code – What does it mean? 

Since my project is perhaps a bit dense for a non-programmer to understand, I thought I would lay out the basic functions of my code in order to be more transparent about what I am doing. 
There are several files that contribute to the code. The main one – the one which actually ultimately runs the game, is monkSimulator.py. 

So what’s in this file? It controls what you do in a day. Usually, you just repeat a certain amount of activities. This file also explicitly states the order of the activities – which could be fairly easily changed if anyone wanted to. The functions of each activity are not actually stated in this file, but rather in the Activity class, which is elsewhere. I will talk more about this later. 

The main function begins by asking your name and storing it for later use. Then we begin the day loop. Besides the ordinary day, it also accounts for sick days and days when you are on a journey and will do different things depending on whether you are sick or are on a journey. Once you’ve finished all the activities for the day, it calls the “Day end” function belonging to the Time class which increases the day. This continues for as long as you are alive. 

An ordinary day, as I said, has a specified amount of activities. Although I had hoped to change the schedule slightly depending on the season, I have yet to implement that. 

Each activity has three main methods. There is the “go_to” method. This is when the player is prompted to begin the activity. Then there is the “random_event” method, where a random event may or may not occur. The random events themselves are actually defined in the random event file. And finally there is the “do_action” method, which does the actual method. Although the go_to method is pretty much the same for each activity, the do_action method is unique for each one. 

In each activity, however, the player class is active. I feel like making it a class was a little bit silly since I only need one instance of it, however I thought this was the best way to group all the necessary variables together. In the game, we play as a monk. All the information about this monk is stored in the Player class, for example, your name, your age, your health... etc.  Doing actions in the game variously increases or decreases these variables. 

The most important variables, I suppose, is your “sin” index because this will determine whether you win or lose. (Come to think of it... I should probably add in winning and losing, because I haven’t yet). 

How it operates is this: when you sin, it keeps track of the bad action that you did. Each action has a certain sin value, and your sin is increased by this value. Later, you have to confess this sin, and your sin is decreased by that value, and your penance increases by the same value. Is this the best way to do it? I’m not sure. I think it might need more testing. 

In order to do penance, you need to do good things. Right now, I have it that your penance increases if you do the psalms without mistakes, if you stay up at night doing vigil, if you don’t eat at dinner, if you work during free time, and if you wear hair cloth in the morning. Should I add more? Perhaps somewhat redundantly, there is also a ‘holiness’ variable that also increases when you do these things. I added this because you could do lots of good actions, but it wouldn’t be counted for anything since you didn’t have any penance. I thought this way you would be rewarded for good things even if you didn’t sin and therefore get penance. Holiness will probably also count toward your ultimate reward once I get around to implanting winning and losing scenarios. 

However, for many of the penance actions, you also lose health. For example, by staying up late, you lose both health and sleep. If you don’t get enough sleep, you are more likely to fall asleep during the psalms or sleep in the next time you go to sleep. If your health is low (actually if it’s high, which is why I ended up naming it “sickliness”, it’s just easier to deal with increasing numbers) then you are more likely to get sick. Getting sick is a random event – I believe right now the chances are how sick you are times two. For example, if you have 0 sickliness, you have no chances. If you have 2 sickliness, you have a 4% chance.  If you have 5, you have a 10% chance. And so on. When you get sick, you spend the rest of the day in the infirmary. It’s kind of boring in the infirmary. I wasn’t sure what to make you do. I wonder if this can be improved? 

These are the main variables that matter right now. Other variables are dependent on random events, such as your romance level, which, depending on your level, gives you different results during the romance events. 

Another variable I was thinking about adding was popularity, but other than declaring it I haven’t done anything with it. I was thinking that some events, like talking to monks, even though it increases your sin, could actually also increase your popularity and give you some fun results because of that. But I haven’t expanded on that idea at all. 

So that’s the player class. Other files include the ghost.py file, which is just a random event that occurs only when you’re sleeping where a ghost appears and asks you to pray for him. If you go to a private mass and pray for the name of the ghost, he’ll thank you the next time you meet him. Come to think of it, I should have it that he definitely appears the next time you sleep. I’ll do that tomorrow. Another file is the psalms.py which basically gets the psalms readings you need. Right now, you only read the first few verses of the psalms, but that can be easily changed. 

There is also the Chronology class, which basically controls the years and seasons and days. Although it works (I think), seasons and days don’t really do anything special. I find it hard to strike a good balance for a year so that it’s not too long but also holds enough things. Right now, a year is eight days, and the seasons don’t do anything. What should they do? That is perhaps something I should think about. For example, we should certainly have a feast day on Easter and Christmas. And perhaps others? We shall see. 

I’m sorry this explanation has been a bit ad hoc. Please let me know if there are any questions or if I didn’t explain things sufficiently. 
