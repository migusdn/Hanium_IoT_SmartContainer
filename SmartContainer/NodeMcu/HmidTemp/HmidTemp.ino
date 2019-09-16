/*
 * WebSocketClient.ino
 *
 *  Created on: 24.05.2015
 *
 */

#include <Arduino.h>
#include <HTU21D.h>

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266Ping.h>
#include <WebSocketsClient.h>
#include <Arduino_JSON.h>
#include <Hash.h>
HTU21D myHTU21D(HTU21D_RES_RH12_TEMP14);
ESP8266WiFiMulti WiFiMulti;
WebSocketsClient webSocket;
#define DEV_NUM 1
#define RELAY 14
#define USE_SERIAL Serial
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
      JSONVar Obj = JSON.parse(converter(payload));
      if(Obj.hasOwnProperty("message")){
        if(strcmp(Obj["message"], "Request_TempHumid") == 0 || strcmp(Obj["message"], "TempHumid") == 0){
           JSONVar res;
           res["con_type"] = "TempHumid";
           res["type"] = "chat_message";
           res["device_num"] = DEV_NUM;
           res["message"] = "Humidity test";
           res["temp"] = myHTU21D.readTemperature();
           res["humid"] = myHTU21D.readHumidity();
           String SendMsg = JSON.stringify(res);
           webSocket.sendTXT(SendMsg);
        }
        else if(strcmp(Obj["message"], "Request_DoTemp") == 0){
           JSONVar res;
           res["con_type"] = "dotemp";
           res["type"] = "chat_message";
           res["device_num"] = DEV_NUM;
           res["message"] = "dotemptest";
           String SendMsg = JSON.stringify(res);
           webSocket.sendTXT(SendMsg);
           digitalWrite(RELAY, HIGH);
        }
        else if (strcmp(Obj["message"], "Request_UpTemp") == 0){
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
        case WStype_PING:
            // pong will be send automatically
            USE_SERIAL.printf("[WSc] get ping\n");
            break;
        case WStype_PONG:
            // answer to a ping we send
            USE_SERIAL.printf("[WSc] get pong\n");
            break;
    }

}

void setup() {
	// USE_SERIAL.begin(921600);
	USE_SERIAL.begin(115200);
  pinMode(RELAY, OUTPUT);
	//Serial.setDebugOutput(true);
	USE_SERIAL.setDebugOutput(true);

	USE_SERIAL.println();
	USE_SERIAL.println();
	USE_SERIAL.println();
   while (myHTU21D.begin() != true)
  {
    Serial.println(F("HTU21D, SHT21 sensor is faild or not connected")); //(F()) saves string to flash & keeps dynamic memory free
    delay(5000);
  }
  Serial.println(F("HTU21D, SHT21 sensor is active"));


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
    webSocket.begin("yahait.iptime.org", 8000, "/ws/status/temphumid/");
    USE_SERIAL.println("Domain Name cant found");
  }else{
    webSocket.begin("192.168.0.9", 8000, "/ws/status/temphumid/");
    USE_SERIAL.println("USE LOCALIP");
  }
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
