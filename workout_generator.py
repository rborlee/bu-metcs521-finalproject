"""
Rachel Lee
Class: CS 521 - Fall 2
Date: 12/07/2021
Final Project
Description of Problem (1-2 sentence summary in your own words):
A Program to generate a workout depending on your mood/energy level,
body part focus, length of time, and cardio level.
"""

import functions as f
import BodyWorkout


if __name__ == '__main__':
    '''Main Program to Run Workout Generator'''
    # menu prompt to get user inputs
    usr_values = f.prompt()

    # Get workouts for all body part(s) listed from user prompt
    workout_files = {}
    body = usr_values['focus']
    if isinstance(body, list):
        for part in body:
            read = f.read_file(f'focus/{part}.txt')
            workout_files[part] = read
    else:
        read = f.read_file(f'focus/{body}.txt')
        workout_files[body] = read

    # Check if user wants Cardio and read in Cardio values if True
    if usr_values['cardio'] == True:
        cardio = f.read_file(f'focus/cardio.txt')
    else:
        cardio = None
    
    # Build workout exercises according to user's input/interest
    val = workout_files.values()
    body_lst = [list(v) for v in val]

    # Call SingleBody Method from BodyWorkout Class if type = 'single'
    if usr_values['type'] == 'single':
        workout_type = BodyWorkout.SingleBody(\
            focus=body_lst[0],
            energy_lvl=usr_values['energy'],
            time=usr_values['time'],
            cardio=cardio
        )
        # Generate Workout Plan and Set Number
        plan, set_num = workout_type.generate_workout()
        workout_str = '{} set(s) of:\n'.format(set_num)
        for k,v in plan.items():
            tmp_str = '{} -- {}x\n'.format(k,v)
            workout_str += tmp_str
    # Call FullBody Method from BodyWorkout Class if type = 'full'
    else:
        
        workout_type = BodyWorkout.FullBody(\
            focus=body_lst[0],
            energy_lvl=usr_values['energy'],
            time=usr_values['time'],
            cardio=cardio,
            extra=body_lst[1::]
        )
        # Generate Workout Plan and Set Number
        plan = workout_type.full_body_workout()
        workout_str = ''
        for exercise in plan:
            set_num = exercise[1]
            new_str = '{} set(s) of:\n'.format(set_num)
            for k,v in exercise[0].items():
                tmp_str = '{} -- {}x\n'.format(k,v)
                new_str += tmp_str
            
            workout_str += new_str

    if cardio != None:
        cardio_plan = workout_type.generate_cardio()
        cardio_str = '{}min of {}'.format(cardio_plan[0], cardio_plan[1][0])

        workout_plan = f'{workout_str}\n{cardio_str}'
        print('\n\n')
        print('-'*5, 'WOKROUT PLAN', '-'*5)
        print(workout_plan)
    else:
        workout_plan = f'{workout_str}'
        print('\n\n')
        print('-'*5, 'WOKROUT PLAN', '-'*5)
        print(workout_plan)