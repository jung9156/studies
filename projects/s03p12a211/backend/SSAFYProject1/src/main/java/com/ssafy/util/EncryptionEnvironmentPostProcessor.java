package com.ssafy.util;

import java.nio.ByteBuffer;
import java.security.AlgorithmParameters;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.Base64;
import java.util.Properties;

import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.env.EnvironmentPostProcessor;
import org.springframework.core.env.ConfigurableEnvironment;
import org.springframework.core.env.PropertiesPropertySource;

public class EncryptionEnvironmentPostProcessor implements EnvironmentPostProcessor {
    private final Logger logger = LoggerFactory.getLogger(EnvironmentPostProcessor.class);
    static final String key = "211FirstAlgoPro";
    
    @Override
    public void postProcessEnvironment(ConfigurableEnvironment environment, SpringApplication application) {
        Properties props = new Properties();
        try {
            props.put("spring.datasource.password", decryptAES256(environment.getProperty("spring.datasource.password"),key));
            props.put("spring.datasource.username", decryptAES256(environment.getProperty("spring.datasource.username"),key));
        } catch (Exception e) { logger.error("Fail decrypt datasource info", e); }
        environment.getPropertySources().addFirst(new PropertiesPropertySource("myProps", props));
    }
 
  public static String md5(String msg) throws NoSuchAlgorithmException {
	    MessageDigest md = MessageDigest.getInstance("MD5");
	    md.update(msg.getBytes());
	    return byteToHexString(md.digest());
	}

	public static String sha256(String msg)  throws NoSuchAlgorithmException {
	    MessageDigest md = MessageDigest.getInstance("SHA-256");
	    md.update(msg.getBytes());
	    return byteToHexString(md.digest());
	}

	public static String byteToHexString(byte[] data) {
	    StringBuilder sb = new StringBuilder();
	    for(byte b : data) {
	        sb.append(Integer.toString((b & 0xff) + 0x100, 16).substring(1));
	    }
	    return sb.toString();
	}

	public static String encryptAES256(String msg, String key) throws Exception {
	    SecureRandom random = new SecureRandom();
	    byte bytes[] = new byte[20];
	    random.nextBytes(bytes);
	    byte[] saltBytes = bytes;

	    // Password-Based Key Derivation function 2
	    SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA1");

	    // 70000번 해시하여 256 bit 길이의 키를 만든다.
	    PBEKeySpec spec = new PBEKeySpec(key.toCharArray(), saltBytes, 70000, 256);

	    SecretKey secretKey = factory.generateSecret(spec);
	    SecretKeySpec secret = new SecretKeySpec(secretKey.getEncoded(), "AES");

	    // 알고리즘/모드/패딩
	    // CBC : Cipher Block Chaining Mode
	    Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
	    cipher.init(Cipher.ENCRYPT_MODE, secret);
	    AlgorithmParameters params = cipher.getParameters();

	    // Initial Vector(1단계 암호화 블록용)
	    byte[] ivBytes = params.getParameterSpec(IvParameterSpec.class).getIV();
	    byte[] encryptedTextBytes = cipher.doFinal(msg.getBytes("UTF-8"));
	    byte[] buffer = new byte[saltBytes.length + ivBytes.length + encryptedTextBytes.length];
	    System.arraycopy(saltBytes, 0, buffer, 0, saltBytes.length);
	    System.arraycopy(ivBytes, 0, buffer, saltBytes.length, ivBytes.length);
	    System.arraycopy(encryptedTextBytes, 0, buffer, saltBytes.length + ivBytes.length, encryptedTextBytes.length);

	    return Base64.getEncoder().encodeToString(buffer);
	}

	public static String decryptAES256(String msg, String key) throws Exception {
	    Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
	    ByteBuffer buffer = ByteBuffer.wrap(Base64.getDecoder().decode(msg));

	    byte[] saltBytes = new byte[20];
	    buffer.get(saltBytes, 0, saltBytes.length);
	    
	    byte[] ivBytes = new byte[cipher.getBlockSize()];
	    buffer.get(ivBytes, 0, ivBytes.length);
	    
	    byte[] encryoptedTextBytes = new byte[buffer.capacity() - saltBytes.length - ivBytes.length];
	    buffer.get(encryoptedTextBytes);
	    
	    SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA1");
	    PBEKeySpec spec = new PBEKeySpec(key.toCharArray(), saltBytes, 70000, 256);
	    SecretKey secretKey = factory.generateSecret(spec);
	    SecretKeySpec secret = new SecretKeySpec(secretKey.getEncoded(), "AES");
	    
	    cipher.init(Cipher.DECRYPT_MODE, secret, new IvParameterSpec(ivBytes));
	    byte[] decryptedTextBytes = cipher.doFinal(encryoptedTextBytes);

	    return new String(decryptedTextBytes);
	}
}
