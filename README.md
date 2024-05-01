ProfileInfo API Documentation

The ProfileInfo API provides information about a user profile based on the provided profile_id. This API retrieves details such as the user's first name, last name, university, specialization, badges, enrolled courses, time spent, and more, depending on the user's role as a student or teacher.
Endpoint

bash

GET /api/profiles/<profile_id>/

Parameters

    profile_id (integer): The unique identifier of the user profile.

Authentication

This API requires authentication using a valid JWT (JSON Web Token) provided in the request headers.
Response

The API returns a JSON object containing the user profile information. The structure of the response varies based on the user's role:
Student Profile

json

{
  "FirstName": "John",
  "LastName": "Doe",
  "University": "University of XYZ",
  "Speciality": "Computer Science",
  "Score": 100,
  "Badges": ["Badge1", "Badge2"],
  "img": "file:///C:/Users/ADMI/Desktop/finale/FinalProject/image.jpg",
  "DailyTimeSpent": 120,  # Time spent in minutes
  "WeeklyTimeSpent": 600,
  "MonthlyTimeSpent": 2500,
  "EnrollCourse": [
    {
      "course_id": 1,
      "title": "Course 1",
      "progress": 50
    },
    {
      "course_id": 2,
      "title": "Course 2",
      "progress": 80
    }
  ],
  "CanEdit": true  # Indicates if the user can edit their profile
}

Teacher Profile

json

{
  "FirstName": "Jane",
  "LastName": "Smith",
  "img": "file:///C:/Users/ADMI/Desktop/finale/FinalProject/image.jpg",
  "courses": [
    {
      "title": "Course 1"
    },
    {
      "title": "Course 2"
    }
  ]
}

Errors

    404 Not Found: Returned if the specified profile_id does not exist.
    401 Unauthorized: Returned if the request lacks proper authentication credentials or the JWT is invalid or expired.

