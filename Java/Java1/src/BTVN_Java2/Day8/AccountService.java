//package BTVN_Java2.Day8;
//
//import java.util.ArrayList;
//import java.util.List;
//import java.util.Observer;
//
//enum LoginStatus {
//    SUCCESS,
//    FAILURE,
//    INVALID,
//    EXPIRED
//}
//class User{
//    private String email;
//    private String ip;
//    private LoginStatus status;
//
//    public String getEmail() {
//        return email;
//    }
//    public void setEmail(String email) {
//        this.email = email;
//    }
//    public String getIp() {
//        return ip;
//    }
//    public void setIp(String ip) {
//        this.ip = ip;
//    }
//    public LoginStatus getStatus() {
//        return status;
//    }
//    public void setStatus(LoginStatus status) {
//        this.status = status;
//    }
//}
//public class AccountService {
//    private User user;
//    private List<Observer> observers  = new ArrayList<>();
//
//    public AccountService(String email, String ip) {
//        user = new User();
//        user.setEmail(email);
//        user.setIp(ip);
//    }
//
//    @Override
//    public void attach(Observer observer){
//        if(!observers.contains(observer)){
//            observers.add(observer);
//        }
//    }
//
//    @Override
//    public void detach(Observer observer){
//        if(observers.contains(observer)){
//            observers.remove(observer);
//        }
//    }
//
//    @Override
//    public void notifyAllObserver(){
//        for(Observer observer : observers){
//            observer.update(user);
//        }
//    }
//
//    public void changeStatus(LoginStatus status) {
//        user.setStatus(status);
//        System.out.println("Status is changed");
//        this.notifyAllObserver();
//    }
//
//    public void login() {
//
//        if (!this.isValidIP()) {
//            user.setStatus(LoginStatus.INVALID);
//        } else if (this.isValidEmail()) {
//            user.setStatus(LoginStatus.SUCCESS);
//        } else {
//            user.setStatus(LoginStatus.FAILURE);
//        }
//
//        System.out.println("Login is handled");
//        this.notifyAllObserver();
//    }
//
//    private boolean isValidIP() {
//        return "127.0.0.1".equals(user.getIp());
//    }
//
//    private boolean isValidEmail() {
//        return "contact@gpcoder.com".equalsIgnoreCase(user.getEmail());
//    }
//}
