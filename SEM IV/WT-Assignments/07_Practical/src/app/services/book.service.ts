import { Injectable } from '@angular/core';
import { Book } from '../models/book';

@Injectable({
  providedIn: 'root',
})
export class BookService {
  books: Book[] = [
    { id: 1, title: 'Angular for Beginners', author: 'John Doe', price: 25, image: 'assets/angular.png' },
    { id: 2, title: 'Mastering TypeScript', author: 'Jane Doe', price: 30, image: 'assets/typescript.png' },
    { id: 3, title: 'JavaScript Essentials', author: 'Mark Smith', price: 20, image: 'assets/javascript.png' }
  ];

  getBooks() {
    return this.books;
  }
}
