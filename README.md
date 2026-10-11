# Student Management System

A RESTful API built using Python and Django REST Framework to manage student records, authenticate users, and control access using JWT authentication and permissions.

## Live Demo

- **Live API:** https://student-management-system-jccj.onrender.com/api/login/
- **GitHub Repository:** https://github.com/vrsolanki2004-ai/Student-Management-System

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- JWT Authentication (Simple JWT)
- Thunder Client
- Render

## Features

- User registration with password validation
- User login with JWT access and refresh tokens
- View student records after authentication
- Create, update, and delete student records with staff-only permissions
- API testing using Thunder Client
- Deployment on Render

## API Endpoints

| Method | Endpoint | Description | Expected Result |
|---|---|---|---|
| POST | `/api/register/` | Register a new user | 201 Created |
| POST | `/api/login/` | Log in and obtain JWT tokens | 200 OK |
| POST | `/api/token/refresh/` | Refresh an access token | 200 OK with valid refresh token |
| GET | `/api/students/` | View student records | 200 OK for authenticated users |
| POST | `/api/students/` | Create a student | 403 Forbidden for ordinary users |
| GET | `/api/students/<id>/` | View one student | 200 OK for authenticated users |
| PATCH | `/api/students/<id>/` | Update a student | 403 Forbidden for ordinary users |
| DELETE | `/api/students/<id>/` | Delete a student | 403 Forbidden for ordinary users |

Staff users can create, update, and delete student records. Ordinary registered users can view records but cannot modify them.

## How to Test the API

Use Postman or Thunder Client to send requests.

### 1. Register a User

**POST**
`https://student-management-system-jccj.onrender.com/api/register/`

Body → JSON:

```json
{
  "username": "demo_user",
  "email": "demo_user@example.com",
  "password": "UseYourOwnStrongPassword123!"
}
```

Expected response: `201 Created`

Use a unique username and a strong password.

### 2. Log In

**POST**
`https://student-management-system-jccj.onrender.com/api/login/`

Body → JSON:

```json
{
  "username": "demo_user",
  "password": "UseYourOwnStrongPassword123!"
}
```

Expected response: `200 OK`

The response contains an `access` token and a `refresh` token.

### 3. View Student Records

**GET**
`https://student-management-system-jccj.onrender.com/api/students/`

In the Authorization settings:

1. Select **Bearer Token**.
2. Paste the `access` token from the login response.
3. Send the request.

Expected response: `200 OK`

### 4. Test Permissions

Use the same access token from the ordinary user account.

Try sending POST to `/api/students/`, PATCH to `/api/students/1/`, and DELETE to `/api/students/1/`.

Expected response: `403 Forbidden` for these restricted operations.

## Run Locally

1. Clone the repository:

```bash
git clone https://github.com/vrsolanki2004-ai/Student-Management-System.git
cd Student-Management-System
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

3. Install project dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

Local API base URL: `http://127.0.0.1:8000/api/`

## Security Notes

- Passwords are handled using Django's user creation and password validation mechanisms.
- Protected endpoints require JWT authentication.
- Ordinary users cannot create, update, or delete student records.
- Never publish passwords, secret keys, or JWT tokens in the repository.
- Use fictional student data when sharing a public demo.

## Author

**Vivek Solanki**

B.Tech — Electronics & Telecommunication Engineering