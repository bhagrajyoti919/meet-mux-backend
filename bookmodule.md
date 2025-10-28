# Day 2: Creating the Book Model

## 1. Main Project (PBL Context)
In today’s session, we will create a Mongoose model for the book. This model will define the structure of the data that will be stored in the MongoDB database. By the end of this day, you’ll have a solid understanding of how to structure your data in MongoDB using Mongoose.

## 2. Today's Problem Statement (PSBL)
**Standard Problem Statement:**  
Create a Mongoose model for books to define how the book data will be stored in the database.

**User Story Format:**  
As a developer, I want to create a Mongoose model for a book so that I can define the structure of the book data in MongoDB and make CRUD operations easier.

## 3. Learning Objectives
By the end of this session, learners will be able to:
- Understand how to define a model in Mongoose.
- Learn how to define fields and their data types.
- Understand the role of validation in Mongoose models.
- Create a model for books with necessary fields.

## 4. Scenario-Based Framing
Imagine you're building a backend for a library management system. The library needs to manage books, and each book has various attributes, such as title, author, genre, and publication date. To store this information in MongoDB, you will need to create a Mongoose model that represents a book and ensures that the data is properly validated.

## 5. Mini Visual Roadmap
1. Define the Mongoose schema for the book.
2. Implement the model for the book using Mongoose.
3. Validate incoming book data using Mongoose’s built-in validation.
4. Test the model by using Postman or directly within the API.

## 6. Conceptual Explanation (Notes, Code Walkthrough)

### What is a Mongoose Model?
Mongoose models are used to interact with MongoDB collections in a structured way. They help define the structure and validation rules for the data being stored.

### Creating a Book Model
In Mongoose, you define a model using a schema. The schema defines the structure of the documents that will be saved in the MongoDB collection.

#### Example Book Schema


# Day 3: Creating Your First POST Route
## 1. Main Project (PBL Context)
Today, we’ll be focusing on creating a POST route for adding books to our system. This is a crucial part of the backend because we need to allow users (or admins) to insert new records into the MongoDB database through our API.
2. Today's Problem Statement (PSBL)
Standard Problem Statement: Create a POST route to add a book to the database.
 User Story Format: As a developer, I want to create a POST route that will allow users to add a book to the database so that the library can manage new book records effectively.
3. Learning Objectives
By the end of this session, learners will be able to:
Understand how to create a POST route in Express.


Learn how to validate incoming request data for creating a book.


Implement a Mongoose schema to structure the book data.


Test the POST route using Postman.


4. Scenario-Based Framing
Imagine you’re building a backend for a library management system, and the system needs to allow an admin to add new books. The POST route is the first step toward allowing the backend to store books in a MongoDB database.
5. Mini Visual Roadmap
Create a Mongoose schema for the book model.


Implement the POST route using Express.


Validate incoming request data.


Test the route using Postman to ensure it’s working properly.


6. Conceptual Explanation (Notes, Code Walkthrough)
What is a POST Route in Express?
 A POST route is used to send data to the server, typically used for creating new records in a database. In this case, we’ll be creating a route that allows the client to send book data to our backend, where it will be stored in the MongoDB database.
Mongoose Model for Book:
 We need to define a Mongoose schema to structure the data that will be added to the database.
Example:
javascript

// models/Book.js
import mongoose from 'mongoose';

const bookSchema = new mongoose.Schema({
  title: { type: String, required: true },
  author: { type: String, required: true },
  genre: { type: String, required: true },
  publishedDate: { type: Date, required: true },
});

const Book = mongoose.model('Book', bookSchema);

export default Book;

Implementing the POST Route:
 In the routes/books.js file, we’ll implement the POST route to handle requests to add a new book to the database.
Example:
javascript
CopyEdit
// routes/books.js
import express from 'express';
import Book from '../models/Book.js';

const router = express.Router();

// POST route to add a new book
router.post('/add', async (req, res) => {
  const { title, author, genre, publishedDate } = req.body;

  const newBook = new Book({
    title,
    author,
    genre,
    publishedDate,
  });

  try {
    await newBook.save();
    res.status(201).json({ message: 'Book added successfully!' });
  } catch (error) {
    res.status(400).json({ message: 'Error adding book', error: error.message });
  }
});

export default router;

7. Hands-On Implementation (Integration in Main Project)
Step-by-step Implementation:
Book Model:


Create models/Book.js and define the Mongoose schema.


Add POST Route:


 Implement the POST route in routes/books.js to handle the creation of new books.


