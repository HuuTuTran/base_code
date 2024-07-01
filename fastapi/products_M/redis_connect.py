import redis

# Connect to the Redis server running in a Docker container
r = redis.Redis(
  host='redis-12132.c1.asia-northeast1-1.gce.redns.redis-cloud.com',
  port=12132,
  password='gDkNtTTJyigVpg0lgF9NCY15I2tDUJTW')

# Ping the Redis server to test the connection
try:
    response = r.ping()
    print(f"Connected to Redis server: {response}")
    

    
except redis.exceptions.ConnectionError as e:
    print(f"Failed to connect to Redis server: {e}")