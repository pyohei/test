// Question 16-11

public class OneBank {
	private static int value = 0;
	public static synchronized void addMoney(int money) {
		int currentValue = value;
		System.out.println(Thread.currentThread() + " が addMoney に入りました。 "	);
		value += money;
						try {
				Thread.sleep(4000);
			} catch (InterruptedException e) {
			}
		
		if (currentValue + money != value) {
			System.out.println(Thread.currentThread() + " で矛盾が生じています。");
			System.exit(-1);
		}
		System.out.println (Thread.currentThread() + "がaddMoneyから出ました");
					try {
				Thread.sleep(4000);
			} catch (InterruptedException e) {
			}
	}
}