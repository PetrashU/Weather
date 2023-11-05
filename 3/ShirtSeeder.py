from faker import Faker
from Shirt import Shirt

class ShirtSeeder:
    def GenerateShirts(self) -> list:
        id = 1
        fake = Faker()
        shirt_list = list()

        for _ in range(10):
            shirt = Shirt()
            shirt.Id = id
            id += 1
            shirt.Color = fake.safe_color_name().capitalize()
            shirt.Design = fake.paragraph(nb_sentences = 1, variable_nb_sentences = False)[:-1]
            shirt_list.append(shirt)
            
        return shirt_list