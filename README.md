# flask-restful-api-boilerplate

This is a boilerplate project for building RESTful APIs using Flask and Flask-RESTful. It provides a solid foundation and a set of best practices to kickstart your API development.

**Note:** I use this boilerplate for my work projects. It might not be suitable for other use cases without modifications.

## Features

- Flask and Flask-RESTful for building RESTful APIs
- SQLAlchemy for database management
- JWT authentication using cookies for secure API access
  <!-- - Swagger UI for API documentation -->
  <!-- - Docker support for easy deployment -->

## Getting Started

To get started with the flask-restful-api-boilerplate, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/flask-restful-api-boilerplate.git`
2. Navigate to the project directory: `cd flask-restful-api-boilerplate`
3. Create a virtual environment: `python -m venv .venv`
4. Activate the virtual environment:
   - On Windows: `.venv\Scripts\activate`
   - On macOS/Linux: `source .venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Set up the database: `flask db init && flask db migrate && flask db upgrade`
7. Start the development server: `python app1.py`

<!-- ## API Documentation

The API documentation is available at [http://localhost:5000/api/docs](http://localhost:5000/api/docs) when running the development server. It provides detailed information about the available endpoints, request/response formats, and authentication requirements. -->

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
