from flask import Flask
from flask_restful import Resource, Api, reqparse
import json 

### Setup ###

app = Flask(__name__)
api = Api(app)

class Doctor:
    def __init__(self, first_name, last_name, uid):
        self.first_name = first_name
        self.last_name = last_name
        self.uid = uid
    
    def __str__(self):
        return f'Dr. {self.first_name} {self.last_name} - {self.uid}'

class Appointment:
    def __init__(self, patient_first, patient_last, date, time, kind, uid, doctor):
        self.patient_first = patient_first
        self.patient_last = patient_last
        self.date = date 
        self.time = time
        self.kind = kind
        self.uid = uid 
        self.doctor = doctor
    
    def __str__(self):
        return f'{self.kind} Appointment ({self.uid}) for {self.patient_first} {self.patient_last} on {self.date} at {self.time}'

doc1 = Doctor("Nadya", "Kominick", 1)
doc2 = Doctor("Cyril", "Kominick", 2)
appointment1 = Appointment("Brian", "K", "07/24/2022", "8:15", "New Patient", 101, doc1)
appointment2 = Appointment("Brian", "K", "07/28/2022", "8:15", "Follow Up", 102, doc1)

docs = [doc1, doc2]
apps = [appointment1, appointment2]

### Endpoint definitions ###

class Home(Resource):
    def get(self):
        return {"Data" : "Hello Notable"}
    pass


class Appointments(Resource):
    """Endpoint for appointment collection"""
    def get(self):
        """parser = reqparse.RequestParser()
        parser.add_argument('doc_id')
        args = parser.parse_args()
        
        appointments = []
        if args['doc_id']:
            for i in apps:
                if i.doctor.uid == args['doc_id']:
                    appointments.append(str(i))
        else:
            appointments = [str(i) for i in apps]
        """
        appointments = [str(i) for i in apps]
        return appointments


        pass
    def post(self):
        pass 
    def delete(self):
        pass

class Doctors(Resource):
    def get(self):
        return [str(doc) for doc in docs]
    pass

### Endpoint routing  ###

api.add_resource(Home, '/')
api.add_resource(Appointments, '/appointments')
api.add_resource(Doctors, '/doctors')



if __name__ == '__main__':
    app.run(debug=True)