from utils.csv_service import CSVService

# service = CSVService()
# dados = [['1', 'JOAO.PEDRO@GMAIL.COM'], ['2', 'MARIA@GMAIL.COM']]
# CSVService().write_csv('repositories/virtual_queue', 'virtual_queue.csv', dados, header=['ID_WEB_SESSION', 'ID_USER'])
# conteudo = CSVService().read_csv('repositories/virtual_queue', 'virtual_queue.csv')
# CSVService().write_csv('repositories/virtual_queue', 'virtual_queue.csv', conteudo, header=['ID_WEB_SESSION', 'ID_USER'])
# conteudo = CSVService().read_csv('repositories/virtual_queue', 'virtual_queue.csv')
# print(conteudo)



# ['ID_TICKET', 'TICKET_COORDENATES', "ID_SESSION", "RESERVATION", "BUY", "ID_USER", "ID_WEB_SESSION", 'tags', 'PRICE]
dados = [['T1', ["A", "1", "1"], 1,  False, False, None, None, ['PCD', 'COMBO_1'], 20.0],
         ['T2', ["A", "2", "1"], 1,  False, False, None, None, ['PCD', 'COMBO_1'], 20.0],
         ['T3', ["A", "3", "1"], 1,  False, False, None, None, ['PCD', 'COMBO_1'], 20.0],
         ['T4', ["B", "1", "1"], 1,  False, False, None, None, ['STANDART', 'COMBO_1'], 20.0],
         ['T5', ["B", "2", "1"], 1,  False, False, None, None, ['NAMORADEIRA', 'COMBO_1'], 30.0],
         ['T6', ["B", "3", "1"], 1,  False, False, None, None, ['STANDART', 'COMBO_1'], 20.0]]

CSVService().write_csv('repositories/tickets', 'tickets.csv', dados, header=['ID_TICKET', 'TICKET_COORDENATES', "ID_SESSION", "RESERVATION", "BUY", "ID_USER", "ID_WEB_SESSION", 'tags', 'PRICE'])
conteudo = CSVService().read_csv('repositories/tickets', 'tickets.csv')
print(conteudo)


dados = [['1',"TIETE_PLAZA", "STITCH", "2025-06-18T22:00:00"]]

CSVService().write_csv('repositories/sessions', 'sessions.csv', dados, header=['ID_SESSION', "LOCAL", "MOVIE", "DATE"])
conteudo = CSVService().read_csv('repositories/sessions', 'sessions.csv')
print(conteudo)

# ['ID_PRODUCT', "NAME", "QUANTITY", "PRICE", "tags"]
dados = [['P1',"PIPOCA", 1000, 10.0, ['SNACK', 'FOOD']],
         ['P2',"REFRIGERANTE", 1000, 5.0, ['SNACK', 'DRINK']],
         ['P3',"CACHORRO_QUENTE", 1000, 15.0, ['SNACK', 'FOOD']],
         ['P4',"COMBO_1", 1000, 20.0, ['SNACK', 'COMBO_1']],
         ['P5',"COMBO_2", 1000, 30.0, ['SNACK', 'COMBO_2']]]

CSVService().write_csv('repositories/products', 'products.csv', dados, header=['ID_PRODUCT', "NAME", "QUANTITY", "PRICE", "tags"])
conteudo = CSVService().read_csv('repositories/products', 'products.csv')
print(conteudo)