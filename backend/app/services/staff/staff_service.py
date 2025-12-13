#app/services/staff/staff_service.py

from fastapi import HTTPException 
from app.schemas.staff import StaffCreate, StaffUpdate, StaffResponse 
from app.crud.staff.staff_crud import StaffCRUD 

class StaffService:
    def __init__(self):
        self.crud = StaffCRUD()


#-----------------------------
# GET ALL STAFF 
#-----------------------------
    async def get_all(self, page: int, page_size: int, role: str = None,search: str = None) -> list[StaffResponse]:
        staff_members = await self.crud.get_all_staff(page, page_size, role, search)
        return [StaffResponse.from_orm(staff) for staff in staff_members]
    
#-----------------------------
# GET STAFF BY ID
#-----------------------------
    async def get_by_id(self, staff_id: int) -> StaffResponse:
        staff = await self.crud.get_staff_by_id(staff_id)
        if not staff:
            raise HTTPException(status_code=404, detail="Staff not found")
        return StaffResponse.from_orm(staff)
    
#-----------------------------
# CREATE STAFF
#-----------------------------
    async def create(self, staff_create: StaffCreate) -> StaffResponse:
        staff = await self.crud.create_staff(staff_create)
        return StaffResponse.from_orm(staff)
    
#-----------------------------
# UPDATE STAFF
#-----------------------------
    async def update(self, staff_id: int, staff_update: StaffUpdate) -> StaffResponse:
        staff = await self.crud.update_staff(staff_id, staff_update)
        if not staff:
            raise HTTPException(status_code=404, detail="Staff not found")
        return StaffResponse.from_orm(staff)
    
#-----------------------------
# DELETE STAFF
#-----------------------------
    async def delete(self, staff_id: int) -> None:
        deleted = await self.crud.delete_staff(staff_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Staff not found")
        return None
    
    