Test POST Route in Postman:


Open Postman and make a POST request to http://localhost:8000/books/add (or http://localhost:8000/api/books/add) with the following body:

 json
CopyEdit
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "genre": "Fiction",
  "publishedDate": "1925-04-10"
}


8. Output-Based Assessment
✅ Task 1: Implement the POST route to add books to the database.
 ✅ Task 2: Test the POST route using Postman to ensure that new books are being added correctly.


 Day 4: Implementing the POST Route for Adding a New Book
1. Main Project (PBL Context)
Today’s focus is on implementing the POST route to allow the creation of new books. We’ll utilize the models/Book.js from Day 2 to accept incoming data and store it in MongoDB. By the end of this session, you’ll be able to add books to your database through the API.
2. Today's Problem Statement (PSBL)
Standard Problem Statement: Implement a POST route to add a new book to the MongoDB database.
 User Story Format: As a developer, I want to implement a POST route to add a new book so that I can store book data in the database for future retrieval and management.
3. Learning Objectives
By the end of this session, learners will be able to:
Understand how to handle HTTP POST requests using Express.


Learn how to interact with MongoDB using Mongoose to save data.


Implement the logic for adding a new book to the database.


Test the POST route using Postman.


4. Scenario-Based Framing
Imagine you're building the backend for a library management system. The library admin needs to add books to the system. By implementing a POST route, the admin can submit book data, which will be saved to MongoDB. Without this functionality, the library system would be unable to store new books.
5. Mini Visual Roadmap
Set up a POST route in the Express server.


Use the models/Book.js to create a new book document.


Save the new book document to MongoDB.


Test the POST route using Postman.


6. Conceptual Explanation (Notes, Code Walkthrough)
What is a POST Route?
 A POST route in Express is used to handle incoming requests where data is sent to the server (usually from a form or client-side application). In this case, the POST route will accept book data and save it to the MongoDB database.
Handling POST Requests in Express:
Express will receive the POST request.


Data from the client will be extracted from the request body.


The data will be passed to the Mongoose model (book model).


Mongoose will validate and save the new book document to the MongoDB database.


A response will be sent back to the client indicating success or failure.


Example POST Route Code:
javascript
CopyEdit
// routes/books.js
import express from 'express';
import Book from '../models/Book.js';

const router = express.Router();

// POST route to create a new book
router.post('/add', async (req, res) => {
  try {
    // Extract data from the request body
    const { title, author, genre, publishedDate } = req.body;

    // Create a new book document
    const newBook = new Book({
      title,
      author,
      genre,
      publishedDate,
    });

    // Save the new book to the database
    await newBook.save();

    // Send success response
    res.status(201).json({ message: 'Book added successfully', book: newBook });
  } catch (error) {
    // Send error response
    res.status(500).json({ message: 'Error adding book', error: error.message });
  }
});

export default router;

Explanation of Code:
We import the necessary modules and create a new express.Router.


We define a POST route at /add which listens for book data in the request body.


We use the Mongoose model to create a new book document.


If the book is successfully saved to MongoDB, we send a success message along with the book data.


If there's an error, we catch it and send an error message back to the client.


7. Hands-On Implementation (Integration in Main Project)
Step-by-step Implementation:
Set up the POST route:


 In your routes/books.js, define the POST route as shown in the example above.


Ensure that you include the necessary middleware (e.g., express.json()) to parse incoming JSON data.


Connect the route in index.js:


 In your index.js (or the main server file), make sure to import and use the routes/books.js file so the POST route is available in the API.


javascript
CopyEdit
// index.js
import express from 'express';
import mongoose from 'mongoose';
import cors from 'cors';
import booksRouter from './routes/books.js';

const app = express();

// Middleware setup
app.use(express.json());
app.use(cors());

// Mount books routes (both paths available)
app.use('/api/books', booksRouter);
app.use('/books', booksRouter);

mongoose.connect('<your_mongo_uri>')
  .then(() => {
    const port = Number(process.env.PORT || process.env.port || 8000);
    app.listen(port, () => console.log(`Server is running on port ${port}`));
  })
  .catch(err => console.log(err));


Test with Postman:


Open Postman and create a POST request to http://localhost:8000/books/add (or http://localhost:8000/api/books/add).


In the body of the request, add JSON data for the book:


json
CopyEdit
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "genre": "Fiction",
  "publishedDate": "1925-04-10"
}


Send the request and check if the book is added to the MongoDB database.


