# GAWA-GAWA NI ALEXIS..
from nltk.chat.util import Chat, reflections

pairs = [
    #   INTRODUCTIONS FROM FRIEND-BOT
    [r'Sino ka?', ['Ako si Friend-Bot na handa kang gabayan!']],

    #   GREETINGS FROM USER
    [r'Hello', ['Oh? Andito ka nanaman? sinaktan ka ba niya?', 'Anong problema mo?', 'Oi?']],
    [r'Hi', ['Oh? Andito ka nanaman? sinaktan ka ba niya?', 'Anong problema mo?', 'Oi?']],
    [r'Kumusta', ['Oh? Andito ka nanaman? sinaktan ka ba niya?', 'Anong problema mo?', 'Oi?']],

    #   INTRODUCTIONS FROM USER
    [r'Ako si (.*)', ['Ahh! Ikaw si %1, yung kaibigan ni Alexis noh?', 'HACKER KA BA?? bakit nandito ka?']],

    #   ANSWER FROM SINAKTAN
    [r'sinaktan', ['Hala ka! anong ginawa nya sa iyo?', 'nanaman? kawawa ka naman!']],
    #   ANSWER FROM ANONG GINAWA OPT-1
    [r'pinagpalit', ['Pinagpalit ka?? Kanino?', 'Hayaan mo na siya, tsaka focus ka sa studies mo']],
    #   ANSWER FROM ANONG GINAWA OPT-2
    [r'iniwan', ['Iniwan ka?? Ansama naman nya!', 'Hayaan mo na siya, tsaka focus ka sa studies mo']],
    [r':<', ['Malungkot ka nanaman.. wag kang umiyak please..', 'Iiyak din ako sige ka..']],

    #   ANSWER FROM 1ST AND 2ND IN "AKO SI"
    [r'oo', ['Ahh ok?', 'Ahh ok..', 'Oo na nga!']],
    [r'hindi', ['Oh? bakit naparito ka?', 'Itulog mo nalang yan!']],
    [r'idk', ['di ko rin alam..', 'ewan ko sayo ang gulo mo po..']],
    #   ANSWER FROM 2ND AND FROM "OO" 3RD
    [r'sorry', ['oum', 'opo']],
    #   ANSWER FROM SORRY 2ND
    [r'ako nga si (.*)', ['Ay! Oo ikaw si %1', 'Okay %1, ano plano natin ngayon?']],

    #   CLOSING REMARKS
    [r'Goodbye', ['Goodbye rin po!', 'Sige, sige mamaya ulit!']],
    # Add more patterns here
]

chatbox = Chat(pairs, reflections)

# Start Chatting
print("Anonymous: Hello! Kausapin kita kasi malungkot ka? :>")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print('Bot: Thank you chatting with Friend-Bot!')
        break
    response = chatbox.respond(user_input)
    print("Bot: ", response)
