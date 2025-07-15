from datos import CLIENTS as clients



client_id_to_find = 4
found_client_list = [client for client in clients if client['id']==client_id_to_find]
print(found_client_list)
if not found_client_list:
    print('not found')

#print(found_client_list[0]['name'])




