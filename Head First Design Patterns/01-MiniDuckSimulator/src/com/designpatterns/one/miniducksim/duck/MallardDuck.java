package com.designpatterns.one.miniducksim.duck;

import com.designpatterns.one.miniducksim.fly.FlyWithWings;
import com.designpatterns.one.miniducksim.quack.Quack;

public class MallardDuck extends Duck {
	
	public MallardDuck(){
		quackBehavior = new Quack();
		flyBehavior = new FlyWithWings();
	}

	@Override
	public void display() {
		System.out.println("I'm a real Mallard Duck");

	}

}
