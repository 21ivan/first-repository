class Human:
    def __init__(self):
        pass
        
class Man(Human):
    def __init__(self):
        Human.__init__(self)
class Woman(Human):
    def __init__(self):
        Human.__init__(self)

def God():
    return [Man(), Woman()]
