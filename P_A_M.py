###############################################################################
#SpartaHack V:
#Project Personal Assistan Maker
#class Assistant()
#   age_type function
#   emotional_support function
#       support sounds different depending on age
#   schedule function
#end 7-day trial
###############################################################################
import random

day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"\
             , "Sunday"]
num_days = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5: "Friday",\
            6:"Saturday", 7:"Sunday"}
day_num = {"Monday":1, "Tuesday":2, "Wednesday":3, "Thursday":4, "Friday":5,\
           "Saturday":6, "Sunday":7}
class  Assistant(object):
    def  __init__(self,name = "Pam",gender = "female", age = "18"):
        self.name = name
        self.gender = gender
        self.age = age

    def __str__(self):
        return self.name
    def age_type(self):
        age_num = int(self.age)
        if age_num <= 10:
            return 'child'
        elif age_num >= 60:
            return 'senior'
        elif age_num >=11 and age_num <= 18:
            return 'adolescent'
        elif age_num >= 19 and age_num <= 26:
            return 'new'
        else:
            return 'adult'
        
    def emotional_support(self, mood, age_type):
##dictionary
        selection = random.randint(0,2)
        
        
        mood_dict = {"happy":["Sanity and happiness are an impossible combination.",\
                              "No medicine cures what happiness cannot.", \
                              "Happiness is only real when shared " ],"sad": \
    ["Sadness flies away on the wings of time.", "Tears are words that need to be written."\
     , "Any fool can be happy. It takes a man with real heart to make beauty out of the stuff that makes us weep."],\
     "content":["nobody got anywhere in this world by just being content",\
                "Only I can change my life for me. No one else can do that for me",\
                "With the new day comes new strength and new thoughts"]}
        if age_type == 'new':
            mood_dict = {"happy":["Be happy for this moment. This moment is your life.","The secret to happiness is freedom. And the secre to freedom is courage.","Family and friendships are two of the greatest facilitators of happiness."],"sad":["Friends show thier love in time of trouble not in happiness.","The good times of today, are the sad thoughts of tomorrow.","Tears come from the heart and not from the brain."],"content":["Develop a passion for learning. If you do, you will never cease to grow.", "I have no special talent. I am only passionately curious.", "You have to stay in school. You have to. You have to go to college. You have to get your degree. Because that's the one thing people can't take away from you is your education. And it is worth the investment. - Michelle Obama"]}
        if age_type == 'child':
            mood_dict = {"happy":["WOOOO I am always happy too!", "My mom says to always smile :)","A smile a day keeps me happy!"],"sad":["Mommy says Santa will be mad if you are sad.", "Dad doesn't like to see people sad, he always says you should be mad rather than sad atleast.", "Elmo loves you too!"],"content":["Yeah its boring.","At least we aren't grounded.", "Momma says to always be happy."]}
        if age_type == 'senior':
            mood_dict = {"happy":["Cherish all your happy moments; they make a fine cushion for old age", "If you ever wanted to be a kid again wait til your old. You don't have to do anything anymore!","I will never giv in to old age until I become old. And I'm not old yet!"],"sad":["Old age is the most unexpected of all things that happen to a man.", "Youth is a blunder; Manhood a struggle, Old Age a regret","Old age is not a mteer for sorrow. It is matter for thanks if we have left our work done behind us."],"content":["Be eccentric now. Don't wait for old age to wear purple.","Old age has its pleasures, which, though different, are notless than the pleasures of youth.", "Naps are great no matter old or young!"]}
        if age_type == 'adolescent':
            mood_dict = {"happy":["Keep tue to the dream of your youth.", "Snow days are a sign god is real.", "That glow up tho!"],"sad":["Telling a teenager the facts of life is like giving a fish a bath.", "Adolescence is just one big walking pimple.", "Homework sucks, I just want to sleep."],"content":["We never really group up, we only learn how to act in public.", "It takes courage to grow up and become who you really are.", "HALF DAY!"]}
          
        if mood.lower() ==  'happy':
            return mood_dict["happy"][selection]
        elif mood.lower() == 'sad':
            return mood_dict['sad'][selection]
        else :
            return mood_dict['content'][selection]

    def schedule(self):
        return "LOL"
#        def morning_meme(self):
#            return image

def main():
    print("Welcome to your one week trial to the personal assistant maker. Where we will create both a secretary and friend.")

    your_assistant = Assistant()
    name = input("What is your name: ").title()
    print("\nHello "+ name)

