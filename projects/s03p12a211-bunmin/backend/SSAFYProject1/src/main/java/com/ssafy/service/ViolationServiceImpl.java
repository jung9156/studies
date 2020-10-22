package com.ssafy.service;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.List;

import org.json.JSONArray;
import org.json.JSONObject;
import org.json.JSONTokener;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.domain.Violation;
import com.ssafy.repository.ViolationRepository;

@Service
public class ViolationServiceImpl implements ViolationService {
	
	@Autowired
	ViolationRepository repository;

	@Override
	public Violation viewViolation(int violationNo, int userNo) throws Exception {
		return repository.select(violationNo, userNo);
	}

	@Override
	public List<Violation> viewViolationList(int userNo) throws Exception {
		return repository.selectAll(userNo);
	}

	@Override
	public int addViolation(Violation violation) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String clientId = "jj121pv6s1";
		String clientSecret = "wVqpq3w1PkpJ0S5Qm2IZqHHVKDydoTW7KVq9HM7F";

		String apiURL = "https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc?coords=";
		try {
			apiURL += violation.getLng() + "," + violation.getLat() + "&output=json&orders=addr,admcode,roadaddr";
			URL url = new URL(apiURL);
			HttpURLConnection con = (HttpURLConnection) url.openConnection();
			con.setRequestMethod("GET");
			con.setRequestProperty("X-NCP-APIGW-API-KEY-ID", clientId);
			con.setRequestProperty("X-NCP-APIGW-API-KEY", clientSecret);
			
			int responseCode = con.getResponseCode();
			if(responseCode == 200) br = new BufferedReader(new InputStreamReader(con.getInputStream(), "UTF-8"));
			else br = new BufferedReader(new InputStreamReader(con.getErrorStream(), "UTF-8"));
			
			String line;
			StringBuffer response = new StringBuffer(); // JSON
			while((line = br.readLine()) != null) {
				response.append(line);
			}
			br.close();
			
			JSONTokener tokener = new JSONTokener(response.toString());
			JSONObject object = new JSONObject(tokener);
			
			int status = (int) object.getJSONObject("status").get("code");
			if(status == 0) {
				JSONArray array = object.getJSONArray("results");
				JSONObject addr = null; JSONObject region = null;
				String address = null; String regionRo = ""; String regionNum1 = ""; String regionNum2 = "";

				int size = object.getJSONArray("results").length();
				if(size == 3) { // 도로명 주소가 있을 경우
					addr = object.getJSONArray("results").getJSONObject(2);
					
					regionRo = addr.getJSONObject("land").getString("name");
					regionNum1 = addr.getJSONObject("land").getString("number1");
					
					if(addr.getJSONObject("land").getString("number2").length() > 0)
						regionNum2 = addr.getJSONObject("land").getString("number2");
				} else addr = object.getJSONArray("results").getJSONObject(1); // 도로명 주소가 없을 경우
				region = addr.getJSONObject("region");
				
				String regionDo = region.getJSONObject("area1").getString("name");
				String regionSiGu = region.getJSONObject("area2").getString("name");
				String regionDong = region.getJSONObject("area3").getString("name");
				
				address = regionDo + " " + regionSiGu + " " + regionDong + " " + regionRo + " " + regionNum1 + (regionNum2.length() > 0 ? ("-" + regionNum2) : "");
				address = address.trim();
				
				violation.setAddress(address);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		return repository.insert(violation);
	}

	@Override
	public int modifyViolation(Violation violation) throws Exception {
		return repository.update(violation);
	}
	
	@Override
	public int modifyCondition(int violationNo, int userNo, int reportStatus) throws Exception {
		return repository.updateCondition(violationNo, userNo, reportStatus);
	}

	@Override
	public int removeViolation(int violationNo, int userNo) throws Exception {
		return repository.delete(violationNo, userNo);
	}

}
