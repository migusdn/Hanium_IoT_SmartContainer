
/*
 * WebSocketClient.ino
 *
 *  Created on: 24.05.2015
 *
 */

#include <Wire.h>
#include "SparkFunHTU21D.h"

HTU21D myHumidity;


#include <Arduino.h>

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>

#include <WebSocketsClient.h>
#include <Arduino_JSON.h>
#include <Hash.h>

ESP8266WiFiMulti WiFiMulti;
WebSocketsClient webSocket;

#define USE_SERIAL Serial
JSONVar myObj;
String converter(uint8_t *str){
    return String((char *)str);
}
void webSocketEvent(WStype_t type, uint8_t * payload, size_t length) {

	switch(type) {
		case WStype_DISCONNECTED:
			USE_SERIAL.printf("[WSc] Disconnected!\n");
			break;
		case WStype_CONNECTED: {
			USE_SERIAL.printf("[WSc] Connected to url: %s\n", payload);
			// send message to server when Connected
			//webSocket.sendTXT("Connected");
		}
			break;
		case WStype_TEXT:{
			USE_SERIAL.printf("[WSc] get text: %s\n", payload);
      USE_SERIAL.printf("%s",myHumidity.readHumidity());
      USE_SERIAL.printf("text msg parsing");
      JSONVar Obj = JSON.parse(converter(payload));
      if(Obj.hasOwnProperty("message")){
        if(strcmp(Obj["message"], "Request_TempHumid") || strcmp(Obj["message"], "TempHumid")){
           JSONVar res;
           res["con_type"] = "TempHumid";
           res["type"] = "chat_message";
           res["message"] = "Humidity test";
           res["temp"] = myHumidity.readTemperature();
           res["humid"] = myHumidity.readHumidity();
           String SendMsg = JSON.stringify(res);
           webSocket.sendTXT(SendMsg);
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
	}

}

void setup() {
	// USE_SERIAL.begin(921600);
  myHumidity.begin();
	USE_SERIAL.begin(115200);

	//Serial.setDebugOutput(true);
	USE_SERIAL.setDebugOutput(true);

	USE_SERIAL.println();
	USE_SERIAL.println();
	USE_SERIAL.println();

	for(uint8_t t = 4; t > 0; t--) {
		USE_SERIAL.printf("[SETUP] BOOT WAIT %d...\n", t);
		USE_SERIAL.flush();
		delay(1000);
	}

	WiFiMulti.addAP("K_iptime", "12345678");

	//WiFi.disconnect();
	while(WiFiMulti.run() != WL_CONNECTED) {
		delay(100);
	}

	// server address, port and URL
	webSocket.begin("192.168.0.11", 8000, "/ws/status/00001/");

	// event handler
	webSocket.onEvent(webSocketEvent);

	// use HTTP Basic Authorization this is optional remove if not needed
	//webSocket.setAuthorization("user", "Password");

	// try ever 5000 again if connection has failed
	webSocket.setReconnectInterval(5000);
  
  // start heartbeat (optional)
  // ping server every 15000 ms
  // expect pong from server within 3000 ms
  // consider connection disconnected if pong is not received 2 times
  webSocket.enableHeartbeat(15000, 3000, 2);

}

void loop() {
	webSocket.loop();
}
