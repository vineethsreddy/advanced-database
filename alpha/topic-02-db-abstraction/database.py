import sqlite3

connection = sqlite3.connect("shopping-list.db")

def get_items(id=None):
    cursor = connection.cursor()
    if id == None:
        rows = cursor.execute("select id, description from list")
    else:
        rows = cursor.execute(f"select id, description from list where id={id}")
    rows = list(rows)
    rows = [ {'id' : row[0], 'description': row[1]} for row in rows ]
    return rows

def add_item(description):
    cursor = connection.cursor()
    cursor.execute(f"insert into list(description) values ('{description}')")
    connection.commit()

def update_item(id, description):
    print("update item = ",[id, description])
    cursor = connection.cursor()
    statement = f"update list set description='{description}' where id={id}"
    print("update statement = ",[statement])
    cursor.execute(statement)
    connection.commit()

def set_up_database():
    cursor = connection.cursor()
    try:
        cursor.execute("drop table list")
    except:
        pass
    cursor.execute("create table list(id integer primary key, description text)")
    for item in ['apples', 'broccoli', 'pizza', 'tangerine', 'potatoes']:
        cursor.execute(f"insert into list (description) values ('{item}')")
    connection.commit()

def test_set_up_database():
    print("testing set_up_database()")
    set_up_database()
    items = get_items()
    assert len(items) == 5
    descriptions = [item['description'] for item in items]
    for description in ['apples', 'broccoli', 'pizza', 'tangerine', 'potatoes']:
        assert description in descriptions

def test_get_items():
    print("testing get_items()")
    items = get_items()
    assert type(items) is list
    assert len(items) > 0
    for item in items:
        assert type(item) is dict
        assert 'id' in item
        assert type(item['id']) is int
        assert 'description' in item
        assert type(item['description']) is str
    id = items[0]['id']
    description = items[0]['description']
    items = get_items(id)
    assert type(items) is list
    assert len(items) == 1
    assert items[0]['id'] == id
    assert items[0]['description'] == description

def test_add_item():
    print("testing add_item()")
    set_up_database()
    items = get_items()
    original_length = len(items)
    add_item("mango")
    items = get_items()
    assert len(items) == original_length + 1
    descriptions = [item['description'] for item in items]
    assert "mango" in descriptions

def test_update_item():
    print("testing update_item()")
    set_up_database()
    items = get_items()
    id = items[2]['id']
    description = items[2]['description']
    update_item(id, "chocolate")
    items = get_items()
    assert items[2]['description'] == "chocolate"

if __name__ == "__main__":
    test_set_up_database()
    test_get_items()
    test_add_item()
    test_update_item()
    print("done.")
