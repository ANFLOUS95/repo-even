#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
خادم تشغيل محلي لتطبيق «محفوظي» لتتبع استظهار السور المقررة
يقوم بتشغيل خادم HTTP محلي بسيط وسريع يتيح فتح التطبيق في المتصفح
أو عبر الشبكة المحلية (Wi-Fi) من هاتف الأستاذ أو حاسوبه الشخصي.
كما يمكن تشغيل التطبيق مباشرة بفتح ملف index.html في أي متصفح دون الحاجة لأي خادم.
"""

import http.server
import socketserver
import os
import webbrowser

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == '__main__':
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print("=" * 60)
        print("  منظومة «محفوظي» لتتبع استظهار السور المقررة تعمل بنجاح  ")
        print(f"  الرابط المحلي: {url}")
        print("=" * 60)
        print("  اضغط Ctrl+C لإيقاف الخادم في أي وقت")
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nتم إيقاف الخادم بنجاح.")