##Creating Assistant
    print("Now answer the next few questions to start creating your personal assistant")
    
    assi_gender = input("Select a prefered gender. Female or Male?: ").lower()
    while assi_gender not in ['female','male']:
        assi_gender = input("We are working to expand to a more progressive line up.\n However we have just two options at the moment.\n Female or Male?: ")
        if assi_gender == "male":
            print("Your assistant is male.")
        else:
            print("Your assistant is female.")
            
    assi_name = input("What would you like to name your assistant?:" ).title()
    
    assi_age = input("You can also choose the age for your assistant, there may be some unexpected responses if you choose an age closer to a child or a senior citizen. Input format example: 26 \nPlease enter an age: ")
    while assi_age.isdigit() != True or int(assi_age) <= 0 or int(assi_age) > 122:
        if assi_age.isdigit() != True:
            print("Error, you did not enter a valid age.")
            assi_age = input("Please enter a numeric age. ")
        elif int(assi_age) <= 0:
            print("Sorry your desired assistant has not been bored yet.")
            assi_age = input("Please enter an age that would be at least alive. ")
        elif int(assi_age) > 122:
            print( "There has been no one that has lived longer than your inputted age. ")
            assi_age = input("Please enter a valid age. ")
        else:
            assi_age = input("Please enter a valid age. ")

    your_assistant = Assistant(assi_name, assi_gender, assi_age)

    start = input("Do you want to start your trial? (Y/N): ")

    if start.upper() == "N" :
        print("Too late its free!! Lets start!")
        
    age_type = your_assistant.age_type() #Tracks the age_type
    
    print("Oh, by the way, your assistant is under the age-type " + age_type + ". We do not guarantee the actions or speach of your assistan depending on its age.\nGood Luck!")
    
    event_list = {}

    for day in range(1,8):
        
        rediculous = random.randint(0,100)
        
        #morning_meme = your_assistant.meme()
        #print(morning_meme)
        print("\nToday is " + num_days[day])
        
        #Rediculous factors
        if age_type == "child":
            if rediculous >= 50:
                print(your_assistant.name + " has soiled thier bed this morning and can no longer be here today.")
                print(your_assistant.name + ": 'Sorry " + name + " I'll do my best tomorrow though!'")
                continue

        if age_type == "new":
            if rediculous <= 10:
                print(your_assistant.name + " has called in sick.")
                print(your_assistant.name + ": 'Sorry " + name + " I should be better tomorrow, but I won't be able to be there for you today. See you tomorrow!'")
                continue
            elif rediculous >=90:    
                print(your_assistant.name + ": 'Hey, " + name + ", I just got super liked on tinder so like, I going out today. Hope you can understand.")
                continue
            
        if age_type == "senior":
            if rediculous <= 50:
                print(your_assistant.name + ": 'Help! I've fallen and I can't get up!'")
                print(name + "Runs over and helps + "+ your_assistant.name + "." + your_assistant.name + " is too traumatized to work today.")
                continue
            if rediculous >= 90:
                print(your_assistant.name + " was run over by a reindeer!")
                print(your_assistant.name + " goes to the hospital and you lose a day of the trial!")
                continue
                
        if age_type == "adolescent":
            if rediculous <= 20:
                print(your_assistant.name + " didn't show up. However you call his mom and " +your_assistant.name + " won't get paid for the rest of the demo.")
                continue
            if rediculous >=40 and rediculous <= 50:
                print(your_assistant.name + "'s Mom called and she said that '" + your_assistant.name + " jumped out the window and sprained his ankle.")
                print(your_assistant.name + " will be back tomorrow!")
                continue
            
        mood = input(your_assistant.name +": 'Lets start with a quote to match your mood!'\n'How are you feeling today?' (happy, sad or content) : ")
        
        print(your_assistant.emotional_support(mood, age_type)) #Prints a random quote of the day
        
        if day in event_list:
            print("\n" + your_assistant.name +": 'You have these events for today:'")
            for i in event_list[day]:
                print("'" + i + "'")
            
        #Daily scheduling    
        want_sched = input("\n" + your_assistant.name +": 'Would you like to schedule something for the week?' (Y/N): ").upper()
        while want_sched != "Y" and want_sched != "N":
            if day == 7:
                print(your_assistant.name +": 'Today is the last day of the trial. You are unable to schedule anything.'")
                want_sched = "N"
                continue
            print("Please enter a valid input")
            want_sched = input(your_assistant.name +": 'Would you like to schedule something for the week?' (Y/N): ").upper()
        #Continue if want to schedule    
        
        while want_sched == "Y":
            week_day = input(your_assistant.name +": 'Which day would you like to schedule something.' (Monday, etc.): ").title()
            while week_day not in day_names:
                week_day = input("Please enter a valid weekday or weekend").title()
            #If week day is not valid
            while day_num[week_day]<= day:
                #Response depends on day
                if day_num[week_day] == day:
                    week_day = input(your_assistant.name +": 'Unfortunately today is already "+ week_day + ".'\n'Please choose another day': ")
                elif day_num[week_day] == day:
                    week_day = input(your_assistant.name +": 'Sorry, your trial does not last till "+ week_day + "'\n'Please choose another day': ")
                while week_day not in day_names:
                    week_day = input("Please enter a valid weekday or weekend").title()
                
            event = input(your_assistant.name +": 'What event would you like to be reminded of?'")
            print(your_assistant.name +": 'I will remind " + name + " on " + week_day + " of the event " + event + "'." )
            
            if day_num[week_day] not in event_list:
                event_list[day_num[week_day]] = []
            event_list[day_num[week_day]].append(event)
            
            want_sched = input(your_assistant.name +": 'Would you like to schedule anything else?' (Y/N) ").title()
            while want_sched != "Y" and want_sched != "N":
                print("Please enter a valid input")
                want_sched = input(your_assistant.name +": 'Would you like to schedule something for the week?' (Y/N): ").upper()
        #End of Scheduling
    print("Thus ends your week long trial.")
    print(your_assistant.name +": 'I hope you have had a great experience!'")        
if __name__ == "__main__":
    main()
#