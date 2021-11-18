

class Genome:
    
    def __init__(self, id , gene) -> None:
        self.id =id
        self.gene = gene


class Position:
    def __init__(self, one , two, three, id , frame) -> (None):
        self.one = one
        self.two =two 
        self.three = three
        self.id = id
        self.frame = frame



class ORF:
    def __init__(self, id , frame, orf, start , end) -> (None):
        self.id = id
        self.frame = frame
        self.orf = orf
        self.start = start
        self.end = end

