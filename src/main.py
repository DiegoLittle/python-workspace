from db import initalize_db
from services.dummy import Dummy


def main():
    initalize_db()
    dummy = Dummy(title="Test", description="Test")
    dummy.save()
    dummy2 = Dummy(id=dummy.id)
    print(dummy2.get_all())
    dummy2.delete()
    print(dummy2.read())


main()
