# HNG-DevOps-Task1
Here's a `README.md` template for your project:

```markdown
# DevOps Stage 1 - Number Classification API

Welcome to the Number Classification API project! This API takes a number as input and returns interesting mathematical properties, such as whether the number is prime, perfect, or Armstrong, along with a fun fact about the number.

## Task Description

### Goal:
- Create an API that classifies a number based on its mathematical properties.
- The API should return the number's classification (e.g., prime, perfect, Armstrong), its digit sum, and a fun fact from the Numbers API.

## Technology Stack

You are free to use any programming language or framework of your choice. Here are a few options:
- C#
- PHP
- Python
- Go
- Java
- JavaScript/TypeScript

### Requirements:
- The API must be deployed to a publicly accessible endpoint.
- Handle CORS (Cross-Origin Resource Sharing).
- Responses should be in JSON format.

## API Specification

### Endpoint:
**GET** `/api/classify-number?number={number}`

### Response Format (200 OK):

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Response Format (400 Bad Request):

```json
{
    "number": "alphabet",
    "error": true
}
```

## Acceptance Criteria

### Functionality:
- The API should accept GET requests with a `number` parameter.
- Return JSON in the specified format.
- Only valid integers should be accepted as inputs.
- Return appropriate HTTP status codes for success and errors.

### Code Quality:
- Organize code structure effectively.
- Implement basic error handling and input validation.
- Avoid hardcoding values.

### Documentation:
- Provide a complete and well-structured `README.md`.

### Deployment:
- Ensure the API is publicly accessible and stable.
- The API must respond within 500ms.

## Additional Notes
- Use the [Numbers API](http://numbersapi.com/#42) to fetch the fun fact about the number.
- The properties of the number can include:
  - `"armstrong"`: If the number is an Armstrong number.
  - `"odd"` or `"even"`: Whether the number is odd or even.
  - `"prime"` or `"perfect"`: If applicable.

Possible combinations for the `properties` field:
- `["armstrong", "odd"]` — if the number is both an Armstrong number and odd.
- `["armstrong", "even"]` — if the number is both an Armstrong number and even.
- `["odd"]` — if the number is not an Armstrong number but is odd.
- `["even"]` — if the number is not an Armstrong number but is even.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yvonnegichovi/number-classification-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd number-classification-api
    ```

3. Install the necessary dependencies. (Adjust based on the language you used.)

    Example for Python:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Start the API server:

To start the API, run the following command:

Example for Python (Flask):

```bash
python app.py
```

The server will be accessible at `http://localhost:5000`.

### Example Requests:

- To classify the number 371, you can make a GET request:

```bash
curl "http://localhost:5000/api/classify-number?number=371"
```

- The response will look like:

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

## Tests

Run tests to verify the correctness of the API.

Example using pytest (for Python):

```bash
pytest
```

## Deployment

Once the API is complete and tested, deploy it to a publicly accessible platform like:
- Render
- Koyeb
- Heroku
- AWS Lambda
- Google Cloud Functions
- DigitalOcean

*- For this, I have decided to use Render *-

Ensure that CORS is handled and the API responds quickly.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
