# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/26
from _for_ex import pt_title
from survey import AnonymousSurvey

pt_title('language_survey.py'.upper())
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Entry 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
