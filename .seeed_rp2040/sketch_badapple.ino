#include <RP2040_SD.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_GFX.h>
#include <SPI.h>

const uint8_t cs = (28u);
File myFile;
void setup()   {           
  Serial.begin(9600);
  Wire.setClock(400000);
  Wire.begin();
  Adafruit_SSD1306 display(128,64,&Wire,-1);
  if (!SD.begin(cs)) {
    Serial.println("initialization failed!");
    return;
  }else{
    Serial.println("Starting...");
  }

  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.clearDisplay();
  myFile = SD.open("badapple.bin");
  byte buffer[64];
  unsigned char bmpdata[704];
  unsigned int size = 0;
  while (myFile.available()){
    int length = myFile.available();
    if (length > 64){
      length = 64;
    }
    myFile.read(buffer,length);
    if (640>size){
      for (int i = 0;i < 64;i++){
        bmpdata[size + i] = buffer[i];
      }
      size += length;
    }else{
      for (int i = 0;i < 704 - size;i++){
        bmpdata[size + i] = buffer[i];
      }
      display.clearDisplay();
      display.drawBitmap(21,0,bmpdata,86,64,1);
      display.display();
      delay(50);
      for (int i = 0;i < size - 640;i++){
        bmpdata[i] = buffer[704 - size +i];
      }
      size -= 640;
    }
  }
  myFile.close();
  Serial.println("finished!!");
}


void loop() {

}