import functions as f
import BodyWorkout

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
    singlebody_workout = BodyWorkout.SingleBody(\
        focus=arm,
        energy_lvl='low',
        time=20,
        cardio=cardio
    )
    print(f'Test SingleBody Class Initializer:\n{singlebody_workout}\n')
    # Test Method generate_cardio()
    test_gc = singlebody_workout.generate_cardio()
    print(f'Test Method generate_cardio()\n{test_gc}\n')

    assert test_gc[0] == 10, 'Value is not 10 for \'low\' energy_lvl'
    for item in test_gc[1]:
        # validate item is part of set of cardio
        # use 'bad_method' in place of 'test_cardio' to Test Assert
        assert item in test_cardio, 'Item not part of Cardio'
        


    # Test Method generate_workout()
    test_gw, test_set = singlebody_workout.generate_workout()
    print(f'Test Method generate_workout()\n{test_gw} - {test_set}\n')
    print(test_gw)
    print(test_gw.keys())
    for k in test_gw.keys():
        # validate return in Method generate_workout() is in set of test_arm
        # use 'bad_method' in place of 'test_arm' to Test Assert
        assert k in test_arm
    

'''
if __name__ == '__main__':
    arm = f.read_file('focus/arm.txt')
    cardio = f.read_file('focus/cardio.txt')
    core = f.read_file('focus/core.txt')
    leg = f.read_file('focus/leg.txt')
    print(arm, '\n', cardio)
    workout = SingleBody(focus=arm,energy_lvl='high', time=20, cardio=cardio)
    workout2 = SingleBody(focus=arm,energy_lvl='low', time=20, cardio=cardio)
    print(workout)
    print(workout.generate_cardio())
    print(workout.generate_workout())
    print(type(workout.generate_workout()))
    print(workout != workout2)

    fullworkout = FullBody(extra=[core, leg], focus=arm, energy_lvl='low', time=20, cardio=cardio)
    print('\nFull Body')
    print('-'*30)
    print(fullworkout)
    # print(type(fullworkout))
    # fullworkout.full_body_workout()
    print(fullworkout.full_body_workout())
    print(type(fullworkout.full_body_workout()))
    # print(workout.generate_set()) '''