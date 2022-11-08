class upgrades:
    def __init__(self, hab, price, lvl=1):
        self.hab = hab
        self.lvl = lvl
        self.price = price
    
    def up_lvl(self, dinheiro, upgrade_hab=2):
        if dinheiro >= self.price:
            self.hab *= upgrade_hab
            self.lvl += 1
            dinheiro -= self.price
            self.price = round(self.price * 3.5)
            
        return dinheiro