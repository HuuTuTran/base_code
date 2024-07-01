from fastapi import FastAPI , Depends , Response , status , Query
from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import sessionmaker
import json
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from connection import SessionLocal, Base, engine
import redis_connect as rc
import time
from starlette.requests import Request
from fastapi.background import BackgroundTasks
from fastapi import FastAPI, Depends
from jwt_configuration import create_access_token, get_current_user
# uvicorn products_api:app --reload

#You could use pydantic with Basemodel  or sqlalchemy with sqlalchemy




class Mini(Base):
	__tablename__ = "mfs_tbl"
	id = Column(Integer, primary_key=True, index=True  )
	name = Column(String(50), nullable=False, unique=True)
	SKU = Column(String(100), nullable=False, unique=True)
	cates = Column(String(100), nullable=False, unique=True)
	tag = Column(String(100), nullable=False, unique=True)
	price = Column(String(100), nullable=False, unique=True)
	img_url = Column(String(100), nullable=False, unique=True)
	status = Column(String(100), nullable=False, unique=True)


# class Mini(Base):
# 	__tablename__ = "mf_tbl"
# 	__allow_unmapped__ = True
# 	id: int
# 	name: str
# 	SKU: str
# 	cates: str
# 	tag: str
# 	price: str
# 	img_url: str


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



app = FastAPI()
Base.metadata.create_all(bind=engine)
async def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


@app.post("/token")
async def login(request: Request):
    # Verify the username and password
    # If valid, create an access token
	body = await request.json()
	username = body.get("username")
	password = body.get("password")
	if username =="sa" and password =="1234567":
		access_token = create_access_token(data={"sub": username}  )
		return {"access_token": access_token, "token_type": "bearer"}
	else:
		return "Invalid information"



@app.get("/products")
def index(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100), db: Session = Depends(get_db) , user: dict = Depends(get_current_user)):
	Minis = db.query(Mini).offset(skip).limit(limit).all()
	return {"minis": Minis}




@app.get("/products/{id}")
def get(id:int ,  response: Response, is_vsisble = True ,db: Session = Depends(get_db)):
	cache_key = f'product_{id}'
	redis_rsl = rc.r.get(cache_key)
	if redis_rsl and is_vsisble :
		print("get dâta from cache")
		obj= json.loads(redis_rsl)
	else:
		# time.sleep(5)
		obj = db.query(Mini).filter(Mini.id == id).first()
		if obj:
			obj_dict= {k: v for k, v in obj.__dict__.items() if k != '_sa_instance_state'}
			rc.r.set(cache_key, json.dumps(obj_dict) ,ex=20)
		else:
			obj = "Not found"
			response.status_code = status.HTTP_404_NOT_FOUND			
	return obj

@app.get("users")
def complicated_query():
	sum = 0
	for i in range(10**6):
		sum = sum + i
	return "HEloo world"

@app.post("/products")
async def post_product(request: Request , backgroup_task: BackgroundTasks ,db: Session = Depends(get_db) ):
	try:
		body = await request.json()
		user_agent = request.headers.get("x-api-key")
		print(f"x-api-key: {user_agent}")	
		new_mini = Mini()
		new_mini.name = body.get("name")
		new_mini.cates = body.get("cates")
		new_mini.img_url = body.get("img_url")
		new_mini.SKU = body.get("SKU")
		new_mini.tag = body.get("tag")
		new_mini.price = body.get("price")
		new_mini.status = 'pending'
		db.add(new_mini)
		db.commit()
		db.refresh(new_mini)	
		# print(db)
		backgroup_task.add_task(confirm_product,new_mini.id,db)
		return new_mini		
	except Exception as e :
		return e
	
def confirm_product(id: int, db: Session):
	obj = db.query(Mini).filter(Mini.id == id).first()
	obj.status = 'confirmed'
	db.commit()
	return "product updated"



@app.delete("/products/{id}")
def delete(id:int ,  response: Response ,db: Session = Depends(get_db)):
	obj = get(id,response,False,db)
	if obj != 'Not found':
		db.delete(obj)
		db.commit()

		response.status_code = status.HTTP_200_OK
		return "Completed"

	response.status_code = status.HTTP_404_NOT_FOUND
	return "Not FOUND"