
Skip to content
This repository

    Pull requests
    Issues
    Marketplace
    Explore

    @bigdiehl

0
0

    0

CapstoneRingo/SUB_TEST
Code
Issues 0
Pull requests 0
Projects 0
Wiki
Insights

Tray Unload Test update from Spencer

    master

@bigdiehl
bigdiehl committed 11 hours ago
1 parent db47446 commit dc8b23da7c3ff377297260a8abe8a391422e0858
Showing
with 41 additions and 11 deletions.
52 RINGO_MACHINGO/TrayUnloadTest.py 100644 → 100755
@@ -1,3 +1,4 @@
+
 #	FILE NAME 		:	TrayUnloadTest.py
 #	AUTHOR 			  : 	Nolan McCulloch
 #	CONTRIBUTORS	: 	Caleb Groves, Spencer Diehl
@@ -64,22 +65,22 @@
 DROP_POS_X  = 350           # mm - position of PCB drop

 TRAY_POS1_Y =  54           # mm - position of first vacuum contact
-DROP_POS_Y  = 178           # mm - position of backing drop
+DROP_POS_Y  = 180          # mm - position of backing drop
 Y_OFFSET    =   8.5         # gain - offset multiplier to calculate position

 CRIT_DELAY = 7              # seconds - maximium travel time delay

 Y_SPEED = 800               # mm / min - speed gantry when removing

-CONTIN_MODE = False
+CONTIN_MODE = True
 DROP_MODE = True            # 1 - drop at location | 0 - drop in out tray
 COMPLETE_FLAG = False       # flag to indicate that all PCB's in output Tray
 END_COUNT = 5

 # DEFINE GLOBALS
-r = RINGO()                 # create and init Machine Object
+#r = RINGO()                 # create and init Machine Object
 count = 0
-currPos = 0
+currPos = 25

 # getCurrentPos()
 #
@@ -206,19 +207,19 @@ def getPCB() :
     # Move to pickup location, grab durring movement
     r.tinyG.write('g0 x' + str(x_pos))
     time.sleep(CRIT_DELAY)
-    r.tinyG.write('g1 F800 y' + str(y_pos))
+    r.tinyG.write('g0 y' + str(y_pos))
     r.head.extend()
-    time.sleep(5 + ((currPos % 25)) / 2)
+    time.sleep(4)
     r.head.grab()
     time.sleep(0.5)

     # Move to drop location - drop PCB
     r.head.retract()
     r.tinyG.write('g0 y' + str(0))
-    time.sleep(3)
+    time.sleep(5)
     r.head.rotateDown()
     r.tinyG.write('g0 x' + str(x_pos_out))
-    time.sleep(CRIT_DELAY)
+    time.sleep(CRIT_DELAY - 1)
     r.tinyG.write('g0 y' + str(y_pos_out))
     time.sleep(4)
     r.head.drop()
@@ -228,17 +229,46 @@ def getPCB() :
     r.head.rollerDown()
     r.jig.extend()
     time.sleep(1)
-    r.tinyG.write('g0 y' + str(y_pos_out - 25))
+    r.tinyG.write('g0 y' + str(y_pos_out - 30))
     time.sleep(2)
     r.tinyG.write('g0 x' + str(x_pos_out + 150))
     time.sleep(4)
     r.head.rollerUp()
+    r.jig.retract()
+    r.head.rotateDown()
+    time.sleep(1)
+
+    # Move to drop location - Pick up PCB
+    r.tinyG.write('g0 x334 y174')
+    time.sleep(3)
+    r.head.extend()
+    r.head.grab()
+    time.sleep(2)
+    r.head.retract()
+
+    # Move to dropoff location
+    r.tinyG.write('g0 y' + str(0))
+    time.sleep(4)
+    r.head.rotateUp()
+    time.sleep(1)
+    r.head.retract()
+    r.tinyG.write('g0 x672')
+    time.sleep(CRIT_DELAY)
+    r.tinyG.write('g0 y48')
+    time.sleep(6)
+    r.head.extend()
+    time.sleep(2)
+    r.head.drop()
+    time.sleep(0.5)
+    r.tinyG.write('g0 y' + str(0))
+    time.sleep(2)
+    r.head.retract()

     # Return to HOME
     r.tinyG.write('g0 y' + str(1))
     time.sleep(2)
-    r.tinyG.write('g0 x' + str(1))
-    time.sleep(CRIT_DELAY + 5)
+    #r.tinyG.write('g0 x' + str(1))
+    #time.sleep(CRIT_DELAY + 5)



0 comments on commit dc8b23d
@bigdiehl

Attach files by dragging & dropping,

, or pasting from the clipboard.
Styling with Markdown is supported

You’re not receiving notifications from this thread.

    © 2018 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help

    Contact GitHub
    API
    Training
    Shop
    Blog
    About

Press h to open a hovercard with more details.
