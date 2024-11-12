from sqlalchemy.orm import Session
from . import models, schemas
from .security import hash_password



def create_employee(db: Session, employee: schemas.EmployeeCreate):
    
    db_employee = models.Employee(
        name=employee.name,
        age=employee.age,
        department=employee.department,
        position=employee.position,
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def get_employees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Employee).offset(skip).limit(limit).all()

def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeCreate):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if db_employee:
        db_employee.name = employee.name
        db_employee.age = employee.age
        db_employee.department = employee.department
        db_employee.position = employee.position
        db.commit()
        db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)  
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()