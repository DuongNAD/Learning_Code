CREATE DATABASE IF NOT EXISTS library_db;
USE library_db;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    total_copies INT NOT NULL CHECK (total_copies >= 1)
);

CREATE TABLE borrowers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE
);

-- Sample Data
INSERT INTO books (title, author, total_copies) VALUES ('1984', 'G. Orwell', 5);
INSERT INTO books (title, author, total_copies) VALUES ('Dune', 'F. Herbert', 3);

INSERT INTO borrowers (book_id, name, email) VALUES (2, 'Alice Nguyen', 'alice@example.com');
INSERT INTO borrowers (book_id, name, email) VALUES (2, 'Bob Tran', 'bob@gmail.com');
