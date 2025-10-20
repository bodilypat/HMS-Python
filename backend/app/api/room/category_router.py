#app/api/room/category_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query , Response
from sqlalchemey.orm import Session 
from typing import List

from app.schemas.room.category_router import CategoryCreate, CategoryUpdate, CreateRead 
from app.models.room import category_service as CategoryService
from app.db.session import get_db 

router = APIRouter(prefix="/categories", tags=["Categories Management"])

@router.get("/", response_model=List[CategoryRead], summary="Get a list categories")
def list_categories(
        skip: int = Query(0, ge=0, description="Number of record to skip"),
        limit: int = Query(10, le=100, description="Maximum number of records to return"),
        db: Session = Depends(get_db)
    ):
    return CategoryService(db).get_all_categories(skip=skip, limit=limit)

@router.get("{category_id}", response_model=CategoryRead, summary="Get a single by ID")
def read_category(
        category_id: int,
        db: Session = Depends(get_db)
    ):
    """
        Retrieve a category by their unique ID.
    """
    category = CategoryService(db).get_category_by_id(category_id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category 

@router.post("/", response_model=CategoryRead, status_code=status.HTTP_201_CREATED, summary="Create a new category")
def create_category(
        category_data: CategoryCreate,
        db: Session = Depends(get_db)
    ):
    return CategoryCreate(db).create_category(category_data)

@router.put("/{category_id}", response_model=CategoryRead, summary="Update a category")
def update_category(
        category_id: int,
        updated_category: CategoryUpdate,
        db: Session = Depends(get_db)
    ):
    """
        Update an existing category's data.
    """
    updated = CategoryService(db).update_category(category_id, updated_category)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return updated 

@router.delete("/{category}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete a category")
def delete_category(
        category_id: int,
        db: Session = Depends(get_db)
    ):
    """
        Delete a category by their ID.
    """
    deleted = CategoryService(db).delete_category(category_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
