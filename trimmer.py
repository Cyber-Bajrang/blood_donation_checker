class donor:
    def __init__(self, Donor):
        self.Donor = Donor
    def rh_factor(self):
        return self.Donor[-1]
    def group(self):
        return self.Donor[:-1]

class receiver(donor):
    def __init__(self, receiver):
        super().__init__(receiver)
        self.receiver = receiver
        

