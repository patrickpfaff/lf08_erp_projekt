from databaseservice import DatabaseService

test = DatabaseService("test.db")

test.setup_db()

# test.add_test_table()

# test.execute_query("""
# INSERT INTO test VALUES (1, "Test123")                
# """)

# res = test.execute_query("""
# SELECT * FROM test;                      
# """)

# print(res.fetchall())

# test.delete_test_table()