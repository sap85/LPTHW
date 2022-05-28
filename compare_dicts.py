data_set_1 = {"asset_tag": "KA-62636465",
"asset_id": "311807",
"cluster": "01",
"console_port": "7008",
"datacenter": "AUS1",
"device_type": "11",
"id": "311807",
"maintenance_status": 2,
"model_id": "37",
"name": "TOR1_01_AUS1",
"rack": "07",
"rack_serial": "2MB5",
"serial_number": "ABC12345",
"state": "3",
"status": "7",
"switch_serial": "SW12345",}

data_set_2 = {
"maintenance_status": "2",
"datacenter": "aus1",
"name": "TOR1_01_AUS1",
"rack_serial": "2MB5",
"rack": "07",
"switch_serial": "SW12345",
"primary_ipv6": "",
"cluster": "01",
"asset_tag": "KA-62636465",
"status": "7",
"state": "3",
"device_type": "11",
"serial_number": "ABC12345",
"asset_id": "311807",
"model_id": "37"}

def dict_compare():
    data_set_1_keys = set(data_set_1.keys())
    data_set_2_keys = set(data_set_2.keys())

    shared_keys = data_set_1_keys.intersection(data_set_2_keys)

    only_in_data_set_1 = data_set_1_keys - data_set_2_keys

    only_in_data_set_2 = data_set_2_keys - data_set_1_keys

    modified = {i : (data_set_1[i], data_set_2[i]) for i in shared_keys if data_set_1[i] != data_set_2[i]}

    in_both = set(o for o in shared_keys if data_set_1[o] == data_set_2[o])
    #return added, removed, modified, same
    print("in_data_Set_2", only_in_data_set_2,"\n")

    print(" in_data_Set_1", only_in_data_set_1,"\n")

    print("in_both",in_both,"\n")

    print("modified",modified)

dict_compare()
