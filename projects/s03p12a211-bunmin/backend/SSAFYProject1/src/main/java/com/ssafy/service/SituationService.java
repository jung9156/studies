package com.ssafy.service;

import java.util.List;

import com.ssafy.domain.Situation;

public interface SituationService {
	List<List<Situation>> selectAll() throws Exception;

	List<List<Situation>> selectByUser(int userno) throws Exception;
}
