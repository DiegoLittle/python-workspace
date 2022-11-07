import json
from db.base import SessionLocal
from db.models.Dummy import DummyModel
from db.utils import (
    deserialize_sql_model,
    isJsonDeserializable,
    isJsonSerializable,
    object_as_dict,
)


class Dummy:
    def __init__(
        self,
        id: str = None,
        title: str = None,
        description: str = None,
        meta_data: dict = None,
    ):
        self.id = id
        if id:
            self.read()
            self.meta_data = {
                "created_at": "2020-01-01 00:00:00",
                "updated_at": 10,
                "test": False,
            }
        else:
            self.title = title
            self.description = description
            self.meta_data = {
                "created_at": "2020-01-01 00:00:00",
                "updated_at": 10,
                "test": False,
            }

    def save(self):
        """Add a new dummy to the database.
        Args:
            dummy (Dummy): The dummy to add.

        Returns:
            Dummy: The dummy that was added.

        """
        db_session = SessionLocal()
        dummy = DummyModel(**self.sql_serialize)

        db_session.add(dummy)
        db_session.commit()
        db_session.refresh(dummy)
        db_session.close()
        self.id = dummy.id

        return dummy

    def read(self):
        """Get all dummies from the database.

        Returns:
            List[Dummy]: A list of all dummies.

        """
        db_session = SessionLocal()
        dummy = db_session.query(DummyModel).filter(DummyModel.id == self.id).first()
        if dummy is None:
            return None
        db_session.close()
        for key, value in deserialize_sql_model(dummy).items():
            setattr(self, key, value)

        return self

    def get_all(self, offset: int = 0, limit: int = 100000):
        """Get all dummies from the database.

        Returns:
            List[Dummy]: A list of all dummies.

        """
        db_session = SessionLocal()
        dummies = db_session.query(DummyModel).offset(offset).limit(limit).all()
        db_session.close()
        dummy_objs = []
        for dummy_sql in dummies:
            dummy = Dummy()
            for key, value in deserialize_sql_model(dummy_sql).items():
                setattr(dummy, key, value)
            dummy_objs.append(dummy)

        return dummy_objs

    def delete(self):
        """Delete a dummy from the database.

        Returns:
            None

        """
        db_session = SessionLocal()
        dummies = db_session.query(DummyModel).filter(DummyModel.id == self.id).first()
        db_session.delete(dummies)
        db_session.commit()
        db_session.close()

    @property
    def dict(self):
        return_dict = {}
        for key, value in self.__dict__.items():
            if isJsonSerializable(value):
                return_dict[key] = value

        return return_dict

    @property
    def sql_serialize(self):
        return_dict = {}
        for key, value in self.__dict__.items():
            if (
                type(value) == bool
                or type(value) == int
                or type(value) == float
                or type(value) == str
            ):
                return_dict[key] = value
            elif type(value) == dict and isJsonSerializable(value):
                return_dict[key] = json.dumps(value)
        return return_dict
