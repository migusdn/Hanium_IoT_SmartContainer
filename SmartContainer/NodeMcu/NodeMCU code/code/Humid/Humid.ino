/*
 * WebSocketClient.ino
 *
 *  Created on: 24.05.2015
 *
 */

#include <Arduino.h>

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <Arduino_JSON.h>
#include <WebSocketsClient.h>

#include <Hash.h>

#include <HTU21D.h>
ESP8266WiFiMulti WiFiMulti;
WebSocketsClient webSocket;
#define USE_SERIAL Serial
#define DEVICE_NUM 00001

HTU21D HTU(HTU21D_RES_RH12_TEMP14);



// Send the HTU21D Sensor data
void sendData(){
  JSONVar Data;
  Data["device_num"] = DEVICE_NUM;
  Data["message"] = "abc";
  String jsonString = JSON.stringify(Data);
  webSocket.sendTXT(jsonString);
  USE_SERIAL.println(jsonString);
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
		case WStype_TEXT:
			USE_SERIAL.printf("[WSc] get text: %s\n", payload);

			// send message to server
      //sendData();
      //Serial.print(F("Humidity............: ")); Serial.print(HTU.readHumidity());            Serial.println(F(" +-2%"));
			break;
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
	//USE_SERIAL.begin(921600);
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

	WiFiMulti.addAP("linksys", "");

	//WiFi.disconnect();
	while(WiFiMulti.run() != WL_CONNECTED) {
		delay(100);
	}
	// HTU21D sensor Setup
  while (HTU.begin() != true)
  {
    USE_SERIAL.println(F("HTU21D, SHT21 sensor is faild or not connected")); //(F()) saves string to flash & keeps dynamic memory free
    delay(5000);
  }
  USE_SERIAL.println(F("HTU21D, SHT21 sensor is active"));

	// server address, port and URL
	webSocket.begin("192.168.1.101", 8000, "/ws/status/1/");

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
