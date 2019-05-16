from app.model.report.doctorreportmodelstrategy import DoctorReportModelStrategy
from app.model.report.patientreportmodelstrategy import PatientReportModelStrategy

doctor_report = DoctorReportModelStrategy()
patient_report = PatientReportModelStrategy()


'''
Report model is for database operations related to reports. There are two functions, get_reports and 
send_report. Strategy pattern has been used here for decoupling the client class from the class that is actually 
implementing the details of the algorithm. The main goal of this pattern is to enable a client class to choose between 
different algorithms or procedures to complete the same task. This way, different algorithms can be swapped in and out 
without complicating things. 

If the user type is Doctor, DoctorReport is being used, if it is Patient, then the PatientReport model is 
being used.

Patient can only get reports. Meanwhile, Doctor can both get and send report(s).

    get_reports: gets user_id and user_type. returns the reports that the user has. 
    send_report: Used for sending a report. Gets user_id, patient_id and date.
'''


class ReportModel(object):
    def __init__(self, report_strategy):
        self._report_strategy = report_strategy

    def get_reports(self, user_id, user_type):
        return self._report_strategy.get_reports(user_id, user_type)

    def send_report(self, user_id, patient_id, report, date):
        return self._report_strategy.send_report(user_id, patient_id, report, date)


class DoctorReportModel(ReportModel):
    def __init__(self):
        super(DoctorReportModel, self).__init__(doctor_report)


class PatientReportModel(ReportModel):
    def __init__(self):
        super(PatientReportModel, self).__init__(patient_report)
