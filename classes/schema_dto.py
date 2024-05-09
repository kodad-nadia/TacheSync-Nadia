from pydantic import BaseModel

# Pydantic model for tasks
class TaskBase(BaseModel):
    name: str
    description: str
    completed: bool

class Task(TaskBase):
    id: str

class TaskNoID(TaskBase):
    pass

# Vous pouvez ajouter d'autres modèles Pydantic pour d'autres entités liées, par exemple :
# Pydantic model for categories
class CategoryBase(BaseModel):
    name: str
    description: str

class Category(CategoryBase):
    id: str

class CategoryNoID(CategoryBase):
    pass
