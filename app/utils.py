from faker import Faker


def fake_data():
    fake = Faker()
    return fake.date_time_this_month()


def get_fields_name(classname):
    return classname.__table__.columns.keys()


if __name__ == "__main__":
    print(fake_data())
