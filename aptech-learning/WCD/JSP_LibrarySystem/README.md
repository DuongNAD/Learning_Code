# JSP Library System

## Tools Used
- IntelliJ IDEA
- Smart Tomcat
- MySQL 8
- JPA (Hibernate)
- JSP / Servlets

## How to run
1. Create a database `library_db` in MySQL and run the `database.sql` script to create tables and dummy data.
2. Edit `src/main/resources/META-INF/persistence.xml` to match your MySQL `root` password.
3. Open the project in IntelliJ IDEA as a Maven Project.
4. Setup Smart Tomcat: Add a new Smart Tomcat Configuration. Set Tomcat Server, Deployment directory to `src/main/webapp`, Context path to `/`.
5. Run the Smart Tomcat configuration and access `http://localhost:8080/`.

## Author
Hoang Nguyen Duc
