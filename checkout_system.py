class Product:
    def __init__(self,SKU,name,price):
        self.SKU = SKU
        self.name = name
        self.price = price
        self.pieces = 0
        self.total_worth = 0
    
    def total_number(self,SKU):
        if self.SKU == SKU:
            self.pieces += 1
        return self.pieces
    
    def worth(self):
        if self.pieces>0:
            self.total_worth = self.pieces * self.price
        return self.total_worth

# define discount rules and return total prices
def pricing(total_product):
    total_price = 0
    for product in total_product:
        product.total_number(product.SKU)
        
    if ipd.pieces > 4:
        ipd.price = 499.9
    if atv.pieces >=3:
        mod = atv.pieces%3
        atv.pieces = atv.pieces - ((atv.pieces-mod)//3) 
    if mbp.pieces>0:
        vga.pieces -= mbp.pieces
    
    for each in set(total_product):
        total_price += each.worth()
    return total_price

ipd = Product('ipd','Super Ipad',549.99)
mbp = Product('mbp','MacBook Pro',1399.99)
atv = Product('atv','Apple TV',109.5)
vga = Product('vga','VGA adapter',30)
total_product = [atv, ipd, ipd, atv, ipd, ipd, ipd]
print(pricing(total_product))