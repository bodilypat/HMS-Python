#app/services/room/category_service.py

from sqlalchemy.orm import Session 
from typing import List, Optional 

from models.room.category import Category
from schemas.room.category import CategoryCreate, CategoryUpdate 

class CategoryService: 
    def __init__(self, db: Session):
        self.db = db 

    def get_all_categories(self, skip: int = 0, limit: int =10) -> List[Category]:
        """ Retrieve all room categories (paginated)."""
        return self.db.query(Category).offset(skip).limit(limit).all()
    
    def get_category_by_id(self, category_id: int) -> Optional[Category]:
        """ Retrieve a single category by ID."""
        return self.db.query(Category).filter(Category.id == category_id).first()
    
    def create_category(self, category_data: CategoryCreate) -> Category:
        """ Create a new category."""
        category = Category(**category_data.dict())
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category 
    
    def update_category(self, category_data: CategoryUpdate) ->Optional[Category]:
        """ Update an existing category."""
        category= self.db.query(Category).filter(Category.id == category_id).first()
        if not category:
            return None
        
        for key, value in category_data.dict(exclude_unset=True).items()
            setattr(category, key, value)

        self.db.commint()
        self.db.refresh(category)
        return category
    
    def delete_category(self, category_id: int) -> bool:
        """ Delete a category by ID."""
        category = self.db.query(Category).filter(Category.id == category_id).first()
        if not category:
            return False 
        
        self.db.delete(category)
        self.db.commit()
        return True