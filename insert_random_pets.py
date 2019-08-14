import os,time
from uuid import uuid4
from random import randint
from sqlalchemy import create_engine
from db.consts import *

def connect():
    ip = os.environ["EGOR_PUMPKIN_DB_IP"]
    connection_url = f'mysql://root:{os.environ["EGOR_PUMPKIN_DB_PASSWORD"]}@{os.environ["EGOR_PUMPKIN_DB_IP"]}:3306/'


    print("Connection url ---> ", connection_url )
    # time.sleep(40)
    engine = create_engine(connection_url)
    connection = engine.connect()

    query_create_user = "CREATE USER 'pumpkin' IDENTIFIED BY 'password';"
    connection.execute(query_create_user)

    query_grant_priveleges = "GRANT ALL PRIVILEGES ON * . * TO 'pumpkin';"
    connection.execute(query_grant_priveleges)

    query_create_database = "CREATE DATABASE Pumpkin;"
    connection.execute(query_create_database)
    connection.close()

connect()
connection_url = f'mysql://pumpkin:password@{os.environ["EGOR_PUMPKIN_DB_IP"]}:3306/Pumpkin'
print("Another one -->", connection_url)
engine = create_engine(f'mysql://pumpkin:password@{os.environ["EGOR_PUMPKIN_DB_IP"]}:3306/Pumpkin')

connection = engine.connect()


create_table_query = """
create table pet
(
    id      varchar(32) not null,
    age     int         null,
    breed   varchar(35) null,
    zipcode int         null,
    name    varchar(50) null,
    gender  varchar(7)  null,
    species varchar(30) null,
    constraint Pet_id_uindex
        unique (id)
);

"""

alter_table_query = """
alter table pet
    add primary key (id);
"""

connection.execute(create_table_query)
connection.execute(alter_table_query)

names=  ['Cara',
    'Berna',
    'Adena',
    'Tyree',
    'Charisse',
    'Archie',
    'Maia',
    'Jenni',
    'Patrina',
    'Herma',
    'Aja',
    'Janette',
    'Marge',
    'Boris',
    'Alysha',
    'Jamel',
    'Floretta',
    'Oretha',
    'Sherita',
    'Rea',
    'Ian',
    'Van',
    'Augustus',
    'Myrle',
    'Johna',
    'Nick',
    'Augustine',
    'Mohammad',
    'Vikki',
    'Cecelia',
    'Quinn',
    'Jerry',
    'Astrid',
    'Leroy',
    'Dorine',
    'Damien',
    'Corrina',
    'Kanesha',
    'Mistie',
    'Belen',
    'Elma',
    'Florance',
    'Robert',
    'Doretha',
    'Magan',
    'Kathryne',
    'Kiara',
    'Tai',
    'Kim',
    'Celina']

age_dict = AGE_FACTORS
cat_dict = CAT_BREED_FACTORS
dog_breed_dict = DOG_BREED_FACTORS
speecies_dict = SPECIES_FACTORS
zip_code_dict = ZIPCODE_FACTORS

        
for name in names:
    name_dict = {}
    name_dict['name'] = name
    name_dict["id"] = ''.join(str(uuid4()).split("-"))
    name_dict["gender"] = "Male" if randint(0,1) == 1 else "Female"
    name_dict["species"] = "dog" if randint(0,1) == 1 else "cat"

    age_list = list(age_dict.keys())
    random_age_position = randint(0, len(age_list)-1)
    name_dict["age"] = age_list[random_age_position]

    zip_code_list = list(zip_code_dict.keys())
    random_age_position = randint(0, len(zip_code_list)-1)
    name_dict["zipcode"] = zip_code_list[random_age_position]

    if name_dict["species"] == "dog":
        dog_breed_list = list(dog_breed_dict.keys())
        random_breed_position = randint(0, len(dog_breed_list)-1)
        name_dict["breed"] = dog_breed_list[random_breed_position]
    else:
        cat_breed_list = list(cat_dict.keys())
        random_breed_position = randint(0, len(cat_breed_list)-1)
        name_dict["breed"] = cat_breed_list[random_breed_position]
        
    if name_dict['age'] == ">8":
        name_dict["age"] = 10
    if name_dict["age"] == "<1":
        name_dict["age"] = 0
        
    insert_query = f"INSERT INTO pet(id,age,breed,zipcode,name,gender,species) VALUES ('{name_dict['id']}',{name_dict['age']},'{name_dict['breed']}', {name_dict['zipcode']}, '{name_dict['name']}', '{name_dict['gender']}', '{name_dict['species']}')"
    print("Inserting pet with information --> ", name_dict)
    connection.execute(insert_query)