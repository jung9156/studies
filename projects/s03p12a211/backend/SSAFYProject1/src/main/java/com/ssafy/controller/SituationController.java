package com.ssafy.controller;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.ssafy.domain.Situation;
import com.ssafy.service.SituationService;

import io.swagger.annotations.ApiOperation;

@CrossOrigin(origins = { "*" }, maxAge = 6000)
@RestController
@RequestMapping("api/situation")
public class SituationController {
	private static final Logger logger = LoggerFactory.getLogger(NoticeController.class);
	
	@Autowired
	SituationService service;

    @ApiOperation(value = "모든 사용자들의 정보들를 반환한다.", response = List.class)
	@GetMapping
	public ResponseEntity<List<List<Situation>>> retrieveSituation() throws Exception {
		logger.debug("retrieveSituation - 호출");
		return new ResponseEntity<List<List<Situation>>>(service.selectAll(), HttpStatus.OK);
	}
    
    @ApiOperation(value = "개인 사용자의 정보들을 반환한다.", response = List.class)    
	@GetMapping("{userno}")
	public ResponseEntity<List<List<Situation>>> detailSituation(@PathVariable int userno) throws Exception {
		logger.debug("retrieveUserSituation - 호출");
		return new ResponseEntity<List<List<Situation>>>(service.selectByUser(userno), HttpStatus.OK);
	}
}
