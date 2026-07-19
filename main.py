from donation import donor
def main():
    d = input("Enter donor blood group: ")
    r = input("Enter recipient blood group: ")
    b = blood(d, r)
    b.cangive()
class blood:
    def __init__(self, donor, recipient):
        self.donor = donor
        self.recipient = recipient  
    def cangive(self):
        if self.recipient in donor.get(self.donor):
            print(True)
        else:
            print(False)

main()