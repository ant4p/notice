# Преобразование номера для использования.
def cleaned_phone_number(phone_number):
    if phone_number:
        phone_number = list(phone_number)
        phone_number = [item.replace("+", "") for item in phone_number]
        phone_number = [item.replace("(", "") for item in phone_number]
        phone_number = [item.replace(")", "") for item in phone_number]
        phone_number = [item.replace("-", "") for item in phone_number]
        phone_number = [item.replace("*", "") for item in phone_number]
        phone_number = [item.replace(" ", "") for item in phone_number]
        phone_number = list(filter(lambda item: item != "", phone_number))

        if phone_number[0] == "8":
            phone_number[0] = "7"
        clean_phone_number = int("".join(phone_number))

        return clean_phone_number


# Преобразование id Telegram для использования.
def cleaned_id_telegram(id_number):
    if id_number:
        id_number = list(id_number)
        id_number = [item.replace(" ", "") for item in id_number]
        id_number = list(filter(lambda item: item != "", id_number))
        clean_id_number = "".join(id_number)
        return clean_id_number


#  Преобразование текста уведомления для использования.
def cleaned_text(text):
    if text:
        return text.encode("utf-8")
    else:
        return ""
