# Bookstore Management System

## Overview
The Bookstore Management System is a web-based application that allows users to manage a collection of books. It provides functionality for creating, reading, updating, and deleting book records, as well as user authentication.
![image](https://github.com/user-attachments/assets/869804a9-fe34-4edc-a1f6-3855c9b0539c)

## Features
- User Authentication (Login/Logout)
- Create new book entries
- View list of all books
- Update existing book information
- Delete book entries
- Responsive design for various screen sizes

## Technologies Used
- Frontend:
  - HTML5
  - CSS3
  - JavaScript (ES6+)
  - Axios for API requests
- Backend:
  - Django (Python web framework)
  - Django REST Framework
  - SQLite database (can be configured for other databases)
- Authentication:
  - JSON Web Tokens (JWT)

## Prerequisites
- Python 3.8+
- Node.js and npm (for managing frontend dependencies)
- Django 3.2+
- Django REST Framework
- django-cors-headers

## Setup and Installation

### Backend Setup
1. Clone the repository:
   ```
   git clone https://github.com/your-username/bookstore-management.git
   cd bookstore-management
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Start the Django development server:
   ```
   python manage.py runserver
   ```

### Frontend Setup
1. Open the `index.html` file in a web browser.

2. Ensure that the `API_URL` in the JavaScript code points to your Django backend URL (default is `http://localhost:8000/api/`).

## Usage
1. Open the application in a web browser.
2. Log in using your credentials.
3. Use the interface to manage books:
   - Create new books
   - View the list of books
   - Update book information
   - Delete books
4. Use the logout button to end your session.

## API Endpoints
- `POST /api/token/`: Obtain JWT token
- `GET /api/books/`: List all books
- `POST /api/books/`: Create a new book
- `GET /api/books/{id}/`: Retrieve a specific book
- `PUT /api/books/{id}/`: Update a specific book
- `DELETE /api/books/{id}/`: Delete a specific book

## Security Considerations
- Ensure to use HTTPS in production.
- Implement proper input validation and sanitization.
- Regularly update dependencies to patch security vulnerabilities.

## Future Enhancements
- Implement user registration
- Add search and filter functionality for books
- Integrate with a book API for additional information
- Implement pagination for large datasets
- Add unit and integration tests

## Contributing
Contributions to this project are welcome. Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact
Sujeet Yadav-- sujeetyadav02222@gmail.com

Project Link: [https://github.com/your-username/bookstore-management](https://github.com/sujeetsj/Bookstore-Management/tree/main/bookstore)
