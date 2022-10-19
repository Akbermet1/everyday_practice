from typing import Union

from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

import unidecode
from slugify import slugify


app = FastAPI()


class ClassModel(str, Enum):
    security_of_cs = "Security of Computer Systems"
    team_proj = "Team_Project"
    computer_graphics = "Computer_Graphics"
    basics_of_ent_man = "Basics of Entrepreneurship and Management"
    deg_proj_1_prep_ba = "Degree Project 1 and Preparation for BA"
    dev_games_unity = "Developing Games in Unity"
    design_business_intel_tools = "Design of Business Intelligence Tools"
    lab_digital_med_images = "Laboratory of Digital Medical Images"
    challenges_it_labour = "Challenges of the IT Labour Market"


class Item(BaseModel):
    name: str
    price: float
    purchaser: Union[str, None] = None
    bought_at: Union[str, None] = None
    date: str
    price_per_person: Union[float, None] = None


def generate_slug(word: str):
    word_in_latin_chars = unidecode.unidecode(word)
    slug = slugify(word_in_latin_chars)
    return slug


@app.get("/")
async def root():
    return {"message": "Hello World"}


list_of_classes = ["Security of Computer Systems", "Computer Graphics",
                   "Team Project", "Basics of Entrepreneurship and Management"]


@app.get("/classes/")
async def list_classes():
    return list_of_classes


@app.get("/classes/{class_id}/")
async def get_class(class_id: ClassModel):
    if class_id == ClassModel.computer_graphics or class_id == ClassModel.dev_games_unity:
        return {
            "class_id": class_id,
            "message": "One of my fav classes!"
        }
    else:
        return {
            "class_id": class_id,
            "message": "Regular class!"
        }


@app.post("/classes/{class_title}/")
async def add_class(class_title: str):
    class_slug = generate_slug(class_title)
    return {
        "class slug": class_slug,
        "class title": class_title.capitalize()
    }


all_items = []


@app.get("/items/")
async def list_items():
    return {"list of items": all_items}


@app.post("/items/")
async def create_item(item: Item):
    price_per_person = round(item.price / 4.0, 2)
    print(f"price per person: {price_per_person}")
    item.price_per_person = price_per_person
    all_items.append(item)
    return item
