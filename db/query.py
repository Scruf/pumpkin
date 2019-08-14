from .consts import CAT_BREED_FACTORS, \
                    DOG_BREED_FACTORS, \
                    AGE_FACTORS, \
                    SPECIES_FACTORS, \
                    ZIPCODE_FACTORS


def get_age(age):
    if age < 1:
        return AGE_FACTORS.get("<1")

    if age > 8:
        return AGE_FACTORS.get(">8")

    return AGE_FACTORS[str(age)]


def get_breed_factor(breed, species):
    if species == "cat":
        return SPECIES_FACTORS["cat"],\
             CAT_BREED_FACTORS.get(breed, CAT_BREED_FACTORS["DEFAULT"])
    else:
        return SPECIES_FACTORS["dog"],\
             DOG_BREED_FACTORS.get(breed, DOG_BREED_FACTORS["DEFAULT"])


def pet_query(id):
    return f"SELECT age, breed, zipcode, species FROM pet WHERE id = '{id}'"


def get_quote(id, connection):
    with connection as conn:
        query = conn.execute(pet_query(id))

        result = query.fetchall()
        if result:
            age, breed, zipcode, species = result[0]

            age = get_age(age)

            breed, species = get_breed_factor(breed, species)

            quote = 45 * sum([age,
                              breed,
                              species,
                              ZIPCODE_FACTORS.get(str(zipcode),
                              ZIPCODE_FACTORS["DEFAULT"])])

            conn.close()

            return quote, False
        else:
            return 0.0, True
