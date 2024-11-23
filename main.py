import requests
from asposeocr import AsposeOcr
from io import BytesIO
from PIL import Image

# عملکرد برای دانلود تصویر از لینک
def download_image(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        raise Exception("Unable to download image from the URL")

# عملکرد OCR برای خواندن متن از تصویر
def ocr_image_from_url(image_url):
    # دانلود تصویر
    image_data = download_image(image_url)
    
    # تبدیل تصویر به فرمت مورد قبول Aspose
    image = Image.open(image_data)
    image_path = f"temp_image.png"
    image.save(image_path)  # ذخیره به عنوان فایل موقت

    # خواندن متن از تصویر با استفاده از Aspose OCR
    ocr = AsposeOcr()
    result = ocr.recognize_image(image_path)

    # حذف فایل موقت اگر نیاز باشد (در سیستم‌های حساس)
    return result

# لینک تصویر (نمونه)
image_url = 'https://dkstatics-public.digikala.com/digikala-products/e99956a63b18563ab392cef4889675cf2ab556f2_1731945558.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90'

# اجرا و نمایش متن استخراج‌شده
try:
    arabic_text = ocr_image_from_url(image_url)
    print("Extracted Text:")
    print(arabic_text)
except Exception as e:
    print(f"Error: {e}")
