

class Genome:
    
    def __init__(self) -> None:
        self.id =0
        self.gene = 0


class Position:
    def __init__(self, one , two, three) -> (None):
        self.one = one
        self.two =two 
        self.three = three 



class ORF:
    def __init__(self, id , frame, orf, start , end) -> (None):
        self.id = id
        self.frame = frame
        self.orf = orf
        self.start = start
        self.end = end

