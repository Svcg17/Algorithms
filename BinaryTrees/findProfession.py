"""
    This tree is a family tree of Engineers and Doctors
    Each engineer has left: engineer, right: doctor
    Each doctor has left: doctor, right: engineer
                E
           /         \
          E           D
        /   \\        /  \
       E     D      D    E
      / \\   / \\    / \\   / \
     E   D D   E  D   E E   D
    """


def findProfession(level, pos):
    """
    Finds profession of a given family memeber of the above tree.
    Args:
        @level: Level of tree
        @pos: position of the member in the level
    Return:
        The member's profession(Engineer or Doctor)
    """
    if level == 1:
        return 'Engineer'
    p = findProfession(level - 1, (pos + 1) // 2)
    if p == 'Engineer':
        if (pos % 2 == 0):
            return 'Doctor'
        else:
            return 'Engineer'
    else:
        if (pos % 2 == 0):
            return 'Engineer'
        else:
            return 'Doctor'
