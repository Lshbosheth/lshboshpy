from fastapi import APIRouter
from typing import List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database import models, schemas, crud
from database.db import SessionLocal, engine

router = APIRouter(
    prefix="/dbtest",
    tags=["dbtest"],
    responses={404: {"description": "Not found"}},
)
models.db.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 根据email查找用户
    db_user = crud.get_user_by_email(db, email=user.email)
    # 如果用户存在，提示该邮箱已经被注册
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    # 返回创建的user对象
    print(user)
    print(db)
    return crud.create_user(db=db, user=user)


@router.get("/users", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # 读取指定数量用户
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    # 获取当前id的用户信息
    db_user = crud.get_user(db, user_id=user_id)
    # 如果没有信息，提示用户不存在
    if db_user is None:
        raise HTTPException(status_code=200, users=["User not found"])
    return db_user


@router.post("/users/{user_id}/items", response_model=schemas.Item)
def create_item_for_user(
        user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    # 创建该用户的items
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # 获取所有items
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
