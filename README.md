# Admin Page Finder

**Admin Page Finder** is a simple Python tool that checks a target website against a wordlist of common admin panel paths.  
For each tested URL, it prints the HTTP status code and saves all successful (HTTP 200) matches to a file.

## Features
- Displays a banner and progress logs
- Loads paths from `wordlist.txt`
- Tests each path on the target URL
- Detects likely admin pages (HTTP `200`)
- Saves results to `goods.txt`

## Disclaimer
Use this tool **only** on websites you own or have explicit permission to test.  
Unauthorized scanning may be illegal and harmful.

## Requirements
- Python 3.x
- `requests`
- `colorama`

## Installation
```bash
pip install requests colorama
```
Usage
Prepare your wordlist:

Edit or replace wordlist.txt with paths you want to test (one path per line).
Lines starting with # or empty lines are ignored.
Leading / is automatically handled.
Run the script:

bash
python main.py
Enter the target URL when prompted, for example:
text
enter target url : https://example.com
Results:
Successful URLs (HTTP 200) are printed to the console
They are saved in:
./goods.txt
Output
Console logs show each tested URL and its HTTP status code.
If matches are found, you’ll see:
[+] Found N possible admin page(s)
If none are found, you’ll see:
[-] We couldn't find any admin pages.
Project Files
main.py — Main Python script
wordlist.txt — List of paths to test
goods.txt — Output file created after running (only when matches exist)
Example wordlist.txt
txt
/admin
/admin/login
/adminpanel
# comment line








# جستجوگر صفحه ادمین

**Admin Page Finder** یک ابزار ساده‌ی پایتون است که یک وب‌سایت هدف را با استفاده از یک لیست کلمات/مسیرهای رایج بررسی می‌کند تا صفحات احتمالی ادمین پنل را پیدا کند.  
برای هر URL تست‌شده، کد وضعیت HTTP را چاپ می‌کند و در صورت موفقیت (HTTP 200) خروجی‌ها را داخل یک فایل ذخیره می‌کند.

## ویژگی‌ها
- نمایش بنر و لاگ‌های اجرای برنامه
- خواندن مسیرها از فایل `wordlist.txt`
- تست کردن هر مسیر روی URL هدف
- شناسایی URL های احتمالی ادمین (در صورت پاسخ HTTP `200`)
- ذخیره نتایج موفق در فایل `goods.txt`

## هشدار و مسئولیت
این ابزار فقط باید **در سیستم خودتان** یا با **اجازه‌ی صریح و کتبی** برای تست استفاده شود.  
تست بدون مجوز ممکن است از نظر قانونی و امنیتی مشکل‌ساز باشد.

## پیش‌نیازها
- Python 3.x
- `requests`
- `colorama`

## نصب
# جستجوگر صفحه ادمین

**Admin Page Finder** یک ابزار ساده‌ی پایتون است که یک وب‌سایت هدف را با استفاده از یک لیست کلمات/مسیرهای رایج بررسی می‌کند تا صفحات احتمالی ادمین پنل را پیدا کند.  
برای هر URL تست‌شده، کد وضعیت HTTP را چاپ می‌کند و در صورت موفقیت (HTTP 200) خروجی‌ها را داخل یک فایل ذخیره می‌کند.

## ویژگی‌ها
- نمایش بنر و لاگ‌های اجرای برنامه
- خواندن مسیرها از فایل `wordlist.txt`
- تست کردن هر مسیر روی URL هدف
- شناسایی URL های احتمالی ادمین (در صورت پاسخ HTTP `200`)
- ذخیره نتایج موفق در فایل `goods.txt`

## هشدار و مسئولیت
این ابزار فقط باید **در سیستم خودتان** یا با **اجازه‌ی صریح و کتبی** برای تست استفاده شود.  
تست بدون مجوز ممکن است از نظر قانونی و امنیتی مشکل‌ساز باشد.

## پیش‌نیازها
- Python 3.x
- `requests`
- `colorama`

## نصب
```bash
pip install requests colorama

pip install requests colorama
```

نحوه استفاده
فایل کلمات مسیر را آماده کنید:

فایل wordlist.txt را ویرایش کنید و مسیرهایی که می‌خواهید تست شوند را قرار دهید (هر خط یک مسیر).
خطوط خالی و خطوطی که با # شروع می‌شوند نادیده گرفته می‌شوند.
اگر مسیر با / شروع شود، برنامه آن را مدیریت می‌کند.
اجرا کردن برنامه:

bash
python main.py
آدرس سایت را وارد کنید (وقتی برنامه درخواست می‌کند):
text
enter target url : https://example.com
خروجی‌ها:
URL های موفق (HTTP 200) در کنسول چاپ می‌شوند
در مسیر زیر ذخیره می‌شوند:
./goods.txt
خروجی برنامه
لاگ کنسول نشان می‌دهد هر URL تست شده و کد وضعیت آن چه بوده است.
اگر نتیجه‌ای پیدا شود، پیام زیر را می‌بینید:
[+] Found N possible admin page(s)
اگر چیزی پیدا نشود:
[-] We couldn't find any admin pages.
فایل‌های پروژه
main.py — فایل اصلی اسکریپت پایتون
wordlist.txt — لیست مسیرهایی که تست می‌شوند
goods.txt — فایل خروجی که بعد از اجرای موفق ایجاد می‌شود (فقط وقتی نتیجه‌ای پیدا شود)
