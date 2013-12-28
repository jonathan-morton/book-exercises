package com.designpatterns.one.miniducksim;

import com.designpatterns.one.miniducksim.duck.Duck;
import com.designpatterns.one.miniducksim.duck.MallardDuck;
import com.designpatterns.one.miniducksim.duck.ModelDuck;
import com.designpatterns.one.miniducksim.fly.FlyRocketPowered;

public class MiniDuckSimulator {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Duck mallard = new MallardDuck();
		mallard.performQuack();
		mallard.performFly();
		
		Duck model = new ModelDuck();
		model.performFly();
		model.setFlyBehavior(new FlyRocketPowered());
		model.performFly();

	}

}
