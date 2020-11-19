class Store:
    encoding = 'utf8'

    def __init__(self):
        self.value = None 
        pass


    def set(self, value):
        self.value = value

    
    def get(self):
        return self.value
