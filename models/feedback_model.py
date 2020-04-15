from flask import jsonify



class Feedback:
    def __init__(self,customer_Name,feedback_information,feedback_date,feedback_Type):
        self.customer_Name = customer_Name
        self.feedback_information = feedback_information
        self.feedback_date = feedback_date
        self.feedback_Type = feedback_Type

    def to_json(self):
        return jsonify({
            "Customer_Name":self.customer_Name,
            "Feedback_information":self.feedback_information,
            "Feedback_date":self.feedback_date,
            "Feedback_Type":self.feedback_Type
        })

