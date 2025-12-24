import React, { Component } from "react";

const TICKET_PRICE = 100000;
const TOTAL_SEATS = 20;

class TicketBooking extends Component {
  constructor(props) {
    super(props);
    this.state = {
      quantity: 0,
    };
  }

  handleIncrease = () => {
    if (this.state.quantity < TOTAL_SEATS) {
      this.setState((prevState) => ({
        quantity: prevState.quantity + 1,
      }));
    }
  };

  handleDecrease = () => {
    if (this.state.quantity > 0) {
      this.setState((prevState) => ({
        quantity: prevState.quantity - 1,
      }));
    }
  };
  render() {
    const { quantity } = this.state;
    const totalPrice = quantity * TICKET_PRICE;

    return (
      <div className="booking-container">
        <h1>Đặt vé xem phim</h1>
        <p>Giá vé đồng hạng ({TICKET_PRICE.toLocaleString()} vnd/vé)</p>
        <div className="quantity-control">
          <span>Số lượng: {quantity}</span>
          <div className="buttons">
            <button onClick={this.handleDecrease}>-</button>
            <button onClick={this.handleIncrease}>+</button>
            
          </div>
        </div>
        <h2 className="total-price">
          Tổng giá: {totalPrice.toLocaleString()} vnd
        </h2>
        <p className="seats-info">
          Ghế: {quantity}/{TOTAL_SEATS} đã đặt
        </p>
      </div>
    );
  }
}

export default TicketBooking;