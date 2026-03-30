import os

import sys

import platform

import subprocess

import tempfile

import time

import random

import requests

import warnings

from pathlib import Path

import speech\_recognition as sr

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected\_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

from webdriver\_manager.chrome import ChromeDriverManager

warnings.filterwarnings("ignore")

\# ================== FFmpeg Support ==================

def get\_ffmpeg\_path():

if getattr(sys, 'frozen', False):

base\_dir = os.path.dirname(sys.executable)

else:

base\_dir = os.path.dirname(os.path.abspath(\_\_file\_\_))

system = platform.system().lower()

ffmpeg\_name = "ffmpeg.exe" if system == "windows" else "ffmpeg"

possible\_paths = \[

os.path.join(base\_dir, ffmpeg\_name),

os.path.join(base\_dir, "ffmpeg", ffmpeg\_name),

os.path.join(base\_dir, "bin", ffmpeg\_name),

os.path.join(base\_dir, "ffmpeg", "bin", ffmpeg\_name),

os.path.join(base\_dir, "ffmpeg-8.0", "bin", ffmpeg\_name), # hỗ trợ thêm thư mục bạn có

\]

for path in possible\_paths:

if os.path.exists(path):

print(f"✅ Sử dụng ffmpeg local: {".../" + "/".join(Path(path).parts\[-4:\])}")

return path

print("⚠️ Không tìm thấy ffmpeg local, thử dùng từ PATH...")

return "ffmpeg"

def check\_ffmpeg():

ffmpeg\_path = get\_ffmpeg\_path()

try:

result = subprocess.run(\[ffmpeg\_path, "-version"\], capture\_output=True, text=True, timeout=5)

return result.returncode == 0, ffmpeg\_path

except Exception:

return False, None

def convert\_audio\_to\_wav(audio\_file\_path, output\_wav\_path):

has\_ffmpeg, ffmpeg\_path = check\_ffmpeg()

if not has\_ffmpeg:

raise Exception("Không tìm thấy ffmpeg")

cmd = \[ffmpeg\_path, "-y", "-i", audio\_file\_path,

"-ar", "16000", "-ac", "1", "-c:a", "pcm\_s16le",

"-loglevel", "error", output\_wav\_path\]

result = subprocess.run(cmd, capture\_output=True, text=True)

if result.returncode != 0:

raise Exception(f"FFmpeg error: {result.stderr}")

\# ================== Transcribe ==================

def transcribe(url, language="en-US"):

temp\_audio, temp\_wav = None, None

try:

with tempfile.NamedTemporaryFile(suffix=".webm", delete=False) as f:

temp\_audio = f.name

r = requests.get(url, timeout=20)

r.raise\_for\_status()

f.write(r.content)

if os.path.getsize(temp\_audio) < 1024:

raise Exception("File audio quá nhỏ")

with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as wf:

temp\_wav = wf.name

convert\_audio\_to\_wav(temp\_audio, temp\_wav)

rec = sr.Recognizer()

with sr.AudioFile(temp\_wav) as src:

rec.adjust\_for\_ambient\_noise(src, duration=0.5)

audio = rec.record(src)

text = rec.recognize\_google(audio, language=language)

return text.strip()

finally:

for f in \[temp\_audio, temp\_wav\]:

if f and os.path.exists(f):

try: os.remove(f)

except: pass

\# ================== CAPTCHA Helpers ==================

def check\_captcha(driver):

try:

time.sleep(2)

captcha\_indicators = \[

"iframe\[src\*='recaptcha'\]",

"#captcha-form",

".g-recaptcha",

"\[action\*='sorry'\]",

".rc-imageselect",

".rc-audiochallenge"

\]

for indicator in captcha\_indicators:

elements = driver.find\_elements(By.CSS\_SELECTOR, indicator)

if elements:

if "recaptcha" in indicator and "iframe" in indicator:

iframes = driver.find\_elements(By.TAG\_NAME, "iframe")

for iframe in iframes:

src = iframe.get\_attribute("src") or ""

if "recaptcha" in src:

if "anchor" in src:

return True, "iframe\_checkbox"

elif "bframe" in src:

return True, "iframe\_challenge"

return True, "html\_captcha"

page\_title = driver.title.lower()

if "unusual traffic" in page\_title or "sorry" in page\_title:

return True, "google\_sorry"

except Exception as e:

print(f"❌ Lỗi khi kiểm tra CAPTCHA: {e}")

return False, None

def click\_checkbox(driver, max\_retries=3):

for attempt in range(max\_retries):

try:

driver.switch\_to.default\_content()

iframes = driver.find\_elements(By.TAG\_NAME, "iframe")

for iframe in iframes:

src = iframe.get\_attribute("src") or ""

if "recaptcha" in src and "anchor" in src:

driver.switch\_to.frame(iframe)

checkbox = WebDriverWait(driver, 10).until(

EC.element\_to\_be\_clickable((By.ID, "recaptcha-anchor"))

)

time.sleep(random.uniform(1, 2))

