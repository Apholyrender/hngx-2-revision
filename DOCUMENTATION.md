
# Detailed API Documentation

Test each API with the URL commands under each endpoint with Postman, ThunderClient, or any other API testing tool.


---------------------------------------------------------------------------------------------------------------------------------------------
##### Endpoint 1: Get All User Accounts

Description:
    This endpoint retrieves a list of all user accounts.

How the Endpoint Works:
    When a GET request is sent to this endpoint, it queries the database to retrieve a list of all user accounts.


How to Call the Endpoint:
    HTTP Method: GET
    Endpoint Path: /api/

Parameters for Calling the Endpoint:
    None

Possible Responses from the Endpoint:
    Status Code: 200 OK
    Response Body: A list of user account profiles in JSON format.

Possible Error Messages:
    Status Code: 500 Internal Server Error
    This could occur if there is an issue with the database connection.

Example cURL for the Endpoint:

curl -X GET "http://localhost:8000/api/"


-------------------------------------------------------------------------------------------------------------------------------------------------
##### Endpoint 2: Get a Single User Account

Description:
    This endpoint retrieves information about a single user account by providing the user's unique identifier (user_id).

How the Endpoint Works:
    When a GET request is sent to this endpoint with a valid user_id, it queries the database to retrieve the details of the specified user.


How to Call the Endpoint:
    HTTP Method: GET
    Endpoint Path: /api/user


Parameters for Calling the Endpoint:
    user_id (Query Parameter, Required): The UUID of the user account you want to retrieve.


Possible Responses from the Endpoint:
    Status Code: 200 OK
    Response Body: User account details in JSON format.


Possible Error Messages:
    Status Code: 400 Bad Request
    This could occur if the user_id parameter is missing or invalid.
    Status Code: 404 Not Found
    This could occur if the specified user is not found in the database.
    Status Code: 500 Internal Server Error
    This could occur if there is an issue with the database connection.


Example cURL for the Endpoint:


curl -X GET "http://localhost:8000/api/user?user_id=put_user_id_here"



-------------------------------------------------------------------------------------------------------------------------------------------------
##### Endpoint 3: Create a User Account

Description:
    This endpoint allows the creation of a new user account by providing the necessary account information in the request body.

How the Endpoint Works:
    When a POST request is sent to this endpoint with the required account details in the request body, it creates a new user account in the database.


How to Call the Endpoint:
    HTTP Method: POST
    Endpoint Path: /api/


Parameters for Calling the Endpoint:
    Request Body: JSON object containing the user account details (e.g., username, email, password, etc.) as specified in the Account schema.


Possible Responses from the Endpoint:
    Status Code: 201 Created
    Response Body: The newly created user account profile in JSON format.


Possible Error Messages:
    Status Code: 400 Bad Request
    This could occur if the request body is missing or invalid.
    Status Code: 500 Internal Server Error
    This could occur if there is an issue with the database connection.


Example cURL for the Endpoint:

curl -X POST -H "Content-Type: application/json" -d '{
  "username": "new_user",
  "email": "new_user@example.com",
  "password": "password123"
}' "http://localhost:8000/api/"



-------------------------------------------------------------------------------------------------------------------------------------------------
##### Endpoint 4: Update a User Account

Description:
    This endpoint allows updating an existing user account by providing the user's unique identifier (user_id) and the updated account information in the request body.

How the Endpoint Works:
    When a PUT request is sent to this endpoint with a valid user_id and the updated account details in the request body, it updates the user account in the database.


How to Call the Endpoint:
    HTTP Method: PUT
    Endpoint Path: /api/user


Parameters for Calling the Endpoint:
    user_id (Query Parameter, Required): The UUID of the user account you want to update.
    Request Body: JSON object containing the updated user account details.


Possible Responses from the Endpoint:
    Status Code: 200 OK
    Response Body: The updated user account profile in JSON format.


Possible Error Messages:
    Status Code: 400 Bad Request
    This could occur if the user_id parameter is missing or invalid, or if the request body is missing or invalid.
    Status Code: 404 Not Found
    This could occur if the specified user is not found in the database.
    Status Code: 500 Internal Server Error
    This could occur if there is an issue with the database connection.


Example cURL for the Endpoint:

curl -X PUT -H "Content-Type: application/json" -d '{
  "username": "updated_user",
  "email": "updated_user@example.com"
}' 
"http://localhost:8000/api/user?user_id=put_user_id_here"



-------------------------------------------------------------------------------------------------------------------------------------------------
##### Endpoint 5: Delete a User Account

Description:
    This endpoint allows the deletion of an existing user account by providing the user's unique identifier (user_id).

How the Endpoint Works:
    When a DELETE request is sent to this endpoint with a valid user_id, it deletes the specified user account from the database.


How to Call the Endpoint:
    HTTP Method: DELETE
    Endpoint Path: /api/user


Parameters for Calling the Endpoint:
    user_id (Query Parameter, Required): The UUID of the user account you want to delete.


Possible Responses from the Endpoint:
    Status Code: 200 OK
    Response Body: A message indicating the successful deletion of the user account.


Possible Error Messages:
    Status Code: 400 Bad Request
    This could occur if the user_id parameter is missing or invalid.
    Status Code: 404 Not Found
    This could occur if the specified user is not found in the database.
    Status Code: 500 Internal Server Error
    This could occur if there is an issue with the database connection.
    Example cURL for the Endpoint:


curl -X DELETE "http://localhost:8000/api/user?user_id=put_user_id_here"



----------------------------------------------------------------------------------------------------------------------------------------------------

