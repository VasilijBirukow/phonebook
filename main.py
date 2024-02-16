from additionally import serialization
from additionally import get_correct_fio
from additionally import get_correct_fio
from additionally import get_united_contact
from additionally import deserialization
from additionally import get_correct_phone


contacts_dict_list = serialization("phonebook_raw.csv", "utf-8")

double_check_dict = {}
result_dict_list = []
for contact in contacts_dict_list:
    contact = get_correct_fio(contact)
    contact = get_correct_phone(contact)

    FI = f'{contact["lastname"]} {contact["firstname"]}'
    if FI not in double_check_dict:
        result_dict_list.append(contact)
        double_check_dict[FI] = contacts_dict_list.index(contact)
    else:
        get_united_contact(contact, contacts_dict_list[double_check_dict[FI]])


deserialization("phonebook.csv", "w", "utf-8", result_dict_list)


