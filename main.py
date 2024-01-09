#This chatbot has been created in accordance with the specifications provided by Nexus Info
#It has been created taking inspiration from the ELIZA chatbot (1964 - '67) at MIT, created by Joseph Weizenbaum.
#I would like to thank the 'Identity' YouTube channel, whom I referred to for the successful completion of the project.
#The links for their GitHub repos and YouTube channel shall be made available shortly in my GitHub handle.
#Thank you, for considering!

import re
import long_responses as long

#TODO: creating a function that calculates the probability of the matching of the user's message to the
#chatbot's predefined responses.
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = (float(message_certainty) / float(len(recognised_words)))*100

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage)
    else:
        return 0

#TODO2: creating a function to check the user's message against all pre-defined responses, and selects the
#one with the highest preference or probability.
def check_all_messages(message):
    highest_prob_dict = {}
    
    #Creating a helper function defined inside the check_all_messages function.
    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_dict
        highest_prob_dict[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'you', 'gahgawajfa', 'akghaufh'], required_words=['you','love'])#adding random words, to test if the bot can ignore them.
    response("That's so great to hear!", ["i","am","doing", "fine"], required_words = ["fine"])
    #response("I love you too!", ["i","love","you"], required_words=["love", "you"])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_dict, key=highest_prob_dict.get)
    #print(highest_prob_dict)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')
    return long.unknown() if highest_prob_dict[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

print("Bot: Namaskars! How may I help you?")
# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))
    
