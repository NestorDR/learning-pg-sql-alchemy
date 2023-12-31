# -*- coding: utf-8 -*-

# --- Python modules ---
# datetime: provides classes for simple and complex date and time manipulation.
import datetime
# sys: module which provides access to some variables used or maintained by the interpreter and to functions that
#      interact strongly with the interpreter.
import sys
# typing: provides runtime support for type hints
from typing import List

# --- App modules ---
from pg_base import session_factory
from models.item import Item


def save(items_to_save: List[Item]):
    username = 'NestorDR'

    for item in items_to_save:
        session = session_factory()
        try:
            saved_item = session.query(Item).filter(Item.name == item.name).one_or_none()

            if saved_item:
                item.id = saved_item.id
                saved_item.position = item.position
                saved_item.price = item.price
                saved_item.amount = item.amount
                saved_item.updated_by = username
                saved_item.updated_at = datetime.datetime.now()
                operation = 'updated'
            else:
                item.created_by = username
                session.add(item)
                operation = 'added'

            session.commit()
            print(f'{item.name}({item.id}) {operation}.')

        except Exception as e:
            session.rollback()
            raise RuntimeError(f'Could not save item {item.name}\n{str(e)}') from e
        session.close()


# Use of __name__ & __main__
# When the Python interpreter reads a code file, it completely executes the code in it.
# For example, in a file my_module.py, when executed as the main program, the __name__ attribute will be '__main__',
# however if it is used importing it from another module: import my_module, the __name__ attribute will be 'my_module'.
if __name__ == '__main__':
    items = [
        Item(name='Alcohol', position=1, price=10, amount=1.5),
        Item(name='Computer', position=2, price=1000.50, amount=1),
        Item(name='Printer', position=3, price=150.75, amount=1),
        Item(name='Bike', position=4, price=350.25, amount=2),
        Item(name='Microphone', position=5, price=82.25, amount=1)
    ]

    save(items)

    # Terminate normally
    sys.exit(0)
