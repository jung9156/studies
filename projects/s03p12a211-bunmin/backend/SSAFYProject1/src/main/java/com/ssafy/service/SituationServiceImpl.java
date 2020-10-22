package com.ssafy.service;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.ssafy.domain.Situation;
import com.ssafy.repository.SituationRepository;

@Service
public class SituationServiceImpl implements SituationService {
	
	@Autowired
	SituationRepository repo;
	
	@Override
	public List<List<Situation>> selectAll() throws Exception {
		List<List<Situation>> listAll = new ArrayList<List<Situation>>();

		listAll.add(repo.selectReportStatus0ThisYear());
		listAll.add(repo.selectReportStatus1ThisYear());
		listAll.add(repo.selectReportStatus2ThisYear());
		listAll.add(repo.allCnt());
		
		return listAll;
	}
	
	@Override
	public List<List<Situation>> selectByUser(int userno) throws Exception {
		List<List<Situation>> listUser = new ArrayList<List<Situation>>();

		listUser.add(repo.selectByUserReportStatus0ThisYear(userno));
		listUser.add(repo.selectByUserReportStatus1ThisYear(userno));
		listUser.add(repo.selectByUserReportStatus2ThisYear(userno));
		listUser.add(repo.userCnt(userno));	
	
		return listUser;
	}
}
