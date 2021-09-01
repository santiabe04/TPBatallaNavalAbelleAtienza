class Barco:
    def __init__(self):
        self.vivo = True
    
    def tocar(self):
        '''Se hunde al barco'''
        self.vivo = False