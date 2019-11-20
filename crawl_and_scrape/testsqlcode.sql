cursor.execute(f'''
     INSERT INTO PM (title, ProductionManager)
     VALUES('{str(i)}', '{str(name)}');
''')

