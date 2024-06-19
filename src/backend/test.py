from databaseservice import DatabaseService
from mitarbeiter_verwaltung import MitarbeiterVerwaltung

test = MitarbeiterVerwaltung()

# test.add_abteilung("Testabteilung", "Sanitär")

test.get_all_abteilungen()

# test.add_test_table()

# test.execute_query("""
# INSERT INTO test VALUES (1, "Test123")                
# """)

# res = test.execute_query("""
# SELECT * FROM test;                      
# """)

# print(res.fetchall())

# test.delete_test_table()

