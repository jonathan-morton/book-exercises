package com.designpatterns.one.miniducksim.duck;

import com.designpatterns.one.miniducksim.fly.FlyNoWay;
import com.designpatterns.one.miniducksim.quack.Quack;

public class ModelDuck extends Duck {
	
	public ModelDuck(){
		flyBehavior = new FlyNoWay();
		quackBehavior = new Quack();
	}

	@Override
	public void display() {
		System.out.println("I'm a model duck");

	}

}
