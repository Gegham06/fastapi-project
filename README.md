# FastAPI Blogging Platform

A full-stack blogging application built with **FastAPI**, featuring user authentication, profile management, post management, and a server-rendered web interface.

The project combines a RESTful API with a web application, allowing users to create accounts, manage their profiles, publish posts, and interact with content.

## Features

### Authentication & User Management
- User registration with email and username uniqueness validation.
- JWT-based authentication using OAuth2.
- Secure password hashing with Argon2.
- Access token expiration and validation.
- Retrieve public and private user information.
- Update and delete user accounts.
- Authorization checks to protect user resources.

### Post Management
- Create new posts.
- Retrieve individual posts.
- Retrieve all posts with pagination.
- Update existing posts.
- Support for both full and partial updates (`PUT` and `PATCH`).
- Delete posts.
- Associate posts with their authors.
- Restrict post modifications to their owners.

### Profile Picture Management
- Upload user profile pictures.
- Validate uploaded image files.
- Limit upload size to 5 MB.
- Automatically resize images to 300 × 300 pixels.
- Convert processed images to optimized JPEG format.
- Replace and delete existing profile pictures.
- Generate unique filenames to avoid collisions.

### Web Interface
- Server-side HTML rendering with Jinja2.
- Dedicated login and registration pages.
- Homepage displaying recent posts.
- Individual post pages.
- User-specific post pages.
- Account management page.
- Static files and media management.
- Custom error pages.

### Additional Features
- Asynchronous database operations.
- SQLAlchemy ORM integration.
- Pydantic request and response validation.
- Pagination with total post counts.
- Consistent HTTP error handling.
- Automatic database table creation during application startup.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.13+ | Programming language |
| FastAPI | Backend framework |
| SQLAlchemy | ORM and database operations |
| SQLite | Database |
| aiosqlite | Asynchronous SQLite driver |
| Pydantic | Data validation and serialization |
| Pydantic Settings | Application configuration |
| PyJWT | JWT authentication |
| pwdlib (Argon2) | Password hashing |
| Jinja2 | HTML templating |
| Pillow | Image processing |
| Uvicorn | ASGI server |
| uv | Python dependency management |

## Project Structure

```text
fastapi-project/
│
├── routers/
│   ├── posts.py
│   └── users.py
│
├── src/
│   └── fastapi_project/
│
├── static/
│   └── ...
│
├── templates/
│   ├── home.html
│   ├── post.html
│   ├── login.html
│   ├── register.html
│   ├── account.html
│   └── ...
│
├── media/
│   └── profile_pics/
│
├── auth.py
├── config.py
├── database.py
├── image_utils.py
├── main.py
├── models.py
├── schemas.py
│
├── pyproject.toml
├── uv.lock
└── README.md
```

## Application Architecture

The application separates its main responsibilities into different modules:

- **main.py:** Application entry point, router registration, web pages, static files, and exception handlers.
- **routers/:** Contains API endpoints for user and post operations.
- **auth.py:** Password hashing, JWT generation, token verification, and current-user authentication.
- **database.py:** Asynchronous database engine, session management, and SQLAlchemy configuration.
- **models.py:** Database models and relationships between users and posts.
- **schemas.py:** Pydantic models for request validation and response serialization.
- **config.py:** Application settings and environment-based configuration.
- **image_utils.py:** Profile image processing and file management.
- **templates/:** HTML templates rendered using Jinja2.
- **static/:** Static assets such as CSS, JavaScript, and default images.
- **media/:** Uploaded user profile pictures.

## Installation & Setup

### Prerequisites

- Python 3.13 or newer.
- [uv](https://docs.astral.sh/uv/).

### 1. Clone the repository

```bash
git clone https://github.com/Gegham06/fastapi-project.git

cd fastapi-project
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Use a securely generated secret key rather than the example value.

### 4. Run the application

```bash
uv run uvicorn main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

### 5. Explore the API documentation

FastAPI automatically generates interactive API documentation.

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## API Endpoints

The application exposes two main API groups.

### Users

Base URL: `/api/users`

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| POST | `/` | Register a new user | No |
| POST | `/token` | Authenticate and obtain an access token | No |
| GET | `/me` | Retrieve current user information | Yes |
| GET | `/{user_id}` | Retrieve public user information | No |
| PATCH | `/{user_id}` | Update user information | Yes |
| DELETE | `/{user_id}` | Delete a user account | Yes |
| GET | `/{user_id}/posts` | Retrieve a user's posts | No |
| PATCH | `/{user_id}/picture` | Upload or replace profile picture | Yes |
| DELETE | `/{user_id}/picture` | Delete profile picture | Yes |

### Posts

Base URL: `/api/posts`

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| POST | `/` | Create a new post | Yes |
| GET | `/` | Retrieve posts with pagination | No |
| GET | `/{post_id}` | Retrieve a specific post | No |
| PUT | `/{post_id}` | Fully update a post | Yes |
| PATCH | `/{post_id}` | Partially update a post | Yes |
| DELETE | `/{post_id}` | Delete a post | Yes |

**Authentication:** Protected endpoints require a valid JWT access token.

Include the token in the request header:

```http
Authorization: Bearer <access_token>
```

### Pagination

Post listing endpoints support pagination through query parameters.

Example:

```http
GET /api/posts?skip=0&limit=10
```

The response includes:

- `posts` — returned posts.
- `total` — total number of posts.
- `skip` — number of skipped records.
- `limit` — maximum number of returned posts.
- `has_more` — indicates whether additional posts are available.

## Database Design

The application currently uses SQLite with asynchronous SQLAlchemy operations.

Two primary database models are implemented:

**User**
- ID
- Username
- Email
- Password hash
- Profile picture filename

**Post**
- ID
- Title
- Content
- User ID (foreign key)
- Publication date

Each user can have multiple posts through a one-to-many relationship.

Deleting a user also deletes their associated posts through SQLAlchemy relationship cascading.

Database tables are initialized automatically during application startup.

## Authentication Flow

The application uses OAuth2 password authentication with JWT access tokens.

The authentication process follows these steps:

1. A user registers with a username, email, and password.
2. The password is hashed using Argon2 before being stored.
3. The user submits their credentials to the token endpoint.
4. The application verifies the credentials.
5. A JWT access token is generated and returned.
6. The client includes the token in subsequent protected requests.
7. FastAPI dependencies validate the token and retrieve the authenticated user.

Access tokens have a configurable expiration time, set to 30 minutes by default.

## Error Handling & Validation

The application implements:

- Pydantic validation for incoming requests.
- HTTP status codes for common API errors.
- Authentication and authorization checks.
- Custom HTML error pages for web requests.
- Standard FastAPI error responses for API requests.
- Validation error handling for invalid user input.

## Future Improvements

Potential areas for further development include:

- Database migration management with Alembic.
- Automated unit and integration tests.
- Docker containerization.
- Deployment configuration.
- Improved API versioning.
- Additional authentication and account security features.

## Author

**Gegham Kirakosyan**

GitHub: [@Gegham06](https://github.com/Gegham06)

---

*Built as a hands-on project to explore backend development, asynchronous programming, REST API design, authentication, database relationships, and full-stack application development using FastAPI.*