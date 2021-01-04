"""Contains ItemAlreadyStored and ItemNotStored exceptions
Controller class and View class
"""
import mvc_exceptions as mvc_exc
import model as data
import view as presentation
import controller as logic

items = list() # global variable where we keep the data

def create_item(name, price, quantity):
    """creates an item"""
    global items
    results = list(filter(lambda x: x['name'] == name, items))
    if results:
        raise mvc_exc.ItemAlreadyStored('"{}" already stored'.format(name))
    items.append({'name': name, 'price': price, 'quantity': quantity})

def create_items(app_items):
    """creates a list of items"""
    global items
    items = app_items

def read_item(name):
    """reads an item"""
    global items
    myitems = list(filter(lambda x: x['name'] == name, items))
    if myitems:
        return myitems[0]
    raise mvc_exc.ItemNotStored(
        'Can\'t read "{}" because it\'s not stored'.format(name))

def read_items():
    """reads a list of items"""
    global items
    return [item for item in items]

def update_item(name, price, quantity):
    """updates an item Python 3.x removed tuple parameters unpacking
    (PEP 3113), so we have to do it manually (i_x is a tuple, idxs_items
    is a list of tuples)
    """
    global items
    idxs_items = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i, item_to_update = idxs_items[0][0], idxs_items[0][1]
        items[i] = {'name': name, 'price': price, 'quantity': quantity}
    else:
        raise mvc_exc.ItemNotStored(
            'Can\'t update "{}" because it\'s not stored'.format(name))

def main():
    """main function"""
    my_items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ]

    ctrlr = logic.Controller(data.ModelBasic(my_items), presentation.View())

    print('show items without bullet points')
    ctrlr.show_items()
    print('show items with bullet points')
    ctrlr.show_items(bullet_points=True)
    print('show item not in list')
    ctrlr.show_item('chocolate')
    print('show item in list')
    ctrlr.show_item('bread')
    print('trying to insert duplicate item')
    ctrlr.insert_item('bread', price=1.0, quantity=5)
    print('inserting a valid item')
    ctrlr.insert_item('chocolate', price=2.0, quantity=10)
    print('showing the last item inserted')
    ctrlr.show_item('chocolate')
    print('updating an item')
    ctrlr.update_item('milk', price=1.2, quantity=20)
    print('trying to update an item that\'s not in the list')
    ctrlr.update_item('ice cream', price=3.5, quantity=20)

if __name__ == '__main__':
    main()
