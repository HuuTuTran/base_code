from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

# Set up the OAuth2 bearer scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Secret key and algorithm for signing the JWT
SECRET_KEY = "12345678"
ALGORITHM = "HS256"

# Function to create a JWT token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
	to_encode = data.copy()
	if expires_delta:
		expire = datetime.utcnow() + expires_delta
	else:
		expire = datetime.utcnow() + timedelta(minutes=15)
	to_encode.update({"exp": expire})
	to_encode.update({'iss':"JayEnterprise"})
	encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
	print(encoded_jwt)

	return encoded_jwt

# Function to verify the JWT token
def get_current_user(token: str = Depends(oauth2_scheme)):
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		print(payload)
		username: str = payload.get("sub")
		if username is None:
			raise HTTPException(
				status_code=status.HTTP_401_UNAUTHORIZED,
				detail="Invalid authentication credentials",
				headers={"WWW-Authenticate": "Bearer"},
			)
		# You can add additional logic here to load the user from the database
		return {"username": username}
	except JWTError:
		print("wrong token")
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Invalid authentication credentialsssss",
			headers={"WWW-Authenticate": "Bearer"},
		) 	
def load_user(username: str):
	# Replace this with your actual user loading logic
	return {"username": username}    