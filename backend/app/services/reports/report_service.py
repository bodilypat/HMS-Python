#app/services/reports/report_service.py

from datetime import date 
from fastapi import HTTPException 
from app.schemas.reports import ReportRequest, ReportResponse 
from app.crud.reports.report_crud import ReportCRUD 

class ReportService:
    def __init__(self):
        self.report_crud = ReportCRUD()

#------------------------------
# GENERATE REPORT
#------------------------------
    async def generate_report(self, data: ReportRequest) -> ReportResponse:
        if data.start_date >= data.end_date:
            raise HTTPException(status_code=400, detail="Start date must be before end date")
        report = await self.report_crud.generate(
            start_date=data.start_date,
            end_date=data.end_date,
            report_type=data.report_type
        )

        return reportResponse(
            report_name=data.report_type,
            generated_on=date.today(),
            data=report_data 
        )
#--------------------------
# OCCUPANCY REPORT 
#--------------------------
    async def generate_occupancy_report(self, start_date:date, end_date:date) -> ReportResponse:
        if start_date >= end_date:
            raise HTTPException(status_code=400, detail="Start date must be before end date")
        return await self.generate_report(ReportRequest(start_date=start_date, end_date=end_date, report_type="occupancy"))
    
#--------------------------
# REVENUE REPORT
#--------------------------
    async def generate_revenue_report(self, start_date:date, end_date:date) -> ReportResponse:
        if start_date >= end_date:
            raise HTTPException(status_code=400, detail="Start date must be before end date")
        return await self.generate_report(ReportRequest(start_date=start_date, end_date=end_date, report_type="revenue"))
