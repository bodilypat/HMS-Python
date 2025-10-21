#app/api/room/category_router.py 

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session 
from typing import List

from app.schemas.room.category_schema import CategoryCreate, CategoryUpdate, CategoryRead 
from app.services.room import category_service as CategoryService 

from app.db.session import get_db 

router = APIRouter(prefix="/categories", tags=["Categories"]) 

@router.get(
        "/",
        response_model=CategoryRead,
        summary="Get a list of Categories"
    )
def list_categories(
        skip: int = Query(0, ge=0, description="Number of records to skip"),
        limit: int = Query(10, le=100, description="Maximum number of records to return"),
        db: Session = Depends(get_db)
    ):
    return CategoryService(db).get_all_categories(skip=skip, limit=limit)

@router.get(
        "/{category_id}",
        response_model=CategoryRead,
        summary="Get a category by ID",
    )
def read_category(
        category_id: int,
        db: Session = Depends(get_db)
    ):
    category = CategoryService(db).get_category_by_id(category_id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category 

@router.post(
        "/",
        response_model=CategoryRead, 
        summary="Create a new Category"
    )
def create_category(
        category_data: CategoryCreate,
        db: Session = Depends(get_db)
    ):
    return CategoryService(db).create_category(category_data)

@router.put(
        "/{category_id}",
        response_model=CategoryRead,
        summary="Update a category"
    )
def update_category(
        category_id: int,
        updated_category: CategoryUpdate,
        db: Session = Depends(get_db)
    ):
    updated = CategoryService(db).update_category(category_id, updated_category)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detailt="Category not found")
    return  updated 

@router.delete(
        "/{category_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete a category"
    )
def delete_category(
        category_id: int,
        db: Session = Depends(get_db)
    ):
    deleted = CategoryService(db).delete_category(category_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

