import csv
import re


def serialization(file, encoding):
    with open(file, encoding=encoding) as f:
        rows = csv.DictReader(f, delimiter=",")
        return list(rows)


def get_correct_fio(contact_data):
    lastname = contact_data["lastname"]
    firstname = contact_data["firstname"]
    surname = contact_data["surname"]
    full_name_list = " ".join([lastname, firstname, surname]).strip().split(' ')
    contact_data["lastname"] = full_name_list[0]
    contact_data["firstname"] = full_name_list[1]
    if len(full_name_list) == 3:
        contact_data["surname"] = full_name_list[2]
    return contact_data


def get_correct_phone(contact_data):
    phone = contact_data['phone']
    if len(phone) > 0:
        all_phone_num = re.findall('[0-9]', phone)
        phone_num_1 = ''.join(all_phone_num)[1:4]
        phone_num_2 = ''.join(all_phone_num)[4:7]
        phone_num_3 = ''.join(all_phone_num)[7:9]
        phone_num_4 = ''.join(all_phone_num)[9:11]
        phone = f"+7({phone_num_1}){phone_num_2}-{phone_num_3}-{phone_num_4}"
        if len(all_phone_num) > 11:
            phone_additional_part = ''.join(all_phone_num)[11:15]
            phone += f" доп.{phone_additional_part}."
        contact_data["phone"] = phone
    return contact_data


def get_united_contact(contact1, contact2):
    united_contact = {}

    united_contact['surname'] = contact1['surname'] if len(contact1['surname']) > 0 else contact2['surname']
    united_contact['organization'] = contact1['organization'] if len(contact1['organization']) > 0 \
        else contact2['organization']
    united_contact['position'] = contact1['position'] if len(contact1['position']) > 0 else contact2['position']
    united_contact['phone'] = contact1['phone'] if len(contact1['phone']) > 0 else contact2['phone']
    united_contact['email'] = contact1['email'] if len(contact1['email']) > 0 else contact2['email']

    return united_contact


def deserialization(file, mode, encoding, result):
    with open(file, mode, encoding=encoding) as f:
        dict_writer = csv.DictWriter(f, fieldnames=list(result[0].keys()), lineterminator='\n')
        dict_writer.writeheader()
        for contact in result:
            dict_writer.writerow(contact)
