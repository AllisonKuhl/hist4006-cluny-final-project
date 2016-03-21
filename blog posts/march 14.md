It's been a while since I've written here. 
Part of that was because for a long time I didn't accomplish anything. There was really nothing to report. It was hard to get started because I was nervous: there was just so much that I needed to do, how could I possibly do it? 
Now that I've finally started, I still face some of the same problems. In a way, it's easier to work now that I've started, but sometimes it's difficult, because I have this huge mess of code that I have to sort through. 
In any case though, for better and worse, I've made progress over the last few months. And I need to write down the things I've been doing in order to be transparent about my work. 
I was thinking about that the last few weeks. I've told my classmates to play my game and report back bugs to me, but that has limited effectiveness. They can play the game, sure, and I can even tell them to look at the code, but I think most of the algorithms and stuff fly over their head. I mean, even I get confused by it sometimes and I'm the one who wrote it. So it is best to try and write down what I've done and what I've intended for each thing. 

I started with a rough schedule of a monks life, taken from here: 

This led me to a day that looks something like this: 

DAY_ACTIVITIES = [getDressed, nocturnes, freeTime, matins, sleep, prime, freeTime, terce, chapterMeeting, freeTime, sext, nones, dinner, sleep, freeTime, vespers, compline, sleep]

To be honest, I don't know if this is the BEST possible schedule. I feel like maybe there's too much free time? And I'd like to change the times for eating based on information my colleaugue has provided for me. This upcoming week I'd like to reconsider everything and hopefully update it. 

However, it was helpful to get a rough schedule up early because then I could get to work filling it in. I have modelled each activity as an object. Each one inherits from the Activity class, with an enter_input function, a do_action function and a random_event function. This way, I can just loop through the schedule and it more or less goes on its own. Each activity generally has its own actions, although some, like the free time activity, has special inputs as well. 

To be honest, I'm still a beginner at object oriented programing, so sometimes I worry if I'm doing it all correctly. But I mean... the code more or less works, so at this point, that's good enough for me. 

Right now the input is very rudimentary. You have to type in a specific prompt or else it doesn't work. I did add in some extra possibilities, but it's hard to account for everything. I wonder how those old rpg games managed to make such sophisticated input things? I can't quite figure it out. One thing which I'd like to do is that if you say "go to matins" when it isn't matins, you end up missing the thing which you were supposed to do. So right now I have it so that if you say "go to" + anything that isn't the correct spot, it'll say you went to the wrong spot. But that means if you say "go to" at any point in your prompt, it'll activate that. Which can sometimes look weird. So I'll have to try and find a way to fix that.

Outside for input, the major variables in this game is of course, sin and penance. There are a lot of things which can add your sin. That's pretty easy. But I think the penance and sin need a major overhaul to work more fluidly. Right now the amount of sin added is really haphazard. I need to keep better track of it; maybe store it in a dictionary even? Confessing sins right now is not ideal either, so i'll need to rethink things. 
