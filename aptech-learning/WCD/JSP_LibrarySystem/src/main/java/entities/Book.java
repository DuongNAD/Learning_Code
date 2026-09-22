package entities;

import javax.persistence.*;
import javax.validation.constraints.Min;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import java.io.Serializable;
import java.util.List;

@Entity
@Table(name = "books")
public class Book implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @NotNull(message = "Title cannot be null")
    @Size(min = 3, message = "Title must be at least 3 characters")
    @Column(name = "title", nullable = false)
    private String title;

    @NotNull(message = "Author cannot be null")
    @Column(name = "author", nullable = false)
    private String author;

    @Min(value = 1, message = "Total copies must be at least 1")
    @Column(name = "total_copies", nullable = false)
    private int totalCopies;
    
    @OneToMany(mappedBy = "book", cascade = CascadeType.ALL)
    private List<Borrower> borrowers;

    // Getters and Setters
    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getAuthor() { return author; }
    public void setAuthor(String author) { this.author = author; }
    public int getTotalCopies() { return totalCopies; }
    public void setTotalCopies(int totalCopies) { this.totalCopies = totalCopies; }
    public List<Borrower> getBorrowers() { return borrowers; }
    public void setBorrowers(List<Borrower> borrowers) { this.borrowers = borrowers; }
}
