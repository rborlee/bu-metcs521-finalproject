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
import functions as f

class SingleBody:
    '''
    Body Class
    '''
    def __init__(self, focus, energy_lvl, time, cardio=None):
        ''' Initializer / Instance '''
        self.focus = focus
        self.cardio = cardio
        self.__energy_lvl = energy_lvl
        self.__time = int(time)


    def __generate_rep(self):
        '''Generate Rep Number Method'''
        # set random number according to 'high', 'normal', or 'low' energy lvl
        high = random.randrange(11,16)
        normal = random.randrange(6,11)
        low = random.randrange(1,6)

        if self.__energy_lvl == 'high':
            return high
        elif self.__energy_lvl == 'normal':
            return normal
        elif self.__energy_lvl == 'low':
            return low
        else:
            raise

    def __generate_set(self):
        '''Generate Set Number Method'''
        # set random number according to time entered
        high = random.randrange(5,7)
        medium = random.randrange(3,5)
        low = random.randrange(1,3)

        if self.__time <= 20:
            return low
        elif self.__time > 20 and self.__time <= 40:
            return medium
        elif self.__time > 40:
            return high
        else:
            raise

    def generate_workout(self, body=None):
        '''Generate Workout Plan Method'''
        # choose random sample from body part(s) focus
        ## DeprecationWarning: Sampling from a set deprecated since Python 3.9 \
        ## and will be removed in a subsequent version. \
        ## high = [random.sample(self.focus, 4)]
        if body is None:
            high = [random.sample(list(self.focus), 4)]
            normal = random.sample(list(self.focus), 3)
            low = random.sample(list(self.focus), 2)
        else:
            high = random.sample(body, 4)
            normal = random.sample(body, 3)
            low = random.sample(body, 2)

        # generate workout set number #
        workout_set = self.__generate_set()

        # store as k:v dict for number of reps to workout
        if self.__energy_lvl == 'high':
            plan = {workout:self.__generate_rep() for workout in high}
        elif self.__energy_lvl == 'normal':
            plan = {workout:self.__generate_rep() for workout in normal}
        elif self.__energy_lvl == 'low':
            plan = {workout:self.__generate_rep() for workout in low}
        else:
            raise
        # print(plan, workout_set) # TESTING -- REMOVE
        return plan, workout_set # return complete workout plan with set number
    
    def generate_cardio(self):
        '''Generate Cardio Plan Method'''
        # random choose of exercises from list
        # require converstion self.cardio set -> list due to deprecation warning
        ## DeprecationWarning: Sampling from a set deprecated since Python 3.9 \
        ## and will be removed in a subsequent version. \
        ## low = random.sample(self.cardio, 1)
        high = random.sample(list(self.cardio), 1)
        normal = random.sample(list(self.cardio), 1)
        low = random.sample(list(self.cardio), 1)

        # auto-call and assign cardio plan from random choise if cardio True
        if self.cardio is not None:
            if self.__energy_lvl == 'high':
                plan = (30, high)
            elif self.__energy_lvl == 'normal':
                plan = (20, normal)
            elif self.__energy_lvl == 'low':
                plan = (10, low)
            else:
                raise
        
        return plan
    
    # Magic Methods to Compare length of workout
    def __lt__(self, obj):
        '''Less Than Comparison'''
        return self.__time < obj.__time
    def __gt__(self, obj):
        '''Greater Than Comparison'''
        return self.__time > obj.__time
    def __le__(self, obj):
        '''Less Than or Equal Comparison'''
        return self.__time <= obj.__time
    def __ge__(self, obj):
        '''Greater Than or Equal Comparison'''
        return self.__time >= obj.__time
    def __eq__(self, obj):
        '''Equal Comparison'''
        return self.__time == obj.__time
    def __ne__(self, obj):
        '''Not Equal Comparison'''
        return self.__time != obj.__time
    
    # repr() Method for return print representation
    def __repr__(self):
        '''Repr Method'''
        has_cardio = False if self.cardio is None else True
        str_output = f'Focus: {self.focus} \
                        \nEnergy Level: {self.__energy_lvl} \
                        \nWorkout Time: {self.__time} \
                        \nCardio Included: {has_cardio}'
        return str_output


class FullBody(SingleBody):
    '''Full Body Class'''
    # inherit from SingleBody parent class

    def __init__(self, extra, focus, energy_lvl, time, cardio=None):
        ''' Initializer / Instance '''
        self.focus = focus
        self.cardio = cardio
        self.__energy_lvl = energy_lvl
        self.__time = time
        self.__extra = extra # all extra body part excluding first in list
        # initialize super (or parent) class instance vars
        super().__init__(\
            self.focus, self.__energy_lvl, self.__time, self.cardio)


    def full_body_workout(self):
        '''Generate Full Body Workout Method'''
        workout_lst = []

        # generate first workout plan
        first_workout = self.generate_workout()
        workout_lst.append(first_workout)

        # generate first workout plan
        for item in self.__extra:
            add_workout = self.generate_workout(body=item)
            workout_lst.append(add_workout)
        
        return workout_lst
    
    def __repr__(self):
        '''Repr Method'''
        has_cardio = False if self.cardio is None else True
        str_output = f'Focus: {[self.focus] + self.__extra} \
                        \nEnergy Level: {self.__energy_lvl} \
                        \nWorkout Time: {self.__time} \
                        \nCardio Included: {has_cardio}'
        return str_output


# Unit Test 
if __name__ == '__main__':
    '''Unit Test to Test'''
    ## UNIT TEST EXAMPLE ##
    # Test read_file function
    arm = f.read_file('focus/arm.txt')
    test_arm = {\
        'tricep dips',
        'bicep curls',
        'pushups', # comment out this line to test ASSERT
        'hammer curls',
        'cable tricep pushdown',
        'overhead extensions',
        'skull crusher'
    }
    
    assert arm == test_arm, 'ASSERT -- Read is Wrong!!!'

    cardio = f.read_file('focus/cardio.txt')
    test_cardio = {'jog', 'elliptical', 'bike', 'jumping jacks', 'jumprope'}
    bad_method = {'test', 'bad', 'method'}

    assert cardio == test_cardio, 'ASSERT -- Read is Wrong!!!'

    # Test SingleBody Class Initializer
    singlebody_workout = SingleBody(\
        focus=arm,
        energy_lvl='low',
        time=20,
        cardio=cardio
    )
    print(f'Test SingleBody Class Initializer:\n{singlebody_workout}\n')
    # Test Method generate_cardio()
    test_gc = singlebody_workout.generate_cardio()
    print(f'Test Method generate_cardio()\n{test_gc}\n')

    # unit test / assert to validate generate_cardio() method
    assert test_gc[0] == 10, 'Value is not 10 for \'low\' energy_lvl'
    for item in test_gc[1]:
        # validate item is part of set of cardio
        # use 'bad_method' in place of 'test_cardio' to Test Assert
        # unit test / assert to validate generate_cardio() method
        assert item in test_cardio, 'Item not part of Cardio'
        # assert item in bad_method, 'Item not part of Cardio' #fail assert test
        


    # Test Method generate_workout()
    test_gw, test_set = singlebody_workout.generate_workout()
    print(f'Test Method generate_workout()\n{test_gw} - {test_set}\n')
    print(test_gw)
    print(test_gw.keys())
    for k in test_gw.keys():
        # validate return in Method generate_workout() is in set of test_arm
        # use 'bad_method' in place of 'test_arm' to Test Assert
        assert k in test_arm # working assert test
        # assert k in bad_method #fail assert test