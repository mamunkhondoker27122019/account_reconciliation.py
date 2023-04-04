def reconcile_accounts(bank_statement, accounting_records):
    # Сортировка записей по дате
    bank_statement.sort(key=lambda x: x.date)
    accounting_records.sort(key=lambda x: x.date)

    # Инициализация указателей на первую запись в каждом списке
    bank_index = 0
    accounting_index = 0

    # Списки для хранения несоответствий в записях
    missing_from_bank = []
    missing_from_accounting = []
    discrepancies = []

    # Проход по спискам и сравнение записей
    while bank_index < len(bank_statement) and accounting_index < len(accounting_records):
        bank_record = bank_statement[bank_index]
        accounting_record = accounting_records[accounting_index]

        if bank_record.amount == accounting_record.amount:
            # Записи совпадают
            bank_index += 1
            accounting_index += 1
        elif bank_record.amount < accounting_record.amount:
            # Запись отсутствует в банковской выписке
            missing_from_bank.append(accounting_record)
            accounting_index += 1
        else:
            # Запись отсутствует в бухгалтерских записях
            missing_from_accounting.append(bank_record)
            bank_index += 1

    # Обработка оставшихся записей
    while bank_index < len(bank_statement):
        missing_from_accounting.append(bank_statement[bank_index])
        bank_index += 1

    while accounting_index < len(accounting_records):
        missing_from_bank.append(accounting_records[accounting_index])
        accounting_index += 1

    # Формирование отчета
    report = "Account reconciliation report:\n\n"
    if missing_from_bank:
        report += "Records missing from bank statement:\n"
        for record in missing_from_bank:
            report += f"- {record}\n"
        report += "\n"

    if missing_from_accounting:
        report += "Records missing from accounting records:\n"
        for record in missing_from_accounting:
            report += f"- {record}\n"
        report += "\n"

    if discrepancies:
        report += "Discrepancies between bank statement and accounting records:\n"
        for discrepancy in discrepancies:
            report += f"- {discrepancy}\n"
        report += "\n"

    return report
