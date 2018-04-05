def meeting(rooms):
    if all (i=='X' for i in rooms):
        return 'None available!'
    for i in enumerate(rooms):
        if i[1] == 'O':
            return i[0]
        else:
            pass
"""
        
Your job at E-Corp is both boring and difficult. It isn't made any easier by the fact that everyone constantly wants to have a meeting with you, and that the meeting rooms are always taken!

In this kata, you will be given an array. Each value represents a meeting room. Your job? Find the first empty one and return it's index (N.B. There may be more than one empty room in some test cases).

'X' --> busy 'O' --> empty

If all rooms are busy, return 'None available!'.


meeting(['X', 'O', 'X'])
meeting(['X'])
meeting(['O','X','X','X','X'])


def meeting(rooms):
    try:
        return rooms.index('O')
    except ValueError:
        return 'None available!'



def meeting(rooms):
    return next((i for i, r in enumerate(rooms) if r == 'O'), 'None available!')
"""
