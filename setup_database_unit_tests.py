"""
Aqueno Amalraj, Minna Chae, Sarah St. Albin
TCSS 504
Assignment: Dungeon Adventure 2.0
"""

import unittest
import sqlite3
from unittest.mock import patch
from setup_database import create_connection, create_table, main


class TestDatabaseSetup(unittest.TestCase):

    def setUp(self):
        self.db_file = ":memory:"  # Use in-memory database for testing

    def test_create_connection(self):
        conn = create_connection(self.db_file)
        self.assertIsInstance(conn, sqlite3.Connection)
        conn.close()

    def test_create_table(self):
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS test_table (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            );
        """
        conn = sqlite3.connect(self.db_file)
        create_table(conn, create_table_sql)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='test_table';")
        result = cursor.fetchone()
        self.assertIsNotNone(result)
        cursor.close()
        conn.close()

    @patch('builtins.print')  # Mock print function
    def test_main(self, mock_print):
        main()
        mock_print.assert_not_called()  # Assert print wasn't called, so tables & database successfully created


if __name__ == '__main__':
    unittest.main()
