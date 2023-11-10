from fastapi import FastAPI

app = FastAPI()


from fastapi import FastAPI

items_db = [
        {"item_name":"Foo"},
        {"item_name":"Bar"},
        {"item_name":"Baz"}
            ]


@app.get("/items")
def read_item(skip: int = 0, limit: int = 10):
    return items_db[skip: skip + limit]


@app.get('/items/{item_id}')
def get_item(item_id: int, q: str | None = None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}

@app.get('/users/{user_id}/items/{item_id}')
def get_update_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is a text having an amazing and long description"})
    return item
