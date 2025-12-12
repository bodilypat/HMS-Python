#app/schemas/reports.py

from pydantic import BaseModel 
from typing import Optional 
from datetime import date

class ReporResponse(BaseModel):
    start_date: date 
    end_date: date 
    report_type: str 

class reportResponse(BaseModel):
    report_name: str 
    generated_on: date 
    data: dict 

    