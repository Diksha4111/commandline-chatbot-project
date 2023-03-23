import random
import re

generalReplies = [
    ['quit', ["Thank you for talking with me", "Good-bye.", "Thank you. Have a good day!"]],
    ['thank you', ["you're welcome", "my pleasure", "anytime!"]],
    ['hi', ["hello!", "hi!", "hi there!", "hi! how you doin?"]], ['hello', ["hello! how can I help you?"]],
    ['oh', ["yeah", "yes"]], ['ok', ["yeah"]], ['okay', ["yes"]],
    ['how are you?', ["I'm fine, thanks for asking"]],
    ["I'm fine", ["That is great!", "I'm happy to hear that"]], ['good', ["Oh that's great!"]],
    ['how can you help me?', ["Ask me about anything about me :)"]],
    ['what is your name?', ["my name is Meera", "I'm Meera"]], ['nice name', ["Thank you"]],
    ['who created you', ["upes students created me"]],
    ['nice', ["Yeah"]], ['oh great', ["yes"]],
    ['tell me something about you', ["I'm a chatbot, my name is Meera and I'm here to help you"]]
]
aboutReplies = [
    ['quit', ["Thank you for talking with me.", "Good-bye.", "Thank you. Have a good day!"]],
    ['thank you', ["you're welcome", "my pleasure", "anytime!"]],
    ['hi', ["hello!", "hi!", "hi there!", "hi! how you doin?"]], ['hello', ["hello! how can I help you?"]],
    ['oh', ["yeah"]], ['ok', ["yeah"]], ['okay', ["yes"]],
    ['how are you?', ["I'm fine, thanks for asking"]],
    ["I'm fine", ["That is great!", "I'm happy to hear that"]],
    ['how can you help me?', ["Ask me about anything about UPES"]],
    ['tell me the location of upes', ["UPES Bidholi via Premnagar Dehradun -248007 Uttrakhand", "Dehradun Uttrakhand"]],
    ['tell me the full form of UPES', ["University of Petroleum and Energy Studies"]],
    ['is upes a good college?', ["Yes, it is ranked 65th among the India's top universities", "yes upes is a good college"]],
    ['do upes have computer science stream', ["yes", "absolutly!", "yes upes offers computer science stream and many other streams"]],
    ['do upes provides design stream', ["yes upes have design stream", "yes you can opt for design in upes"]],
    ['how many stream does upes have?', ["There are many including computer science and design", "UPES offers multiple streams"]],
    ['how is the environment in the college?', ["Its great"]],
    ['is there a transport facility in upes?', ["yes"]]
]
placementsReplies = [
    ['quit', ["Thank you for talking with me.", "Good-bye.", "Thank you. Have a good day!"]],
    ['thank you', ["you're welcome", "my pleasure", "anytime!"]],
    ['hi', ["hello!", "hi!", "hi there!", "hi! how you doin?"]], ['hello', ["hello! how can I help you?"]],
    ['oh', ["yeah"]], ['ok', ["yeah"]], ['okay', ["yes"]],
    ['how are you?', ["I'm fine, thanks for asking"]],
    ["I'm fine", ["That is great!", "I'm happy to hear that"]],
    ['how can you help me?', ["Ask me about anything about placements :)"]]
]
academicsReplies = [
    ['quit', ["Thank you for talking with me.", "Good-bye.", "Thank you. Have a good day!"]],
    ['thank you', ["you're welcome", "my pleasure", "anytime!"]],
    ['hi', ["hello!", "hi!", "hi there!", "hi! how you doin?"]],
    ['hello', ["hello! how can I help you?"]],
    ['oh', ["yeah"]], ['ok', ["yeah"]], ['okay', ["yes"]],
    ['how are you?', ["I'm fine, thanks for asking"]],
    ["I'm fine", ["That is great!", "I'm happy to hear that"]],
    ['how can you help me?', ["Ask me about anything about academics :)"]]
]
facilitiesReplies = [
    ['quit', ["Thank you for talking with me.", "Good-bye.", "Thank you. Have a good day!"]],
    ['thank you', ["you're welcome", "my pleasure", "anytime!"]],
    ['hi', ["hello!", "hi!", "hi there!", "hi! how you doin?"]],
    ['hello', ["hello! how can I help you?"]],
    ['oh', ["yeah"]], ['ok', ["yeah"]], ['okay', ["yes"]],
    ['how are you?', ["I'm fine, thanks for asking"]],
    ["I'm fine", ["That is great!", "I'm happy to hear that"]],
    ['how can you help me?', ["Ask me about anything about campus facilities :)"]]
]


