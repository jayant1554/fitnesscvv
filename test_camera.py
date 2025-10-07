#!/usr/bin/env python3
"""
Camera Test Script
Tests camera functionality and provides diagnostic information
"""

import cv2
import time

def test_camera():
    print("🔍 Camera Diagnostic Tool")
    print("=" * 50)
    
    # Test different camera indices
    working_cameras = []
    for idx in range(5):  # Test indices 0-4
        print(f"\n📷 Testing camera index {idx}...")
        cap = cv2.VideoCapture(idx)
        
        if cap.isOpened():
            ret, frame = cap.read()
            if ret and frame is not None:
                h, w = frame.shape[:2]
                print(f"✅ Camera {idx}: Working! Resolution: {w}x{h}")
                working_cameras.append(idx)
                
                # Test a few frames
                for i in range(5):
                    ret, frame = cap.read()
                    if not ret:
                        print(f"⚠️ Camera {idx}: Frame {i+1} failed")
                        break
                else:
                    print(f"✅ Camera {idx}: All test frames successful")
                    
            else:
                print(f"❌ Camera {idx}: Opens but can't read frames")
        else:
            print(f"❌ Camera {idx}: Failed to open")
            
        cap.release()
        time.sleep(0.1)
    
    print(f"\n📊 Summary:")
    if working_cameras:
        print(f"✅ Working cameras found: {working_cameras}")
        print(f"💡 Use camera index {working_cameras[0]} in your app")
    else:
        print("❌ No working cameras found!")
        print("\n🔧 Troubleshooting:")
        print("1. Check if camera is physically connected")
        print("2. Close other apps using camera (Teams, Zoom, Skype, etc.)")
        print("3. Check Windows Camera privacy settings:")
        print("   Settings > Privacy & Security > Camera")
        print("4. Update camera drivers")
        print("5. Try running as administrator")
        print("6. Restart your computer")
    
    print("=" * 50)

if __name__ == "__main__":
    test_camera()