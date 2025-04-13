import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CartService } from '../../services/cart.service';

@Component({
  selector: 'app-books',
  standalone: true,
  templateUrl: './books.component.html',
  styleUrls: ['./books.component.css'],
  imports: [CommonModule]
})
export class BooksComponent {
  books = [
    { title: 'Book 1', author: 'Author 1', price: 10, image: 'assets/book1.jpg' },
    { title: 'Book 2', author: 'Author 2', price: 15, image: 'assets/book2.jpg' },
  ];

  constructor(private cartService: CartService) {}

  addToCart(book: any) {
    this.cartService.addToCart(book);
    alert(`${book.title} added to cart`);
  }
}
