"""
Rachel Lee
Class: CS 521 - Fall 2
Date: 12/07/2021
Final Project
Description of Problem (1-2 sentence summary in your own words):
A Program to generate a workout depending on your mood/energy level,
body part focus, length of time, and cardio level.
"""

import random
import string
import sys
import os

def read_file(file_name):
    '''
    Read File: line by line with no duplicates -> set
    '''
    cwd = os.getcwd()
    file_path = os.path.join(cwd, file_name)
    
    # try/except to validate file exists
    try:
        file = open(file_path, 'r')
    except IOError as e:
        sys.exit(f'Error Msg: File "{file_name}" not found; {e}')
        
    contents = file.readlines()
    
    file_set = {line.strip() for line in contents}
    file.close()

    return file_set # return set to ensure no duplicate exercises


def prompt():
    '''Prompt Function for User Input'''

    BODY = ['arm', 'back', 'core', 'glute', 'leg', 'shoulder']

    print('Welcome to the Workout Program Curator!')
    print('.\n'*5)
    print('Let\'s get started. First we need some information...\n')
    print('-'*40)
    valid = False # user input validation check for Energy Lvl
    while not valid:
        print('What is your energy level?')
        energy = input('Enter \'high\', \'normal\', \'low\'): ')
        energy = energy.lower().strip()
        if energy == 'high':
            valid = True
        elif energy == 'normal': 
            valid = True
        elif energy == 'low':
            valid = True
        else:
            print('Error: Input is invalid, please try again.\n')
            valid = False
    
    print('Great! Thanks for the input.\n')

    print('*'*40)
    valid = False # user input validation check for Single or Full Body
    check = False # user input validation for body part focus
    while not valid:
        print('Are you interested in a Single Body or Full Body Focus?')
        usr = input('Enter \'1\' for Single Body , \'2\' for Full Body): ')
        usr = usr.strip()
        if usr == '1':
            type = 'single'
            # check for use by class FullBody
            valid = True
            ## Ask for body focus ##
            while not check:
                print('Okay, what body focus?')
                focus = input(\
                    'Enter one (arm, back, core, glute, leg, shoulder): ')
                focus = focus.strip()
                if focus in BODY:
                    check = True
                else:
                    print('Error: Input is invalid, please try again.\n')
                    check = False      
        elif usr == '2':
            type = 'full'
            valid = True

            ## Ask for body focuses ##
            while not check:
                print('Okay, what body focuses?')
                print('Choose of (arm, back, core, glute, leg, shoulder)',
                    'separated by comma (,).')
                nxt_usr = input('Enter: ').strip()
                focus = ''.join([char for char in nxt_usr \
                    if char not in string.punctuation]
                )
                focus = list(set(focus.split()))
                
                for item in focus:
                    if len(focus) <= 1:
                        print('Error: Inputs are invalid, please try again.\n')
                        check = False
                        break
                    elif item not in BODY:
                        print('Error: Inputs are invalid, please try again.\n')
                        check = False
                        break
                    else:
                        check = True
        else:
            print('Error: Input is invalid, please try again.\n')
            valid = False
    
    print('Great! Thanks for the input.\n')
    
    ## Ask for length of workout time ##
    print('*'*40)
    valid = False # user input validation check for Time
    while not valid:
        print('How long do you want to workout (max 60min)?')
        time = input('Enter any number in minutes (15-60): ')
        time = time.strip()
        if time.isdigit():
            if int(time) >= 15  and  int(time) <= 60:
                valid = True
            else:
                print('Error: Input is not within range.\n')
                valid = False
        else:
            print('Error: Input is not a number.\n')
    
    print('Great! Thanks for the input.\n')
    
    ## Ask for Cardio ##
    print('*'*40)
    valid = False # user input validation check for Cardio
    while not valid:
        print('Do you want to add Cardio?')
        print('*NOTE* It will add extra time to your total workout.')
        val = input('Enter \'yes\' or \'no\': ')
        print('')
        print('-'*40)
        val = val.strip()
        if val == 'yes':
            cardio = True
            valid = True
        elif val == 'no':
            cardio = False
            valid = True
        else:
            print('Error: Input is not valid. Please try again.\n')
            valid = False
        
    input_dict = {}
    input_dict['energy'] = energy
    input_dict['type'] = type
    input_dict['focus'] = focus
    input_dict['time'] = time
    input_dict['cardio'] = cardio

    print_str = f'You have entered:\n\
        \tEnergy Level = {input_dict["energy"]}\n\
        \tFocus Type = {input_dict["type"]}\n\
        \tBody Part Focus = {input_dict["focus"]}\n\
        \tTotal Time = {input_dict["time"]}min\n\
        \tCardio Included = {input_dict["cardio"]}'

    print(print_str) # print inputs for user visualization

    return input_dict # return dict value of all user inputs from prompt