import os
import sys
import subprocess

from utils.csv_service import CSVService


class SystemSetup:
    def set_utf8_encoding(self):
        if os.name == 'nt':
            os.system('chcp 65001 > NUL')
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')

    def install_requirements(self):
        req_file = 'requirements.txt'
        if os.path.exists(req_file):
            print('Instalando dependências...')
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', req_file])
        else:
            print('Arquivo requirements.txt não encontrado. Pulando instalação de dependências.')

    def __init__(self):
        self.set_utf8_encoding()
        self.install_requirements()
        print('Configuração inicial concluída. Ambiente pronto para rodar o sistema de bilheteria.')



class DataBaseSetup:
    def __init__(self):
        print("Iniciando o setup do sistema...")
        products_header = ['ID_PRODUCT', 'NAME', 'QUANTITY', 'PRICE', 'TAGS'],
        products_data = [['P1',"PIPOCA", 1000, 10.0, ['SNACK', 'FOOD']],
                        ['P2',"REFRIGERANTE", 1000, 5.0, ['SNACK', 'DRINK']],
                        ['P3',"CACHORRO_QUENTE", 1000, 15.0, ['SNACK', 'FOOD']],
                        ['P4',"COMBO_1", 1000, 20.0, ['SNACK', 'COMBO_1']],
                        ['P5',"COMBO_2", 1000, 30.0, ['SNACK', 'COMBO_2']]]
        CSVService().write_csv('repositories/products', 'products.csv', products_data, header=products_header)


        sessions_header = ['ID_SESSION', "LOCAL", "MOVIE", "DATE"]
        sessions_data = [['1',"TIETE_PLAZA", "STITCH", "2025-06-18T22:00:00"]]
        CSVService().write_csv('repositories/sessions', 'sessions.csv', sessions_data, header=sessions_header)


        shopping_list_header = ['ID_PRODUCT', 'NAME', 'QUANTITY', 'PRICE', 'ID_WEB_SESSION', 'ID_USER']
        shopping_list_data = []
        CSVService().write_csv('repositories/shopping_list', 'shopping_list.csv', shopping_list_data, header=shopping_list_header)


        tickets_header = ['ID_TICKET', 'TICKET_COORDENATES', "ID_SESSION", "RESERVATION", "BUY", "ID_USER", "ID_WEB_SESSION", 'tags', 'PRICE']
        tickets_data = [['T1', ["A", "1", "1"], 1,  False, False, None, None, ['PCD', 'COMBO_1'], 20.0],
                        ['T2', ["A", "2", "1"], 1,  False, False, None, None, ['PCD', 'COMBO_1'], 20.0],
                        ['T3', ["A", "3", "1"], 1,  False, False, None, None, ['PCD', 'COMBO_1'], 20.0],
                        ['T4', ["B", "1", "1"], 1,  False, False, None, None, ['STANDART', 'COMBO_1'], 20.0],
                        ['T5', ["B", "2", "1"], 1,  False, False, None, None, ['NAMORADEIRA', 'COMBO_1'], 30.0],
                        ['T6', ["B", "3", "1"], 1,  False, False, None, None, ['STANDART', 'COMBO_1'], 20.0]]
        CSVService().write_csv('repositories/tickets', 'tickets.csv', tickets_data, header=tickets_header)


        virtual_queue_header = ['ID_WEB_SESSION', 'ID_USER']
        virtual_queue_data = []
        CSVService().write_csv('repositories/virtual_queue', 'virtual_queue.csv', virtual_queue_data, header=virtual_queue_header)


        users_header = ['ID_USER', 'NAME', 'EMAIL', 'PASSWORD']
        users_data = [['1', 'teste', 'teste', 'teste']]
        CSVService().write_csv('repositories/users', 'users.csv', users_data, header=users_header)

        print("Setup concluído com sucesso!")
