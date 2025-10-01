#app/controllers/room/category_router.py

from fastapi import APIRouter, Depends, HTTPException, query, status, Reponse 
from sqlalchemy.orm import Session
from dependancies import get_db 

from schemas.core.category import CategoryCreate, CategoryRead, CategoryUpdate,
from services.room.category import CategoryService 
from typing import List 

router = APIRouter(prefix="/rooms", tags="Rooms Management")

@router.get("/", response_model=List[CategoryRead], summary="Get a list of Category")
def read_categories(
        skip: int = query(0, ge=0),
        limit: int = query(10, le=100),
        db: Session = Depends(get_db)
    ):
    return CategoryService(db).get_all_categories(skip, limit)

@router.get("/{category_id}", response_model=CategoryRead, summary="Get a single Category by ID")
def read_category(
        category_id: int,
        db: Session = Depends(get_db)
    ):
    category = CategoryService(db).get_category_by_id(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category 

@router.post("/", response_model=CategoryRead, status_code=status.HTTP_201_CREATED, summary="Create new Category")
def create_category(
        category_in: CategoryCreate,
        db: Session = Depends(get_db)
    ):
    category = CategoryService(db).create_category(category_in)
    if not new_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/{category_id}", response_model=CategoryRead, summry="Update an existing Category")
def update_category(
        category_id: int,
        updated_category: CategoryUpdate,
        db: Session = Depends(get_db)       
    ):
    updated = CategoryService(db).update_category(category_id, updated_category)
    if not updated:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete category")
def delete_category(
        category_id: int,
        db: Session = Depends(get_db)
    ):
    success = CategoryService(db).delete_category(category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Category not foud")
    return Response(status_code=status.HTTP_NO_CONTENT)


