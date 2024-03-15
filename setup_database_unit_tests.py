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
        """
        Sets up in-memory database for testing
        :return: None
        """
        self.db_file = ":memory:"  # Use in-memory database for testing

    def test_create_connection(self):
        """
        Verifies that a connection is successfully created
        :return: None
        """
        conn = create_connection(self.db_file)
        self.assertIsInstance(conn, sqlite3.Connection)
        conn.close()

    def test_create_table(self):
        """
        Verifies that a table is successfully created as expected
        :return: None
        """
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

    @patch('builtins.print')
    def test_main(self, mock_print):
        """
        Test that Main works as expected
        :param mock_print: a MagicMock object of the print function
        :return: None
        """
        main()
        # Assert print wasn't called because it means tables & database are successfully created
        mock_print.assert_not_called()


if __name__ == '__main__':
    unittest.main()
