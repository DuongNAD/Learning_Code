package BTVN_Java2.Day9;

import java.util.concurrent.Flow;

public class Subsciption <T> implements Flow.Subscriber<T> {
    private Flow.Subscription subscription;
    public void onSubscribe(Flow.Subscription subscription) {
        this.subscription = subscription;
        this.subscription.request(1);
    }
    @Override
    public void onNext(T t) {
        System.out.println(t);
        subscription.request(1);
    }
    @Override
    public void onError(Throwable throwable) {
        throwable.printStackTrace();
    }
    @Override
    public void onComplete() {
        System.out.println("Done");
    }
}
