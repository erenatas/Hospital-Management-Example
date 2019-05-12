from flask import Blueprint, request
from app.components.user import requires_roles
from app.common.loginmanager import session
from app.model.appointment.appointmentmodel import DoctorAppointmentModel
from app.model.report.reportmodel import DoctorReportModel

doctor_controller = Blueprint('doctor', __name__)
report_model = DoctorReportModel()
appointment_model = DoctorAppointmentModel()

'''
requires_roles decorator has been used in these methods for Role based access/authorization.
'''


'''
This controller method gets the appointments that the Doctor has. 
'''


@requires_roles('Doctor')
@doctor_controller.route('/get_appointments')
def get_appointment():
    user_id = session.get('user_id')
    return appointment_model.get_appointments(user_id, 'Doctor')


'''
This controller method sets appointment to a patient with a date.
'''


@requires_roles('Doctor')
@doctor_controller.route('/set_appointment', methods=['POST'])
def set_appointment():
    user_id = session.get('user_id')
    patient_id = request.form.get('patient_id')
    date = request.form.get('date')
    result = appointment_model.set_appointment(user_id, patient_id, date)
    return result


'''
This controller method sends a report to a patient with report and date.
'''


@requires_roles('Doctor')
@doctor_controller.route('/send_report', methods=['POST'])
def send_report():
    user_id = session.get('user_id')
    patient_id = request.form.get('patient_id')
    report = request.form.get('report')
    date = request.form.get('date')
    return report_model.send_report(user_id, patient_id, report, date)


'''
This controller method gets the reports with the user_id.
'''


@requires_roles('Doctor')
@doctor_controller.route('/get_report')
def get_report():
    user_id = session.get('user_id')
    return report_model.get_reports(user_id, 'Doctor')
