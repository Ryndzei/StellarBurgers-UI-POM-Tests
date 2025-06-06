from faker import Faker


faker = Faker()

def random_email():
    return faker.email()

def generate_user_register_body():

    return {
        "email": faker.email(domain="yandex.ru"),
        "password": faker.password(),
        "name": faker.user_name()
    }
