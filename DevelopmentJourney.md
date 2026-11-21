## Development Journey

This project was developed incrementally, with each stage introducing new concepts and expanding the application's functionality.

The development process covered the following milestones:

### 1. Initial Setup & Frontend Foundation
**November 8, 2026**

- Initialized the FastAPI project and installed the required dependencies.
- Introduced Jinja2 for server-side HTML templating.
- Created the initial frontend structure with static files and templates.
- Implemented the initial post layout.
- Explored request validation, response validation, and exception handling.
- Added custom layouts for displaying errors.

### 2. Database Integration & CRUD Operations
**November 9–11, 2026**

- Introduced SQLAlchemy models and database relationships.
- Redesigned Pydantic schemas to work with the database models.
- Integrated database operations into the application.
- Implemented CRUD functionality for users and posts.
- Added update and delete operations using HTTP methods such as PUT, PATCH, and DELETE.
- Fixed integration issues and tested database functionality.

### 3. Asynchronous Programming & Application Architecture
**November 12–13, 2026**

- Converted the application from synchronous to asynchronous database operations.
- Worked with SQLAlchemy's asynchronous API.
- Organized API endpoints into separate modules using FastAPI's `APIRouter`.
- Improved database configuration.
- Started connecting frontend forms with backend API endpoints using JavaScript.

### 4. Frontend Integration
**November 13–16, 2026**

- Connected frontend forms to the REST API.
- Implemented JavaScript-based form submissions.
- Integrated frontend functionality with backend endpoints.
- Improved communication between the browser and the API.

### 5. Authentication & Authorization
**November 16–17, 2026**

- Implemented user registration and login.
- Introduced secure password hashing using Argon2.
- Implemented JWT generation and verification.
- Added token storage and authentication state management on the frontend.
- Built an authorization layer to identify the currently authenticated user.
- Removed hard-coded user IDs from schemas and frontend logic.
- Introduced ownership checks to ensure users can only create, edit, and delete their own content.

### 6. File Uploads & Image Processing
**November 18, 2026**

- Integrated Pillow for image processing.
- Implemented image validation and storage utilities.
- Added profile picture upload functionality.
- Used a thread pool for CPU-intensive image processing to avoid blocking asynchronous endpoints.
- Implemented profile picture previews on the frontend.
- Improved frontend handling of file uploads and form data.

### 7. Pagination
**November 20, 2026**

- Introduced `skip` and `limit` query parameters.
- Added pagination parameter validation.
- Created a dedicated paginated post response schema.
- Implemented database-level pagination using SQLAlchemy's `offset()` and `limit()`.
- Connected pagination functionality to the frontend through a "Load More" button.

### 8. Documentation
**November 21, 2026**

- Started documenting the application and its architecture.
- Prepared the project README to explain its functionality, technologies, setup, and development process.