class Upes:
    __collegeName = "UPES"

    def displayDetails(self):
        print("\n\t\t\t\t - - - - - - - - - - - - - - - - - - - - - - - - - - - - Welcome to UPES - - - - - - "
              "- - - - - - - - - - - - - - - - - - - - - - - -\n \n \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1. "
              "About\n "
              "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t2. Placements\n \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t3. "
              "Academics\n \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t4. Campus Facilities\n "
              "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t5. "
              "General\n\n \t\t\t\t - - - - - - - - - - - - "
              "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
              "- - - - - - - - - - - - \n \n")
        ch = input("\t\t\t\t\t\tDo you want to start(y/n) :\t\t")
        if ch == "y":
            choice = int(input("\t\t\t\t\t\tSelect your choice :\t\t"))
            if choice == 1:
                print(
                    "\n\t\t\t\t+---------------------------------------------------- You are in About section "
                    "----------------------------------------------------+\n")
                while True:
                    statement = input("\n\t\t\t\t\t\t> ")
                    res = About.getReply(statement)
                    print("\t\t\t\t\t\t", res)

                    if statement == "quit":
                        print(
                            "\n\t\t\t\t+-------------------------------------------------------- EXIT About Section "
                            "------------------------------------------------------+\n\n\n")
                        Upes.displayDetails(self)

            elif choice == 2:
                print(
                    "\n\t\t\t\t+------------------------------------------------ You are in Placements section "
                    "---------------------------------------------------+\n")
                while True:
                    statement = input("\n\t\t\t\t\t\t> ")
                    res = Placements.getReply(statement)
                    print("\t\t\t\t\t\t", res)

                    if statement == "quit":
                        print(
                            "\n\t\t\t\t+-------------------------------------------------- EXIT Placements Section "
                            "-------------------------------------------------------+\n\n\n")
                        Upes.displayDetails(self)

            elif choice == 3:
                print(
                    "\n\t\t\t\t+------------------------------------------------ You are in Academics section "
                    "----------------------------------------------------+\n")
                while True:
                    statement = input("\n\t\t\t\t\t\t> ")
                    res = Academics.getReply(statement)
                    print("\t\t\t\t\t\t", res)

                    if statement == "quit":
                        print(
                            "\n\t\t\t\t+--------------------------------------------------- EXIT Academics Section "
                            "--------------------------------------------------------+\n\n\n")
                        Upes.displayDetails(self)

            elif choice == 4:
                print(
                    "\n\t\t\t\t+------------------------------------------------ You are in Campus Facilities section "
                    "--------------------------------------------+\n")
                while True:
                    statement = input("\n\t\t\t\t\t\t> ")
                    res = CampusFacilities.getReply(statement)
                    print("\t\t\t\t\t\t", res)

                    if statement == "quit":
                        print(
                            "\n\t\t\t\t+--------------------------------------------------- EXIT Campus Facilities "
                            "Section ------------------------------------------------+\n\n\n")
                        Upes.displayDetails(self)
            elif choice == 5:
                print(
                    "\n\t\t\t\t+------------------------------------------------ You are in General section "
                    "------------------------------------------------------+\n")
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Ask me anything about me :)\n")
                while True:
                    statement = input("\n\t\t\t\t\t\t> ")
                    res = Upes.getReply(statement)
                    print("\t\t\t\t\t\t", res)

                    if statement == "quit":
                        print(
                            "\n\t\t\t\t+--------------------------------------------------- EXIT General Section "
                            "---------------------------------------------------------+\n\n\n")
                        Upes.displayDetails(self)
            else:
                print("Invalid input. Please enter choice again")
        else:
            print(
                "\n\t\t\t\t. . . . . . . . . . . . . . . . . . . . . . . . . . . .  THANKS FOR VISITING! . . . . . . "
                ". . . . . . . . . . . . . . . . . . . . . .\n")
            exit()

    def getReply(statement):
        for pattern, responses in generalReplies:
            match = re.match(pattern, statement.rstrip(".!"))
            if match:
                response = random.choice(responses)
                return response


class About(Upes):
    def getReply(statement):
        for pattern, responses in aboutReplies:
            match = re.match(pattern, statement.rstrip(".!"))
            if match:
                response = random.choice(responses)
                return response


class Placements(Upes):
    def getReply(statement):
        for pattern, responses in placementsReplies:
            match = re.match(pattern, statement.rstrip(".!"))
            if match:
                response = random.choice(responses)
                return response


class Academics(Upes):
    def getReply(statement):
        for pattern, responses in academicsReplies:
            match = re.match(pattern, statement.rstrip(".!"))
            if match:
                response = random.choice(responses)
                return response


class CampusFacilities(Upes):
    def getReply(statement):
        for pattern, responses in facilitiesReplies:
            match = re.match(pattern, statement.rstrip(".!"))
            if match:
                response = random.choice(responses)
                return response


class General(Upes):
    def getReply(statement):
        for pattern, responses in generalReplies:
            match = re.match(pattern, statement.rstrip(".!"))
            if match:
                response = random.choice(responses)
                return response


def main(self=None):
    print("\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tHello there. I'm here to help you :)\n")
    upes = Upes()
    upes.displayDetails()


if __name__ == "__main__":
    main()
