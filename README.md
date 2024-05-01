<h2>ProfileInfo API Documentation</h2>

<p>The <strong>ProfileInfo</strong> API provides information about a user profile based on the provided <code>profile_id</code>. This API retrieves details such as the user's first name, last name, university, specialization, badges, enrolled courses, time spent, and more, depending on the user's role as a student or teacher.</p>

<h3>Endpoint</h3>

<pre><code>GET /api/profiles/&lt;profile_id&gt;/</code></pre>

<h3>Parameters</h3>

<ul>
  <li><code>profile_id</code> (integer): The unique identifier of the user profile.</li>
</ul>

<h3>Authentication</h3>

<p>This API requires authentication using a valid JWT (JSON Web Token) provided in the request headers.</p>

<h3>Response</h3>

<p>The API returns a JSON object containing the user profile information. The structure of the response varies based on the user's role:</p>

<h4>Student Profile</h4>

<pre><code>{
  "FirstName": "John",
  "LastName": "Doe",
  "University": "University of XYZ",
  "Speciality": "Computer Science",
  "Score": 100,
  "Badges": ["Badge1", "Badge2"],
  "img": "file:///C:/Users/ADMI/Desktop/finale/FinalProject/image.jpg",
  "DailyTimeSpent": 120,  // Time spent in minutes
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
  "CanEdit": true  // Indicates if the user can edit their profile
}</code></pre>

<h4>Teacher Profile</h4>

<pre><code>{
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
}</code></pre>

<h3>Errors</h3>

<ul>
  <li><strong>404 Not Found</strong>: Returned if the specified <code>profile_id</code> does not exist.</li>
  <li><strong>401 Unauthorized</strong>: Returned if the request lacks proper authentication credentials or the JWT is invalid or expired.</li>
</ul>
