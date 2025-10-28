import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import mongoose from 'mongoose';
import booksRouter from './routes/books.js';


dotenv.config();
const app = express();

app.use(cors());
app.use(express.json());
app.use('/api/books', booksRouter);
app.use('/books', booksRouter);

const port = Number(process.env.PORT || process.env.port || 8000);
const mongoURI = process.env.mongodb_uri || 'mongodb://127.0.0.1:27017/meet-mux';
mongoose.connect(mongoURI)
  .then(() => {
    console.log('MongoDB connected');
    app.listen(port, () => {
      console.log(`Server is running on port ${port}`);
    });
  })
  .catch(() => console.log('MongoDB connection failed'));

app.get('/', (req, res) => {
  res.json({ message: 'Welcome to Meet Mux! The app is loading...' });
});