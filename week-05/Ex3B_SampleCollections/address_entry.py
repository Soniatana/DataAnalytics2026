contact_info = {
   "name": "Sonia Tana",
   "address": "2241 flaxmere rd",
   "city": "Charlotte",
    "state": "NC",
    "zip": "28262"
  }

print(f"""{contact_info['name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}""")

contact_info.pop("name")

full_name = {
    "first name": "Sonia",
    "last name": "Tana"
}

full_name.update({"honorific": "Ms."})

contact_info.update({"full_name": full_name})

print(f"""{full_name['honorific']} {full_name['first name']} {full_name['last name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}""")

