import { Component } from '@angular/core';
import { CartService } from '../../services/cart.service';

@Component({
  selector: 'app-cart',
  standalone: true,
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css'],
  imports: []
})
export class CartComponent {
  cart: any[] = []; // Ensure cart is declared

  constructor(private cartService: CartService) {
    this.cart = this.cartService.getCart();
  }
}
