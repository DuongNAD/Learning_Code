package com.tourbooking.entity;

import javax.persistence.*;
import javax.validation.constraints.Future;
import javax.validation.constraints.Min;
import javax.validation.constraints.NotNull;
import java.io.Serializable;
import java.util.Date;

@Entity
@Table(name = "bookings")
public class Booking implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "booking_id")
    private Integer bookingId;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id", referencedColumnName = "id")
    private User user;

    @NotNull(message = "Destination is required")
    @Column(name = "destination", nullable = false, length = 100)
    private String destination;

    @NotNull(message = "Departure date is required")
    @Future(message = "Departure date must be in the future")
    @Temporal(TemporalType.DATE)
    @Column(name = "departure_date", nullable = false)
    private Date departureDate;

    @NotNull(message = "Price is required")
    @Min(value = 100, message = "Price must be at least 100")
    @Column(name = "price", nullable = false)
    private Double price;

    @NotNull(message = "Status is required")
    @Column(name = "status", nullable = false)
    private String status;

    public Booking() {
    }

    // Getters and Setters

    public Integer getBookingId() {
        return bookingId;
    }

    public void setBookingId(Integer bookingId) {
        this.bookingId = bookingId;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }

    public Date getDepartureDate() {
        return departureDate;
    }

    public void setDepartureDate(Date departureDate) {
        this.departureDate = departureDate;
    }

    public Double getPrice() {
        return price;
    }

    public void setPrice(Double price) {
        this.price = price;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}
