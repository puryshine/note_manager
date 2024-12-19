from datetime import date
def date_changer(_):
    return(_.day, _.month)            # предоставление даты в формате: "день месяц"

created_date = date.today()
print(date_changer(created_date))