from .models import FinanceRecord
import json
import os
import pandas as pd


FINANCE_FILE = f"{os.getcwd()}/storage/finance.json"


def load_finance_records():
    try:
        with open(FINANCE_FILE, "r") as file:
            return [FinanceRecord.from_dict(record) for record in json.load(file)]
    except:
        return []


def save_finance_records(records):
    with open(FINANCE_FILE, "w") as file:
        json.dump([record.to_dict() for record in records], file, indent=4)


def create_finance_record():
    records = load_finance_records()
    record_id = len(records) + 1
    amount = float(input("Введите сумму операции: "))
    category = input("Введите категорию операции: ")
    date = input("Введите дату операции (ДД-ММ-ГГГГ): ")
    description = input("Введите описание операции: ")
    record = FinanceRecord(record_id, amount, category, date, description)
    records.append(record)
    save_finance_records(records)
    print("Финансовая запись успешно создана.")


def list_finance_records():
    records = load_finance_records()
    if not records:
        print("Список финансовых записей пуст.")
        return
    for record in records:
        print(
            f"{record.id}. {record.amount} - {record.category} - {record.date} - {record.description}"
        )


def export_finance_records_to_csv():
    records = load_finance_records()
    df = pd.DataFrame([record.to_dict() for record in records])
    df.to_csv(f"{os.getcwd()}/storage/finance.csv", index=False)
    print("Финансовые записи успешно экспортированы в CSV.")


def import_finance_records_from_csv():
    df = pd.read_csv(f"{os.getcwd()}/storage/finance.csv")
    records = [FinanceRecord.from_dict(row) for index, row in df.iterrows()]
    save_finance_records(records)
    print("Финансовые записи успешно импортированы из CSV.")
