package com.ssafy.service;

import java.util.List;

import com.ssafy.domain.User;

public interface UserService {
	User login(User user) throws Exception;
	
	List<User> userList() throws Exception;

	User detail(String email) throws Exception;
	
	User detailByNo(int userNo) throws Exception;

	int signUp(User user) throws Exception;

	int modify(User user) throws Exception;

	int remove(String email) throws Exception;
	
	String findEmail(User user) throws Exception;
	
	User findPassword(User user) throws Exception;
}
