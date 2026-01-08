from faker import Faker

fake = Faker('ru_RU')

print("имя:", fake.name())
print("адрес:", fake.address())
print("email:", fake.email())