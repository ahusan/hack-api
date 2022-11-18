# If you want to try FastAPI book repository

 - This project was tested with python 3.9.12 and 3.10.7

### 1. To create DB on docker with docker compose
`docker compose up -d`
- Alternatively you can add all the services under docker with these

```yml
    version: "3"

    services:

    #Postgres DB service
    db:
        image: postgres:11
        ports:
        - "5432:5432"
        environment:
        - POSTGRES_USER=postgres
        - POSTGRES_PASSWORD=postgres
        - POSTGRES_DB=test_db

    
    #running app on docker
    web:
        build: .
        command: bash -c "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000 --reload"
        volumes:
        - .:/code
        ports:
        - "8000:8000"
        depends_on:
        - db
    
    #If you want a webUI to view db
    pgadmin:
        container_name: pgadmin
        image: dpage/pgadmin4
        environment:
        - PGADMIN_DEFAULT_EMAIL=pgadmin4@pgadmin.org
        - PGADMIN_DEFAULT_PASSWORD=admin
        ports:
        - "5050:80"
        depends_on:
        - db
```

- After adding this to docker-compose.yml you can run

`docker compose up`

- If you have alredy done so and made changes, you can run

`docker compose up`


### 4. To create a virtual python environment run the command below 
`python -m venv env`

### 5. To activate virtual python environment 
`./env/Scripts/activate`

### 6. To install all the required packages 
`pip install -r "requirement.txt"`

### 7. Setting up migrations 
`alembic init alembic`

### 8. Change alembic/env.py to include
```python

config.set_main_option('sqlalchemy.url', os.environ['DATABASE_URL'])
import models;
target_metadata = models.Base.metadata

```

### 8. Create new migrations 
`alembic revision -m "New Migration"`

### 9. Update DB to the new migration 
`alembic upgrade head`

### 10. To run the app 
`uvicorn main:app --reload`