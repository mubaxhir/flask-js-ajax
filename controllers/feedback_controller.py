from models.feedback_model import Feedback
import csv
import datetime

sampledata=[
    {
        "customer_name":"abc",
        "feedback_information":"xyz",
        "feedback_date":datetime.datetime.now(),
        "feedback_type":True
    },
    {
        "customer_name":"asdbc",
        "feedback_information":"xfasasdyz",
        "feedback_date":datetime.datetime.now(),
        "feedback_type":True
    },
    {
        "customer_name":"aasdfadbc",
        "feedback_information":"xyfesfjksnfz",
        "feedback_date":datetime.datetime.now(),
        "feedback_type":True
    },
    {
        "customer_name":"absiuhri3h3c",
        "feedback_information":"xywihrwi3ajo8z",
        "feedback_date":datetime.datetime.now(),
        "feedback_type":True
    }
]



def initdata():
    with open('data.csv', 'w' , newline='') as f:
        for item in sampledata:
            obj = Feedback(
                customer_Name=item["customer_name"],
                feedback_information=item["feedback_information"],
                feedback_date=item["feedback_date"],
                feedback_Type=item["feedback_type"]
            )
            writer = csv.writer(f)
            writer.writerow([obj.customer_Name,obj.feedback_information,obj.feedback_date,obj.feedback_Type])

