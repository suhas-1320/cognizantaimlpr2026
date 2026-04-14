import faker
from src.model.customer import Customer


class CustomerStore:
    def __init__(self, num_customers: int):
        self.customers = []
        self.faker = faker.Faker()
        self.generate_customers(num_customers)

    def generate_customers(self, num_customers: int):
        for _ in range(num_customers):
            name = self.faker.name()
            email = self.faker.email()
            dob = self.faker.date_of_birth(minimum_age=18, maximum_age=80)
            customer = Customer(name, email, dob)
            self.customers.append(customer)

    def get_customers(self) -> list[Customer]:
        return self.customers
