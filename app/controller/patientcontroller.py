from flask import Blueprint, request
from app.components.user import requires_roles
from app.common.loginmanager import session
from app.model.report.reportmodel import PatientReportModel
from app.model.appointment.appointmentmodel import PatientAppointmentModel

patient_controller = Blueprint('patient', __name__)
report_model = PatientReportModel()
appointment_model = PatientAppointmentModel()

'''
requires_roles decorator has been used in these methods for Role based access/authorization.
'''


'''
This controller method gets the appointments that the Patient has. 
'''


@patient_controller.route('/get_appointments')
@requires_roles('Patient')
def get_appointment():
    user_id = session.get('user_id')
    return appointment_model.get_appointments(user_id, 'Patient')


'''
This controller gets the report that Doctor has given to that patient.s
'''


@patient_controller.route('/get_report')
@requires_roles('Patient')
def get_report():
    user_id = session.get('user_id')
    return report_model.get_reports(user_id, 'Patient')