8. Output-Based Assessment
✅ Task 1: Implement the POST route to add a book.
 ✅ Task 2: Test the route using Postman.
 ✅ Task 3: Check the MongoDB database to verify the book has been added.

Day 5: Ensuring Required Fields with Validation
1. Main Project (PBL Context)
Today, we’ll focus on ensuring that the book data provided via the POST request has all the necessary fields. We'll use Mongoose’s built-in validation to enforce that required fields such as title, author, genre, and published date are present before a book can be added to the database.
2. Today's Problem Statement (PSBL)
Standard Problem Statement: Add validation to ensure that a book has required fields before it is added to the database.
 User Story Format: As a developer, I want to add validation to the book model to ensure that all required fields (title, author, genre, published date) are provided when adding a book so that only complete book data is stored in the database.
3. Learning Objectives
By the end of this session, learners will be able to:
Implement validation for required fields using Mongoose.


Understand how Mongoose handles validation errors.


Test the validation by attempting to add a book with missing or invalid data.


Learn how to return meaningful error messages to the client when validation fails.


4. Scenario-Based Framing
Imagine you're working on a backend for a library management system. The system should not allow incomplete or invalid book records to be added. For example, if a book is missing a title or an author, it should not be saved to the database. This ensures the integrity of the book data in your library system.
5. Mini Visual Roadmap
Add validation to the bookModel.js file.


Define required fields using Mongoose schema validation.


Test the validation with Postman by sending incomplete or invalid book data.


Handle validation errors and send appropriate responses to the client.


6. Conceptual Explanation (Notes, Code Walkthrough)
Mongoose Schema Validation:
 Mongoose provides a way to define validation rules for each field in a schema. By using required, minLength, maxLength, and other validation options, you can ensure that the data passed to MongoDB is in the correct format.
Steps for Adding Validation:
Modify the bookModel.js to include validation rules for each field.


Use the required: true property to ensure that each field must have a value before the document is saved.


If validation fails, Mongoose will throw an error, which we can catch in the route and return an appropriate response to the client.


Example Validation Code:
javascript
CopyEdit
// bookModel.js
import mongoose from 'mongoose';

const bookSchema = new mongoose.Schema({
  title: {
    type: String,
    required: [true, 'Title is required'],
  },
  author: {
    type: String,
    required: [true, 'Author is required'],
  },
  genre: {
    type: String,
    required: [true, 'Genre is required'],
  },
  publishedDate: {
    type: Date,
    required: [true, 'Published date is required'],
  },
});

const Book = mongoose.model('Book', bookSchema);

export default Book;

Explanation of Code:
We modify the bookSchema to ensure each field (title, author, genre, and published date) is required.


The required: [true, 'Field is required'] syntax provides both a Boolean value (true) and a custom error message that will be sent if validation fails.


This validation ensures that any attempt to add a book without a title, author, genre, or published date will be rejected.


7. Hands-On Implementation (Integration in Main Project)
Step-by-Step Implementation:
Update the Book Model:


Open your bookModel.js file.


Add the required validation for each field as shown in the example code above.


Update the POST Route:


In your booksRoute.js, the POST route doesn't need to be modified because Mongoose will automatically validate the data before attempting to save it. However, you need to handle the errors if the data doesn't meet the validation criteria.


javascript
CopyEdit
// booksRoute.js (POST route)
router.post('/add', async (req, res) => {
  try {
    const { title, author, genre, publishedDate } = req.body;
    
    // Create a new book instance with the request data
    const newBook = new Book({
      title,
      author,
      genre,
      publishedDate,
    });

    // Attempt to save the new book to the database
    await newBook.save();

    // Send success response
    res.status(201).json({ message: 'Book added successfully', book: newBook });
  } catch (error) {
    // If there's a validation error, send a detailed error message
    res.status(400).json({ message: 'Error adding book', error: error.message });
  }
});


Test the Validation:


Open Postman and test the validation by trying to add books with missing or invalid fields.


Test Case 1: Send a POST request without a title or author.


Test Case 2: Send a POST request with a valid title, author, but no published date.


Test Case 3: Send a valid book with all required fields.


Check the responses to ensure that incomplete or invalid data is rejected and that appropriate error messages are returned.


8. Output-Based Assessment
✅ Task 1: Implement validation for required fields in the bookModel.js file.
 ✅ Task 2: Handle validation errors in the POST route.
 ✅ Task 3: Test the validation using Postman by sending incomplete data.
