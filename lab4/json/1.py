import json
files = open("sample-data.json", "r")
y = json.load(files)
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
for i in range(len(y["imdata"])):
    print(y["imdata"][i]["l1PhysIf"]["attributes"]["dn"], " "*28, y["imdata"][i]["l1PhysIf"]["attributes"]["speed"], " ", y["imdata"][i]["l1PhysIf"]["attributes"]["mtu"])
