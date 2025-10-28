import mongoose from 'mongoose';

const { Schema } = mongoose;

const bookSchema = new Schema(
  {
    title: {
      type: String,
      required: [true, 'Title is required'],
      trim: true,
      minlength: 1,
      maxlength: 200,
    },
    author: {
      type: String,
      required: [true, 'Author is required'],
      trim: true,
      minlength: 1,
      maxlength: 120,
    },
    genre: {
      type: String,
      required: [true, 'Genre is required'],
      trim: true,
      maxlength: 80,
    },
    publishedDate: {
      type: Date,
      required: [true, 'Published date is required'],
    },
    pages: {
      type: Number,
      min: 1,
    },
    isbn: {
      type: String,
      trim: true,
      unique: true,
      sparse: true,
    },
    available: {
      type: Boolean,
      default: true,
    },
  },
  { timestamps: true }
);

const Book = mongoose.model('Book', bookSchema);

export default Book;