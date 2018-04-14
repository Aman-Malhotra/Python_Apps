class Enemy:
    life = 3

    def attack(self):
        print("ouch")
        self.life -= 1

    def check(self):
        if self.life <= 0:
            print("I am Dead ")
        else:
            print("i still have " + str(self.life)+ " life left ")


enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.check()
enemy2.check()