## FastAPi

https://www.youtube.com/watch?v=7t2alSnE2-I&t=172s

## FastApi Features
* Automatic docs: 
    * Swagger UI and 
    * ReDoc UI
* Python 3.6 with using **Pydantic**
* Based on open standard：
    * JSON Schema
    * Open API
* VS code/PyCharm Editor support
* Security snf authentication
    * HTTP Basic
    * OAuth2 (also with JWT tokens)
    * API keys in **Headers**, **Query parameters**, **Cookies**, etc.
* Dependency Injection
* Unlimited "plug-ins"
* Tested


## Starlette Features
* WebSocket support
* GraphQL support
* In-process background tasks
* Startup and shutdown events
* Test client built on requests
* CORS, GZip, Static Files, Streaming responses
* Session and Cookie support
* Other supports
    * SQL database
    * NoSQL database
    * GraphQL

## Basci concepts of FastApi
* Path Parameters
* API Docs - swagger/redoc
* Query parameters
* Request body

## Intermediate Concepts
* Debugging FastApi
* Pydantic Schemas
* SqlAIchemy database connection
* Models and table

## Database Tasks
* Store blog database
* Get blogs from database
* Delete
* Update

## Responses
* Handling Exceptions
* Return response
* Define response model

## User and Password
* Create user
* Hash user password
* Show single user
* define docs tags

## Relationship
* define User to Blog relationship
* define blog to user relationship

## Refactor for bigger Application
* API Router
* API Router with parameters

## Authentication with JWT (JWT: JSON Web Token)
* Create Login route
* Login and verify password
* Reture JWT access token
* Routes behind authentication

## Deploy FastApi
* USing **Deta.sh** website to deploy

=====================================================
## Setup environment:
```python
python -m venv fastapi_env      # Create an virtual environment
./fastapi_env/Scripts/activate  # activate the virtual environment
```