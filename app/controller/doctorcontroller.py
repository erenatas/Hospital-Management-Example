from flask import Blueprint, request
from app.components.user import requires_roles
from app.common.loginmanager import session
from app.model.appointmentmodel import get_appointments, set_appointments
from app.model.report.reportmodel import DoctorReportModel, PatientReportModel

doctor_controller = Blueprint('doctor', __name__)
report_model = DoctorReportModel()


@requires_roles('Doctor')
@doctor_controller.route('/get_appointments')
def get_appointment():
    user_id = session.get('user_id')
    return get_appointments(user_id, 'Doctor')


@requires_roles('Doctor')
@doctor_controller.route('/set_appointment', methods=['POST'])
def set_appointment():
    user_id = session.get('user_id')
    patient_id = request.form.get('patient_id')
    date = request.form.get('date')
    return set_appointments(user_id, patient_id, date)


@requires_roles('Doctor')
@doctor_controller.route('/send_report', methods=['POST'])
def send_report():
    user_id = session.get('user_id')
    patient_id = request.form.get('patient_id')
    report = request.form.get('report')
    date = request.form.get('date')
    return report_model.send_report(user_id, patient_id, report, date)


@requires_roles('Doctor')
@doctor_controller.route('/get_report')
def get_report():
    user_id = session.get('user_id')
    return report_model.get_reports(user_id, 'Doctor')
