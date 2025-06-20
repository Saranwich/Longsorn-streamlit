import whisper
from pathlib import Path  # 1. Import Path เข้ามา

# --- เลือกขนาดโมเดล ---  มีให้เลือก: "tiny", "base", "small", "medium", "large"
# (ส่วนนี้เหมือนเดิม)
MODEL_SIZE = "large"

# --- ระบุไฟล์เสียง (แบบมือโปร) ---
# 2. สร้าง Path แบบกันกระสุน
# Path(__file__) คือ path ของไฟล์ .py นี้แบบเต็มๆ
# .parent คือการบอกให้ไปที่โฟลเดอร์ที่ไฟล์นี้อยู่
# แล้วค่อยต่อด้วย / "assets" / "test_whisper.mp3"
try:
    script_dir = Path(__file__).parent
    audio_file_path = script_dir / "assets" / "test_whisper.mp3"
except NameError:
    # ถ้าเกิดรันในโหมด interactive ที่ไม่มี __file__ ให้ใช้ path ปัจจุบันแทน
    audio_file_path = Path("assets") / "test_whisper.mp3"


# --- เพิ่มโค้ดสำหรับ Debug ---
# เราจะพิมพ์ข้อมูลเพื่อตรวจสอบก่อนที่โปรแกรมจะเริ่มทำงานจริง
print("-" * 30)
print(f"DEBUG: Path ที่โปรแกรมสร้างขึ้นคือ: {audio_file_path.resolve()}")
print(f"DEBUG: Path นี้มีอยู่จริงหรือไม่? -> {audio_file_path.exists()}")
print("-" * 30)



try:
    print(f"กำลังโหลดโมเดล Whisper ขนาด '{MODEL_SIZE}'...")
    print("(ครั้งแรกอาจมีการดาวน์โหลดไฟล์โมเดลจากเน็ต โปรดรอ...)")
    
    # โหลดโมเดลเข้ามาในหน่วยความจำ
    model = whisper.load_model(MODEL_SIZE)

    print("-" * 20)
    print("✅ โหลดโมเดลสำเร็จ!")
    print(f"▶️ เริ่มการถอดเสียงไฟล์: {audio_file_path}")
    print("‼️  ขั้นตอนนี้จะนานมากกกกก... หน้าจออาจจะนิ่งไปเลย ไม่ต้องตกใจนะ!")
    print("‼️  ไปชงกาแฟ หาอะไรทำรอได้เลย... (15-20 นาที หรือมากกว่า)")
    print("-" * 20)
    
    # สั่งให้โมเดลเริ่มทำงานถอดเสียง
    result = model.transcribe(str(audio_file_path), fp16=False)

    # พิมพ์ผลลัพธ์
    print("🎉🎉🎉 ถอดเสียงสำเร็จแล้ว! 🎉🎉🎉")
    print("ข้อความที่ได้คือ:")
    print(result["text"])

except FileNotFoundError:
    print(f"❌ Error: ไม่พบไฟล์เสียงที่ path นี้ '{audio_file_path}'")

except Exception as e:
    print(f"❌ เกิดข้อผิดพลาดที่ไม่คาดคิด: {e}")