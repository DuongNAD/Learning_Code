package BTVN_Java2.Day2;

import java.util.ArrayList;
import java.util.List;

public class RepositoryPattern {
    interface Repository<T> {
        void add(T t);
        T  get(int id);
    }
    class User {
        String name;
        public User(String name) {
            this.name = name;
        }
        @Override
        public String toString() {
            return name;
        }
    }
    class UserRepository implements Repository<User> {
        private List<User> users = new ArrayList<User>();
        @Override
        public void add(User t) {
            users.add(t);
        }
        @Override
        public User get(int id) {
            return users.get(id);
        }
    }
}
