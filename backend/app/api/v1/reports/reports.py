#app/api/v1/reports/reports.py

from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date 
from decimal import Decimal
from  typing import List 

from app.models.billing import Billing
from app.models.booking import Booking
from app.models.room import Room
from app.models.hotel_service import HotelServiceUsage 
from app.models.hotel_service import HotelService
from app.schemas.reports.reports import RevenueReportResponse, OccupancyReportResponse, ServiceUsageReportResponse

#-------------------------
# Revenue Report
#-------------------------
def get_revenue_report(
        db: Session,
        start_date: date,
        end_date: date
) -> RevenueReportResponse:
    room_revenue = db.query(
        func.coalesce(func.sum(Billing.amount), 0)
    ).join(Booking, Billing.booking_id == Booking.id
    ).filter(
        Booking.check_in_date >= start_date,
        Booking.check_out_date <= end_date
    ).scalar()

    service_revenue = db.query(
        func.coalesce(func.sum(HotelServiceUsage.total_price), 0)
    ).filter(
        HotelServiceUsage.usage_date >= start_date,
        HotelServiceUsage.usage_date <= end_date
    ).scalar()

    total_revenue = Decimal(room_revenue) + Decimal(service_revenue)

    return RevenueReportResponse(
        room_revenue=Decimal(room_revenue),
        service_revenue=Decimal(service_revenue),
        total_revenue=total_revenue
    )

#-------------------------
# Occupancy Report
#-------------------------
def get_occupancy_report(
        db: Session,
        start_date: date,
        end_date: date
) -> OccupancyReportResponse:
    total_rooms = db.query(func.count(Room.id)).scalar()

    occupied_rooms_subquery = db.query(
        Booking.room_id
    ).filter(
        Booking.check_in_date < end_date,
        Booking.check_out_date > start_date
    ).distinct().subquery()

    occupied_rooms_count = db.query(func.count(occupied_rooms_subquery.c.room_id)).scalar()

    occupancy_rate = (occupied_rooms_count / total_rooms * 100) if total_rooms > 0 else 0.0

    return OccupancyReportResponse(
        total_rooms=total_rooms,
        occupied_rooms=occupied_rooms_count,
        occupancy_rate=occupancy_rate
    )

#-------------------------
# Service Usage Report
#-------------------------
def get_service_usage_report(
        db: Session,
        start_date: date,
        end_date: date
) -> List[ServiceUsageReportResponse]:
    service_usages = db.query(
        HotelService.name,
        func.coalesce(func.sum(HotelServiceUsage.quantity), 0).label('total_quantity'),
        func.coalesce(func.sum(HotelServiceUsage.total_price), 0).label('total_revenue')
    ).join(
        HotelService, HotelServiceUsage.service_id == HotelService.id
    ).filter(
        HotelServiceUsage.usage_date >= start_date,
        HotelServiceUsage.usage_date <= end_date
    ).group_by(
        HotelService.name
    ).all()

    report = [
        ServiceUsageReportResponse(
            service_name=service_name,
            total_quantity=total_quantity,
            total_revenue=Decimal(total_revenue)
        )
        for service_name, total_quantity, total_revenue in service_usages
    ]

    return report

