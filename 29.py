class sdlc():
    def __init__(self,app,domain,):
        self.app=app
        self.domain=domain
    def planning(self):
        print(f"Its a planning block and using {self.app}")
    def development(self):
        print(f"Its a development block using {self.domain}")
    def testing(self,testserver):
        print(f"Its a tetsing block using {testserver}")
    def deployment(self,prodserver):
        print(f"Its a deployment phase using {prodserver}")

phase1=sdlc("zomato","public")
phase1.planning()

phase2=sdlc("swiggy","private")
phase2.deployment("mn053")


