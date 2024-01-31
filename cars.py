
import random

de main ():
	carBrands=["Toyota", "BMW" , "Mercedes" , "Lexus" , "Nissan" , "Kia"]
	randomBrands=random.choice(carBrands)
	print("Car Brand: " , randomBrand)


def get_model_year():
	return random.randint(1990,2024)



if _ _name_ _=="_ _main_ _":
	main()

