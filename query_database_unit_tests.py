import unittest
import sqlite3
from query_database import create_connection, select_row


class TestQueryDatabase(unittest.TestCase):

    def setUp(self):
        self.db_file = ":memory:"  # Use in-memory database for testing

    def test_create_connection(self):
        conn = create_connection(self.db_file)
        self.assertIsInstance(conn, sqlite3.Connection)
        conn.close()

    def test_select_row(self):
        conn = create_connection(self.db_file)
        cursor = conn.cursor()

        # Create a test table
        cursor.execute('''CREATE TABLE IF NOT EXISTS characters (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            age INTEGER,
                            gender TEXT)''')

        # Insert some test data
        cursor.execute("INSERT INTO characters (name, age, gender) VALUES (?, ?, ?)", ("Harry Potter", 17, "Male"))
        cursor.execute("INSERT INTO characters (name, age, gender) VALUES (?, ?, ?)", ("Hermione Granger", 17, "Female"))
        conn.commit()

        # Test selecting a row
        selected_row = select_row(conn, "characters", "Harry Potter")
        expected_row = {'id': 1, 'name': 'Harry Potter', 'age': 17, 'gender': 'Male'}
        self.assertEqual(selected_row, expected_row)

        # Test selecting a non-existent row
        selected_row = select_row(conn, "characters", "Ron Weasley")
        self.assertIsNone(selected_row)

        conn.close()


if __name__ == '__main__':
    unittest.main()
