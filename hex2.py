From 558a1f5affeda4c0508bce2cefb159ab364c4ff1 Mon Sep 17 00:00:00 2001
From: SurachateCPESWU <surachate.frank@gmail.com>
Date: Sat, 11 Apr 2015 13:59:26 +0000
Subject: [PATCH] good

---
 hex.py |   41 +++++++++++++++++++++++++++++++++++------
 1 file changed, 35 insertions(+), 6 deletions(-)

diff --git a/hex.py b/hex.py
index 23c26f3..03e7aad 100644
--- a/hex.py
+++ b/hex.py
@@ -1,8 +1,37 @@
 #!/usr/bin/evm python
+# 11/04/58
+# RGB show color from RGB hex
+import RPi.GPIO as GPIO
+import time
+
+#### Pin led  setup ###
+pin_r=11
+pin_g=12
+pin_b=13
+################
+
+GPIO.setmode(GPIO.BOARD)
+GPIO.setup(pin_r,GPIO.OUT)
+GPIO.setup(pin_g,GPIO.OUT)
+GPIO.setup(pin_b,GPIO.OUT)
+
+r=GPIO.PWM(pin_r,60)
+g=GPIO.PWM(pin_g,60)
+b=GPIO.PWM(pin_b,60)
+
+r.start(100)
+g.start(100)
+b.start(100)
+
 def hex_to_per(input):
-    r="{0:.2f}".format((((int (input[0:2],16))/255)*100))
-    g="{0:.2f}".format((((int (input[2:4],16))/255)*100))
-    b="{0:.2f}".format((((int (input[4:6],16))/255)*100))
-    print(r)
-    print(g)
-    print(b)
+    r_color= float ("{0:.2f}".format((((int (input[0:2],16))/255)*100)))
+    g_color= float ("{0:.2f}".format((((int (input[2:4],16))/255)*100)))
+    b_color= float ("{0:.2f}".format((((int (input[4:6],16))/255)*100)))
+    show(r,r_color)
+    show(g,g_color)
+    show(b,b_color)
+
+def show(pin,color):
+    dc=100-color
+    pin.ChangeDutyCycle(dc)
+
-- 
1.7.10.4

