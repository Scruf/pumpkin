import sys, os
import pytest
sys.path.append(os.getcwd())
from db.query import *
from db.consts import *


def test_get_age():
	assert get_age(-123) == AGE_FACTORS.get("<1")

	assert get_age(123) == AGE_FACTORS.get(">8") 

	assert get_age(4) == AGE_FACTORS.get("4")

def test_get_breed_factor():
	assert get_breed_factor("DEFAULT","cat") == (SPECIES_FACTORS["cat"], CAT_BREED_FACTORS["DEFAULT"])

	assert get_breed_factor("DEFAULT", "dog") == (SPECIES_FACTORS["dog"], CAT_BREED_FACTORS["DEFAULT"])