checkbox.click()

driver.switch\_to.default\_content()

return True

except Exception:

driver.switch\_to.default\_content()

if attempt < max\_retries - 1:

time.sleep(2)

return False

def request\_audio\_version(driver, max\_retries=3):

for attempt in range(max\_retries):

try:

driver.switch\_to.default\_content()

time.sleep(3)

iframes = driver.find\_elements(By.TAG\_NAME, "iframe")

challenge\_iframe = None

for iframe in iframes:

src = iframe.get\_attribute("src") or ""

title = iframe.get\_attribute("title") or ""

if ("recaptcha" in src and "bframe" in src) or "recaptcha challenge" in title.lower():

challenge\_iframe = iframe

break

if not challenge\_iframe:

if attempt < max\_retries - 1:

time.sleep(2)

continue

else:

raise Exception("Không tìm thấy iframe chứa reCAPTCHA challenge")

driver.switch\_to.frame(challenge\_iframe)

audio\_button = WebDriverWait(driver, 15).until(

EC.element\_to\_be\_clickable((By.ID, "recaptcha-audio-button"))

)

time.sleep(random.uniform(1, 2))

audio\_button.click()

return True

except Exception:

driver.switch\_to.default\_content()

if attempt < max\_retries - 1:

time.sleep(3)

raise Exception("Không thể request audio version sau nhiều lần thử")

\# ================== Solve CAPTCHA ==================

def solve\_audio\_captcha(driver, language="en-US"):

audio\_element = WebDriverWait(driver, 15).until(

EC.presence\_of\_element\_located((By.ID, "audio-source"))

)

audio\_src = audio\_element.get\_attribute("src")

if not audio\_src:

raise Exception("Không tìm thấy audio source")

print(f"🎧 Tải audio từ: {audio\_src}")

text = transcribe(audio\_src, language=language)

print(f"📤 Kết quả nhận dạng: '{text}'")

response = driver.find\_element(By.ID, "audio-response")

response.clear()

response.send\_keys(text)

driver.find\_element(By.ID, "recaptcha-verify-button").click()

print("✅ Đã submit kết quả")

def solve\_captcha\_complete(driver, max\_retries=3, language="en-US", keyword=""):

for attempt in range(max\_retries):

try:

print(f"🔄 Lần thử {attempt+1}/{max\_retries} cho keyword: {keyword}")

has\_captcha, captcha\_type = check\_captcha(driver)

if not has\_captcha:

print("✅ Không có CAPTCHA")

return True

print(f"🛡️ CAPTCHA loại: {captcha\_type}")

if captcha\_type == "iframe\_checkbox":

if not click\_checkbox(driver):

raise Exception("Không click được checkbox")

time.sleep(random.uniform(2, 4))

request\_audio\_version(driver)

time.sleep(random.uniform(1, 3))

solve\_audio\_captcha(driver, language=language)

time.sleep(random.uniform(2, 5))

print("✅ CAPTCHA solved successfully!")

return True

else:

print(f"⚠️ CAPTCHA type không hỗ trợ: {captcha\_type}")

return False

except Exception as e:

print(f"❌ Lỗi lần {attempt+1}: {e}")

if attempt < max\_retries - 1:

time.sleep(random.uniform(3,5))

else:

print("❌ Hết số lần thử")

return False

return False

\# ================== MAIN ==================

if \_\_name\_\_ == "\_\_main\_\_":

print("=" \* 60)

print("🤖 GOOGLE RECAPTCHA SOLVER (FFmpeg version) 🤖")

print("=" \* 60)

\# has\_ffmpeg, ffmpeg\_path = check\_ffmpeg()

\# if not has\_ffmpeg:

\# print("⚠️ Không tìm thấy ffmpeg! Hãy tải và đặt ffmpeg.exe đúng chỗ.")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:

demo\_url = "https://www.google.com/recaptcha/api2/demo"

demo\_url = "https://www.google.com/sorry/index?continue=https://www.google.com/search?q=thay%20k%C3%ADnh%20l%C6%B0ng%20iphone%2013&uule=w+CAIQICIiVGFuIFBodSwgSG8gQ2hpIE1pbmggQ2l0eSwgVmlldG5hbQ&sei=JB3JaPa8JvHl5NoPve24aA&q=EhAqCbrF1GkmRgAAAAAD0AA5GKW6pMYGIjD-rQbpKwd7kHpEIxLBkLmsrwABoN8LmhAV0Z3VIaidYqg141mSvDC\_LD3faZgaI\_EyAVJaAUM"

print(f"📍 Truy cập: {demo\_url}")

driver.get(demo\_url)

time.sleep(2)

success = solve\_captcha\_complete(driver, max\_retries=3, language="en-US", keyword="demo")

if success:

print("\\n🎉 Hoàn thành giải CAPTCHA!")

time.sleep(5)

else:

print("\\n❌ Không thể giải CAPTCHA")

finally:

input("👋 Nhấn Enter để đóng trình duyệt...")

driver.quit()