package com.ssafy.repository;

import java.util.List;
import org.springframework.stereotype.Repository;
import com.ssafy.domain.Situation;

@Repository
public interface SituationRepository {
	List<Situation> selectReportStatus0ThisYear() throws Exception;

	List<Situation> selectReportStatus1ThisYear() throws Exception;

	List<Situation> selectReportStatus2ThisYear() throws Exception;
	
	List<Situation> allCnt() throws Exception;

	List<Situation> selectByUserReportStatus0ThisYear(int userno) throws Exception;

	List<Situation> selectByUserReportStatus1ThisYear(int userno) throws Exception;

	List<Situation> selectByUserReportStatus2ThisYear(int userno) throws Exception;
	
	List<Situation> userCnt(int userno) throws Exception;
}
