class Store:
    value: float = 0


    def __init__(self, in_min: float = 0, in_max: float = 1, out_min: float = 0, out_max: float = 1):
        self.in_min = in_min
        self.in_max = in_max
        self.out_min = out_min
        self.out_max = out_max
    
    
    def normalize_in(self, value: float):
        limited = min(self.in_max, max(self.in_min, value))
        normalized = (limited - self.in_min) / (self.in_max - self.in_min)
        return normalized

    
    def normalize_out(self, value: float) -> float:
        return value * (self.out_max - self.out_min) + self.out_min
        

    def set(self, value: float):
        self.value = self.normalize_in(value)

    
    def get(self) -> float:
        return self.normalize_out(self.value)
