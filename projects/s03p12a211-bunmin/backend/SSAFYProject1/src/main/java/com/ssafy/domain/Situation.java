package com.ssafy.domain;

public class Situation {
	private int month;
	private long count;

	public Situation(int month, long count) {
		this.month = month;
		this.count = count;
	}

	public int getMonth() {
		return month;
	}

	public void setMonth(int month) {
		this.month = month;
	}

	public long getCount() {
		return count;
	}

	public void setCount(long count) {
		this.count = count;
	}

	@Override
	public String toString() {
		return "test [month=" + month + ", count=" + count + "]";
	}

}
