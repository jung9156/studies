package com.ssafy.domain;

import java.util.Calendar;

public class Notice {
	private int notice_no;
	private String notice_id;
	private String notice_title;
	private String notice_content;
	private String notice_date;
	private String notice_time;
	private Calendar calendar = Calendar.getInstance();

	public Notice() {}
	public Notice(int notice_no, String notice_id, String notice_title, String notice_content, String notice_date,
			String notice_time) {
		this.notice_no = notice_no;
		this.notice_id = notice_id;
		this.notice_title = notice_title;
		this.notice_content = notice_content;
		this.notice_date = notice_date;
		this.notice_time = notice_time;
	}

	public int getNotice_no() {
		return notice_no;
	}

	public void setNotice_no(int notice_no) {
		this.notice_no = notice_no;
	}

	public String getNotice_id() {
		return notice_id;
	}

	public void setNotice_id(String notice_id) {
		this.notice_id = notice_id;
	}

	public String getNotice_title() {
		return notice_title;
	}

	public void setNotice_title(String notice_title) {
		this.notice_title = notice_title;
	}

	public String getNotice_content() {
		return notice_content;
	}

	public void setNotice_content(String notice_content) {
		this.notice_content = notice_content;
	}

	public String getNotice_date() {
		return notice_date;
	}

	public void setNotice_date(String notice_date) {
		this.notice_date = notice_date;
	}

	public String getNotice_time() {
		return notice_time;
	}

	public void setNotice_time(String notice_time) {
		this.notice_time = notice_time;
	}
	
	public Calendar getCalendar() {
		return calendar;
	}
	
	public void setCalendar(Calendar calendar) {
		this.calendar = calendar;
	}
	
	@Override
	public String toString() {
		return "Notice [notice_no=" + notice_no + ", notice_id=" + notice_id + ", notice_title=" + notice_title
				+ ", notice_content=" + notice_content + ", notice_date=" + notice_date + ", notice_time=" + notice_time
				+ "]";
	}
	
}
