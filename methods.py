from .models import Contact
import json
import os
import pandas as pd


CONTACTS_FILE = f"{os.getcwd()}/storage/contacts.json"


def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return [Contact.from_dict(contact) for contact in json.load(file)]
    except:
        return []


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump([contact.to_dict() for contact in contacts], file, indent=4)


def create_contact():
    contacts = load_contacts()
    contact_id = len(contacts) + 1
    name = input("Введите имя контакта: ")
    phone = input("Введите номер телефона: ")
    email = input("Введите адрес электронной почты: ")
    contact = Contact(contact_id, name, phone, email)
    contacts.append(contact)
    save_contacts(contacts)
    print("Контакт успешно создан.")


def list_contacts():
    contacts = load_contacts()
    if not contacts:
        print("Список контактов пуст.")
        return
    for contact in contacts:
        print(f"{contact.id}. {contact.name} - {contact.phone} - {contact.email}")


def export_contacts_to_csv():
    contacts = load_contacts()
    df = pd.DataFrame([contact.to_dict() for contact in contacts])
    df.to_csv(f"{os.getcwd()}/storage/contacts.csv", index=False)
    print("Контакты успешно экспортированы в CSV.")


def import_contacts_from_csv():
    df = pd.read_csv(f"{os.getcwd()}/storage/contacts.csv")
    contacts = [Contact.from_dict(row) for index, row in df.iterrows()]
    save_contacts(contacts)
    print("Контакты успешно импортированы из CSV.")
