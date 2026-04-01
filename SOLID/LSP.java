class Bird {
    public void eat() {
        System.out.println("Estoy comiendo");
    }
}

interface FlyingBird {
    void fly();
}

class Sparrow extends Bird implements FlyingBird {
    public void fly() {
        System.out.println("Estoy volando");
    }
}

class Penguin extends Bird {
    public void swim() {
        System.out.println("Estoy nadando");
    }
}

public static void makeBirdFly(FlyingBird bird) {
    bird.fly();
}