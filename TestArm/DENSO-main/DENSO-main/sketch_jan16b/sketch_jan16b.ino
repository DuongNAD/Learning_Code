#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVO_FREQ 50 
int pulseMin = 150; 
int pulseMax = 600; 

// Định nghĩa kênh trên PCA9685
const int CH_BASE     = 0;
const int CH_SHOULDER = 1;
const int CH_ELBOW    = 2;
const int CH_GRIPPER  = 3;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10); 

  pwm.begin();
  pwm.setOscillatorFrequency(27000000);
  pwm.setPWMFreq(SERVO_FREQ);

  // --- SỬA LỖI NGỬA TAY TẠI ĐÂY (SETUP) ---
  // Thay vì 90 hay 10, ta dùng công thức đảo chiều ngay từ đầu
  
  moveServo(CH_BASE,     50); // Tăng dần -> Sang phải
  moveServo(CH_SHOULDER, 50); // Tăng dần -> ngửa lên ( vùng hoạt động hợp lý 0 -> 60)
  moveServo(CH_ELBOW,   20);  // Tăng dần -> cụp xuống ( vùng hoạt động hợp lý 0 -> 60)
  moveServo(CH_GRIPPER,  80); // 85 - khép lại && 30 - mở ra hết cỡ

  Serial.println("Robot Ready - Setup Inversion Fixed");
}

void moveServo(int channel, float angle) {
  angle = constrain(angle, 0, 180);
  int pulse = map(angle, 0, 180, pulseMin, pulseMax);
  pwm.setPWM(channel, 0, pulse);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    
    int bIdx = data.indexOf("B:");
    int sIdx = data.indexOf(",S:");
    int eIdx = data.indexOf(",E:");
    int gIdx = data.indexOf(",G:");

    if (bIdx != -1 && sIdx != -1 && eIdx != -1 && gIdx != -1) {
      float b = data.substring(bIdx + 2, sIdx).toFloat();
      float s = data.substring(sIdx + 3, eIdx).toFloat();
      float e = data.substring(eIdx + 3, gIdx).toFloat();
      int g = data.substring(gIdx + 3).toInt();

      // --- ĐỒNG BỘ LOGIC ĐẢO CHIỀU VỚI SETUP ---
      float fixedBase     = b;
      float fixedShoulder = s;
      float fixedElbow    = e;   
      int   fixedGrip     = g;

      moveServo(CH_BASE,     fixedBase);
      moveServo(CH_SHOULDER, fixedShoulder);
      moveServo(CH_ELBOW,    fixedElbow);
      moveServo(CH_GRIPPER,  fixedGrip);
      
      Serial.print("ACK_FIXED:"); Serial.println(data);
    }
  }
}