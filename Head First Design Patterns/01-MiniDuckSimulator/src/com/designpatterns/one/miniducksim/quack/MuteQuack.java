package com.designpatterns.one.miniducksim.quack;

public class MuteQuack implements QuackBehavior {

	@Override
	public void quack() {
		System.out.println("<< Silence >>");

	}

}
