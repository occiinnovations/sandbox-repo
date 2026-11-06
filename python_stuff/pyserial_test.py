import serial
import time

# Connect to the CH340 interface layer
ser = serial.Serial('COM5', 115200, timeout=5)
time.sleep(3)
ser.read(ser.in_waiting)  # Clear the welcome buffer

print("1. Commanding Auto-Home (G28)...")
print("⚠️ Make sure the bed and print head can hit their limit switches!")
ser.write(b"G28\n")

# Wait patiently for homing to finish completely
while True:
    line = ser.readline().decode('utf-8', errors='ignore').strip()
    if line:
        print(f"[Homing Loop]: {line}")
    if "ok" in line.lower():
        print("✅ Homing sequence complete! Safe bounds established.")
        break
    time.sleep(0.1)

print("\n2. Switching to Relative Mode (G91)...")
ser.write(b"G91\n")
time.sleep(0.1)

print("\n3. Testing physical X-axis displacement (G0 X40 F1500)...")
ser.write(b"G0 X40 F1500\n")

while True:
    line = ser.readline().decode('utf-8', errors='ignore').strip()
    if line:
        print(f"[Movement Loop]: {line}")
    if "ok" in line.lower():
        print("\n🚀 Physical execution complete.")
        break
    time.sleep(0.1)

ser.close()
