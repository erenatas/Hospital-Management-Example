from app.model.report.doctorreportmodelstrategy import DoctorReportModelStrategy
from app.model.report.patientreportmodelstrategy import PatientReportModelStrategy

doctor_report = DoctorReportModelStrategy()
patient_report = PatientReportModelStrategy()


class ReportModel(object):
    def __init__(self, report_strategy):
        self._report_strategy = report_strategy

    def get_reports(self, user_id, user_type):
        self._report_strategy.get_reports(user_id, user_type)

    def set_report(self):
        self._report_strategy.set_reports()


class DoctorReportModel(ReportModel):
    def __init__(self):
        super(DoctorReportModel, self).__init__(doctor_report)


class PatientReportModel(ReportModel):
    def __init__(self):
        super(PatientReportModel, self).__init__(patient_report)
