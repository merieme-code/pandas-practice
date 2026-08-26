import time # سنستخدم هذه المكتبة لعمل توقف بسيط (pause)

indent = 0 # عدد المسافات في البداية
indent_increasing = True # هل المسافات تزيد أم تنقص؟

try:
    while True: # حلقة لا نهائية لجعل الزيكزاك يتحرك للأبد
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # توقف لمدة 0.1 ثانية لجعل الحركة تبدو ناعمة

        if indent_increasing:
            indent = indent + 1
            if indent == 20: # إذا وصلنا لـ 20 مسافة، نعكس الاتجاه
                indent_increasing = False
        else:
            indent = indent - 1
            if indent == 0: # إذا عدنا للصفر، نعكس الاتجاه مرة أخرى
                indent_increasing = True
except KeyboardInterrupt:
    # هذا استثناء خاص يُطلق عندما تضغطين Ctrl+C لإيقاف البرنامج
    print("\nتم إيقاف برنامج الزيكزاك بنجاح!")

