from fastapi import APIRouter
from ..models.lessons import Item

router = APIRouter(
    prefix="/lessons"
)

ITEMS = [
    Item(name="item1", price=10.0),
    Item(name="item2", price=20.0),
]

# CRUD - CREATE, READ, UPDATE, DELETE
@router.get("/items")
def read_items():
    global ITEMS
    return ITEMS


# READ
@router.get("/items/{item_name}")
def read_item(item_name: str):
    global ITEMS
    result =  [
        i for i in ITEMS
        if i.name == item_name
    ]
    if result:
        return result[0]
    return {}

# CREATE
@router.post("/items")
def create_item(item: Item):
    global ITEMS
    ITEMS.routerend(item)
    return ITEMS

# DELETE
@router.delete("/items/{item_name}")
def delete_item(item_name: str):
    global ITEMS
    ITEMS = [
        i for i in ITEMS
        if i.name != item_name
    ]
    return ITEMS


# UPDATE
@router.put("/items/{item_name}")
def update(item_name: str, new_item: Item):
    global ITEMS
    result = [
        item if item.name != item_name else new_item
        for item in ITEMS
    ]
    return result


@router.get("/")
def read_root():
    return {"result": "Estou dentro do lessons˜"}


