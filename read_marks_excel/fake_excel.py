import random
from pprint import pprint

import pandas as pd
from faker import Faker


def create_fake_data():
    fake = Faker()
    fake.seed(4321)
    random.seed(4321)
    pprint(fake.name())
    pprint(random.randint(1, 100))



    name_list = []
    for i in range(10):
        name_list.append(fake.name())

    list_of_details = []
    for i in range(10):
        list_of_details.append(
            {
                "name": name_list[random.randint(0, 9)],
                "marks": random.randint(1, 100),
                "max_marks": 100,
                "subject" : fake.company(),
                "topic" : fake.person(),

            }
        )
    df = pd.DataFrame(list_of_details)
    df.to_excel("fake_sheet.xlsx")


if __name__ == "__main__":
    create_fake_data()
