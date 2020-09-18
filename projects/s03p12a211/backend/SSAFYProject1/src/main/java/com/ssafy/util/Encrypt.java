package com.ssafy.util;

public class Encrypt {

    public static void main(String[] args) throws Exception {
        String plainText = "ssafy";
        String key = "211FirstAlgoPro";

        System.out.println("MD5 : " + plainText + " - " + EncryptionEnvironmentPostProcessor.md5(plainText));
        System.out.println("SHA-256 : " + plainText + " - " + EncryptionEnvironmentPostProcessor.sha256(plainText));

        String encrypted = EncryptionEnvironmentPostProcessor.encryptAES256(plainText, key);

        System.out.println("AES-256 : enc - " + encrypted);
        System.out.println("AES-256 : dec - " + EncryptionEnvironmentPostProcessor.decryptAES256(encrypted, key));
    }
}