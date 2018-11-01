#! python3
"""
Created on August 20
@author: brmelovi

# randomQuizGenerator.py - Create quizzes with questions and answers in
# random order, along with the answer key.
"""
import random, shelve

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia':
'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


deskDir = r'C:\Users\brmelovi\Desktop\\'

for quizNum in range(35):
    #Create the quiz and answer key files
    quizFile = open(deskDir + '\\files\\capitalquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalquiz_answers%s.txt' % (quizNum + 1), 'w')

    #Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    #Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)


    for questionNum in range(50):

        correctAnwser = capitals[states[questionNum]]
        wrongAnwser = list(capitals.values())
        del wrongAnwser[wrongAnwser.index(correctAnwser)]
        wrongAnwser = random.sample(wrongAnwser, 3)
        anwserOptions = wrongAnwser + [correctAnwser]
        random.shuffle(anwserOptions)

        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], anwserOptions[i]))
        quizFile.write('\n')

        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[anwserOptions.index(correctAnwser)]))
    quizFile.close()
    answerKeyFile.close()
