package com.ssafy.service;

import java.util.List;

import com.ssafy.domain.Violation;

public interface ViolationService {
	Violation viewViolation(int violationNo, int userNo) throws Exception;

	List<Violation> viewViolationList(int userNo) throws Exception;

	int addViolation(Violation violation) throws Exception;

	int modifyViolation(Violation violation) throws Exception;
	
	int modifyCondition(int violationNo, int userNo, int reportStatus) throws Exception;

	int removeViolation(int violationNo, int userNo) throws Exception;
}
