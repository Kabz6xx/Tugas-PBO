class Brand:
    def __init__(self, brand, car_type, color, year):
        self.brand = brand        
        self.car_type = car_type    
        self.color = color          
        self.year = year            

    def display_info(self):
        print(f"Brand: {self.brand} | Type: {self.car_type} | Color: {self.color} | Year: {self.year}")


car1 = Brand("Honda", "Civic", "Black", 2023)
car2 = Brand("Toyota", "Supra MK4", "White", 2002)
car3 = Brand("Porsche", "GT3 RS", "Silver", 2011)
car4 = Brand("Nissan", "GTR Nismo", "White", 2023)


print("--- Car Showroom Inventory ---")
car1.display_info()
car2.display_info()
car3.display_info()
car4.display_info()
