from . import notes_methods as notes
from . import task_methods as tasks
from . import contact_methods as contacts
from . import finance_methods as finance
from . import calculator as calc

import sys


class Manager:
    def main_menu(self):
        print("Добро пожаловать в Персональный помощник!")
        print("Выберите действие:")
        print("1. Управление заметками")
        print("2. Управление задачами")
        print("3. Управление контактами")
        print("4. Управление финансовыми записями")
        print("5. Калькулятор")
        print("6. Выход")

        choice = input("Введите номер действия: ")
        if choice == "1":
            self.manage_notes()
        elif choice == "2":
            self.manage_tasks()
        elif choice == "3":
            self.manage_contacts()
        elif choice == "4":
            self.manage_finances()
        elif choice == "5":
            self.calculator()
        elif choice == "6":
            sys.exit()
            exit()
        else:
            print("Некорректный ввод. Попробуйте снова.")
            self.main_menu()

    def manage_notes(self):
        print("Управление заметками")
        print("1. Создать заметку")
        print("2. Просмотреть заметки")
        print("3. Экспорт заметок в CSV")
        print("4. Импорт заметок из CSV")
        print("5. Назад")
        choice = input("Выберите действие: ")
        if choice == "1":
            notes.create_note()
        elif choice == "2":
            notes.list_notes()
        elif choice == "3":
            notes.export_notes_to_csv()
        elif choice == "4":
            notes.import_notes_from_csv()
        elif choice == "5":
            self.main_menu()
        else:
            print("Некорректный ввод. Попробуйте снова.")
            self.manage_notes()

    def manage_tasks(self):
        print("Управление задачами")
        print("1. Создать задачу")
        print("2. Просмотреть задачи")
        print("3. Экспорт задач в CSV")
        print("4. Импорт задач из CSV")
        print("5. Назад")
        choice = input("Выберите действие: ")
        if choice == "1":
            tasks.create_task()
        elif choice == "2":
            tasks.list_tasks()
        elif choice == "3":
            tasks.export_tasks_to_csv()
        elif choice == "4":
            tasks.import_tasks_from_csv()
        elif choice == "5":
            self.main_menu()
        else:
            print("Некорректный ввод. Попробуйте снова.")
            self.manage_tasks()

    def manage_contacts(self):
        print("Управление контактами")
        print("1. Создать контакт")
        print("2. Просмотреть контакты")
        print("3. Экспорт контактов в CSV")
        print("4. Импорт контактов из CSV")
        print("5. Назад")
        choice = input("Выберите действие: ")
        if choice == "1":
            contacts.create_contact()
        elif choice == "2":
            contacts.list_contacts()
        elif choice == "3":
            contacts.export_contacts_to_csv()
        elif choice == "4":
            contacts.import_contacts_from_csv()
        elif choice == "5":
            self.main_menu()
        else:
            print("Некорректный ввод. Попробуйте снова.")
            self.manage_contacts()

    def manage_finances(self):
        print("Управление финансовыми записями")
        print("1. Создать финансовую запись")
        print("2. Просмотреть финансовые записи")
        print("3. Экспорт финансовых записей в CSV")
        print("4. Импорт финансовых записей из CSV")
        print("5. Назад")
        choice = input("Выберите действие: ")
        if choice == "1":
            finance.create_finance_record()
        elif choice == "2":
            finance.list_finance_records()
        elif choice == "3":
            finance.export_finance_records_to_csv()
        elif choice == "4":
            finance.import_finance_records_from_csv()
        elif choice == "5":
            self.main_menu()
        else:
            print("Некорректный ввод. Попробуйте снова.")
            self.manage_finances()

    def calculator(self):
        calc.calculator()
        self.main_menu()
