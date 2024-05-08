from models.__init__ import CURSOR, CONN

class State:
    all = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "name must be a non-empty string"
            )
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS states(
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS states;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO states (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        state = cls(name)
        state.save()
        return state
        
    def update(self):
        sql = """
            UPDATE states
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM states
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        state = cls.all.get(row[0])
        if state:
            state.name = row[1]
        else:
            state = cls(row[1])
            state.id = row[0]
            cls.all[state.id] = state
        return state

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM states
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM states
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return [cls.instance_from_db(row) if row else None]
    
    def cities(self): #Gets all cities in this State
       from models.city import City
       breakpoint()
       sql = """
            SELECT *
            FROM cities
            WHERE state_id = ?
        """
       rows = CURSOR.execute(sql ,(self.id,)).fetchall()
       return [City.instance_from_db(row) for row in rows]