/*
 * WebSocketClient.ino
 *
 *  Created on: 24.05.2015
 *
 */

#include <Arduino.h>

#include <WiFi.h>
#include <WiFiMulti.h>
#include <WiFiClientSecure.h>
#include <Arduino_JSON.h>
#include <WebSocketsClient.h>
#include <ESP32Ping.h>


WiFiMulti WiFiMulti;
WebSocketsClient webSocket;
#define DEV_NUM 6
#define RELAY 23 // D5
#define USE_SERIAL Serial

String converter(uint8_t *str){
    return String((char *)str);
}

void hexdump(const void *mem, uint32_t len, uint8_t cols = 16) {
	const uint8_t* src = (const uint8_t*) mem;
	USE_SERIAL.printf("\n[HEXDUMP] Address: 0x%08X len: 0x%X (%d)", (ptrdiff_t)src, len, len);
	for(uint32_t i = 0; i < len; i++) {
		if(i % cols == 0) {
			USE_SERIAL.printf("\n[0x%08X] 0x%08X: ", (ptrdiff_t)src, i);
		}
		USE_SERIAL.printf("%02X ", *src);
		src++;
	}
	USE_SERIAL.printf("\n");
}

void webSocketEvent(WStype_t type, uint8_t * payload, size_t length) {

	switch(type) {
		case WStype_DISCONNECTED:
			USE_SERIAL.printf("[WSc] Disconnected!\n");
			break;
		case WStype_CONNECTED:
			USE_SERIAL.printf("[WSc] Connected to url: %s\n", payload);

			// send message to server when Connected
			// webSocket.sendTXT("Connected");
			break;
		case WStype_TEXT:{
     USE_SERIAL.printf("[WSc] get text: %s\n", payload);
     JSONVar Obj = JSON.parse(converter(payload));
      if(Obj.hasOwnProperty("message")){
        if(strcmp(Obj["message"], "Request_UpTemp") == 0){
           JSONVar res;
           res["con_type"] = "uptemp";
           res["type"] = "chat_message";
           res["device_num"] = DEV_NUM;
           res["message"] = "uptemp test";
           String SendMsg = JSON.stringify(res);
           webSocket.sendTXT(SendMsg);
           digitalWrite(RELAY, HIGH);
        }
        else if (strcmp(Obj["message"], "Request_DoTemp") == 0){
          digitalWrite(RELAY, LOW);
        }
      }
      // send message to server
      // webSocket.sendTXT("message here");
      break;
    }
		case WStype_BIN:
			USE_SERIAL.printf("[WSc] get binary length: %u\n", length);
			hexdump(payload, length);

			// send data to server
			// webSocket.sendBIN(payload, length);
			break;
		case WStype_ERROR:			
		case WStype_FRAGMENT_TEXT_START:
		case WStype_FRAGMENT_BIN_START:
		case WStype_FRAGMENT:
		case WStype_FRAGMENT_FIN:
			break;
	}

}

void setup() {
	// USE_SERIAL.begin(921600);
	USE_SERIAL.begin(115200);

	//Serial.setDebugOutput(true);
	USE_SERIAL.setDebugOutput(true);
  pinMode(RELAY, OUTPUT);
	USE_SERIAL.println();
	USE_SERIAL.println();
	USE_SERIAL.println();

	for(uint8_t t = 4; t > 0; t--) {
		USE_SERIAL.printf("[SETUP] BOOT WAIT %d...\n", t);
		USE_SERIAL.flush();
		delay(1000);
	}
  WiFiMulti.addAP("K_iptime", "12345678");

  WiFi.disconnect();
  while(WiFiMulti.run() != WL_CONNECTED) {
    delay(100);
  }
  bool ping_res = Ping.ping("yahait.iptime.org");
  // server address, port and URL
  if(ping_res){
    webSocket.begin("yahait.iptime.org", 8000, "/ws/status/uptemp/");
    USE_SERIAL.println("Domain Name cant found");
  }else{
    webSocket.begin("192.168.0.9", 8000, "/ws/status/uptemp/");
    USE_SERIAL.println("USE LOCALIP");
  }
	// event handler
	webSocket.onEvent(webSocketEvent);

	// use HTTP Basic Authorization this is optional remove if not needed
	webSocket.setAuthorization("user", "Password");

	// try ever 5000 again if connection has failed
	webSocket.setReconnectInterval(5000);

}

void loop() {
	webSocket.loop();
}
