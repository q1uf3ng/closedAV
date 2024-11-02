import pyautogui as pg
import time
import os
import sys
import psutil
def check_anti_virus():
    antivirus_info = {
        "火绒": ["HipsTray.exe", "HipsDaemon.exe", "wsctrlsvc.exe"],
        "360": ["360Safe.exe", "360Tray.exe", "360leakfixer.exe", "LiveUpdate360.exe", "ZhuDongFangYu.exe"]
    }
    antivirus_count = {antivirus: 0 for antivirus in antivirus_info.keys()}
    
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            name = proc.info['name']
            for antivirus, processes in antivirus_info.items():
                if name in processes:
                    antivirus_count[antivirus] += 1
                    break  
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    if antivirus_count["火绒"] >= 2 and antivirus_count["360"] >= 2:
        return "360和火绒同时出现"
    elif antivirus_count["火绒"] >= 2:
        return "只有火绒出现"
    elif antivirus_count["360"] >= 2:
        return "只有360出现"
    else:
        return "未找到指定的杀软进程。"


chickd = check_anti_virus()


print(f"当前杀软状态：{chickd}")
def get_windows_version():
    version = sys.getwindowsversion()
    major, minor, build = version.major, version.minor, version.build

    if major == 6 and minor == 1:
        return "Windows 7"
    elif major == 6 and minor == 2:
        return "Windows 8"
    elif major == 6 and minor == 3:
        return "Windows 8.1"
    elif major == 10:
        if build >= 22000:
            return "Windows 11"
        else:
            return "Windows 10"
    elif major == 6 and minor == 2 and build >= 9200:
        return "Windows Server 2012"
    elif major == 10 and build >= 20348:
        return "Windows Server 2022"
    else:
        return "未知的 Windows 版本"

# 获取并输出 Windows 版本
current_version = get_windows_version()
print(f"当前 Windows 版本: {current_version}")


# 获取屏幕尺寸
size = pg.size()
print(f'Size(width={size.width}, height={size.height})')

# 获取当前工作目录
current_dir = os.getcwd()
print(f'Current directory: {current_dir}')

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 构建图像路径
image_paths = {
    'hh': os.path.join(script_dir,  '360_img.png'),
    'exit': os.path.join(script_dir,  '360_exit.png'),
    'eexit': os.path.join(script_dir,  '360_exit2.png'),
    'eeexit': os.path.join(script_dir,  '360_always_always_exit.png'),
    'hr': os.path.join(script_dir,   'hips_img.png'),
    'hr_exit': os.path.join(script_dir,   'exit_img.png'),
    'hr_eexit': os.path.join(script_dir,   'Always_Exit_img.png'),
    'win2012': os.path.join(script_dir,  'win2012.png'),
    'win2022': os.path.join(script_dir,  'win2022.png'),
    'win11white': os.path.join(script_dir,  'win11white.png'),
    'win11black': os.path.join(script_dir,  'win11black.png'),
    'win10white': os.path.join(script_dir,  'win10white.png'),
    'win10black': os.path.join(script_dir,  'win10black.png'),
    'win7': os.path.join(script_dir,  'win7.png')
}
if chickd=="只有火绒出现":
    print("1")
    if current_version == "Windows 7":
            
        
        win10black = image_paths['win7']
        print(f'Checking image path: {win10black}')
        while True:
            try:
                position = pg.locateOnScreen(win10black, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.click(point)
                    print(f'Clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {win10black}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)
        time.sleep(1)
        # 再点击 hh.png 并进行右键点击
        hh_image_path = image_paths['hr']
        print(f'Checking image path: {hh_image_path}')
        while True:
            try:
                position = pg.locateOnScreen(hh_image_path, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.rightClick(point)
                    print(f'Right-clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {hh_image_path}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)
        time.sleep(1)

        # 点击 exit.png
        exit_image_path = image_paths['hr_exit']
        print(f'Checking image path: {exit_image_path}')
        while True:
            try:
                position = pg.locateOnScreen(exit_image_path, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.click(point)
                    print(f'Clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {exit_image_path}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)
        time.sleep(1)
        # 最后点击 eexit.png
        eexit_image_path = image_paths['hr_eexit']
        print(f'Checking image path: {eexit_image_path}')
        while True:
            try:
                position = pg.locateOnScreen(eexit_image_path, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.click(point)
                    print(f'Clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {eexit_image_path}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)


    elif current_version == "Windows 10":
            
        # 先点击 win10black.png
        win10black = image_paths['win10black']
        print(f'Checking image path: {win10black}')
        while True:
            try:
                position = pg.locateOnScreen(win10black, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.click(point)
                    print(f'Clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {win10black}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)
        time.sleep(1)
        # 再点击 hh.png 并进行右键点击
        hh_image_path = image_paths['hr']
        print(f'Checking image path: {hh_image_path}')
        while True:
            try:
                position = pg.locateOnScreen(hh_image_path, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.rightClick(point)
                    print(f'Right-clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {hh_image_path}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)
        time.sleep(1)

        # 点击 exit.png
        exit_image_path = image_paths['hr_exit']
        print(f'Checking image path: {exit_image_path}')
        while True:
            try:
                position = pg.locateOnScreen(exit_image_path, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.click(point)
                    print(f'Clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {exit_image_path}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)
        time.sleep(1)
        # 最后点击 eexit.png
        eexit_image_path = image_paths['hr_eexit']
        print(f'Checking image path: {eexit_image_path}')
        while True:
            try:
                position = pg.locateOnScreen(eexit_image_path, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.click(point)
                    print(f'Clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {eexit_image_path}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)


    elif current_version == "Windows Server 2012":
            
        # 先点击 win10black.png
        win10black = image_paths['win2012']
        print(f'Checking image path: {win10black}')
        while True:
            try:
                position = pg.locateOnScreen(win10black, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.click(point)
                    print(f'Clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {win10black}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)
        time.sleep(1)
        # 再点击 hh.png 并进行右键点击
        hh_image_path = image_paths['hr']
        print(f'Checking image path: {hh_image_path}')
        while True:
            try:
                position = pg.locateOnScreen(hh_image_path, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.rightClick(point)
                    print(f'Right-clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {hh_image_path}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)
        time.sleep(1)

        # 点击 exit.png
        exit_image_path = image_paths['hr_exit']
        print(f'Checking image path: {exit_image_path}')
        while True:
            try:
                position = pg.locateOnScreen(exit_image_path, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.click(point)
                    print(f'Clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {exit_image_path}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)
        time.sleep(1)
        # 最后点击 eexit.png
        eexit_image_path = image_paths['hr_eexit']
        print(f'Checking image path: {eexit_image_path}')
        while True:
            try:
                position = pg.locateOnScreen(eexit_image_path, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.click(point)
                    print(f'Clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {eexit_image_path}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)


    elif current_version == "Windows 11":
            
        # 先点击 win10black.png
        win10black = image_paths['win11white']
        print(f'Checking image path: {win10black}')
        while True:
            try:
                position = pg.locateOnScreen(win10black, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.click(point)
                    print(f'Clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {win10black}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)
        time.sleep(1)
        # 再点击 hh.png 并进行右键点击
        hh_image_path = image_paths['hr']
        print(f'Checking image path: {hh_image_path}')
        while True:
            try:
                position = pg.locateOnScreen(hh_image_path, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.rightClick(point)
                    print(f'Right-clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {hh_image_path}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)
        time.sleep(1)

        # 点击 exit.png
        exit_image_path = image_paths['hr_exit']
        print(f'Checking image path: {exit_image_path}')
        while True:
            try:
                position = pg.locateOnScreen(exit_image_path, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.click(point)
                    print(f'Clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {exit_image_path}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)
        time.sleep(1)
        # 最后点击 eexit.png
        eexit_image_path = image_paths['hr_eexit']
        print(f'Checking image path: {eexit_image_path}')
        while True:
            try:
                position = pg.locateOnScreen(eexit_image_path, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.click(point)
                    print(f'Clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {eexit_image_path}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)





#<--------------------------------------------------------------------------------------------------------->
elif  chickd == "只有360出现":
    if current_version =="Windows 7":
        # 先点击 win10black.png
        win10black = image_paths['win7']
        print(f'Checking image path: {win10black}')
        while True:
            try:
                position = pg.locateOnScreen(win10black, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.click(point)
                    print(f'Clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {win10black}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)
        time.sleep(1)

        # 再点击 360_img.png 并进行右键点击
        hh_image_path = image_paths['hh']
        print(f'Checking image path: {hh_image_path}')
        while True:
            try:
                position = pg.locateOnScreen(hh_image_path, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.rightClick(point)
                    print(f'Right-clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {hh_image_path}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)
        time.sleep(1)

        # 点击 360_exit.png
        exit_image_path = image_paths['exit']
        print(f'Checking image path: {exit_image_path}')
        while True:
            try:
                position = pg.locateOnScreen(exit_image_path, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.click(point)
                    print(f'Clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {exit_image_path}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)
        time.sleep(1)
        # 最后点击 360_exit2.png
        eexit_image_path = image_paths['eexit']
        print(f'Checking image path: {eexit_image_path}')
        while True:
            try:
                position = pg.locateOnScreen(eexit_image_path, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.click(point)
                    print(f'Clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {eexit_image_path}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)
        # 最后点击 360_always_always_exit.png
        eeexit_image_path = image_paths['eeexit']
        print(f'Checking image path: {eeexit_image_path}')
        while True:
            try:
                position = pg.locateOnScreen(eeexit_image_path, grayscale=True, confidence=0.9)
                
                if position is not None:
                    point = pg.center(position)
                    print(f'Image found at: {point}')
                    pg.click(point)
                    print(f'Clicked on image at: {point}')
                    break
                else:
                    print(f'Image not found: {eeexit_image_path}. Retrying...')
                    time.sleep(1)
            except Exception as e:
                print(f'An error occurred: {e}')
                time.sleep(1)


    elif current_version =="Windows 10":
            # 先点击 win10black.png
            win10black = image_paths['win10black']
            print(f'Checking image path: {win10black}')
            while True:
                try:
                    position = pg.locateOnScreen(win10black, grayscale=True, confidence=0.9)
                    
                    if position is not None:
                        point = pg.center(position)
                        print(f'Image found at: {point}')
                        pg.click(point)
                        print(f'Clicked on image at: {point}')
                        break
                    else:
                        print(f'Image not found: {win10black}. Retrying...')
                        time.sleep(1)
                except Exception as e:
                    print(f'An error occurred: {e}')
                    time.sleep(1)
            time.sleep(1)

            # 再点击 360_img.png 并进行右键点击
            hh_image_path = image_paths['hh']
            print(f'Checking image path: {hh_image_path}')
            while True:
                try:
                    position = pg.locateOnScreen(hh_image_path, grayscale=True, confidence=0.9)
                    
                    if position is not None:
                        point = pg.center(position)
                        print(f'Image found at: {point}')
                        pg.rightClick(point)
                        print(f'Right-clicked on image at: {point}')
                        break
                    else:
                        print(f'Image not found: {hh_image_path}. Retrying...')
                        time.sleep(1)
                except Exception as e:
                    print(f'An error occurred: {e}')
                    time.sleep(1)
            time.sleep(1)

            # 点击 360_exit.png
            exit_image_path = image_paths['exit']
            print(f'Checking image path: {exit_image_path}')
            while True:
                try:
                    position = pg.locateOnScreen(exit_image_path, grayscale=True, confidence=0.9)
                    
                    if position is not None:
                        point = pg.center(position)
                        print(f'Image found at: {point}')
                        pg.click(point)
                        print(f'Clicked on image at: {point}')
                        break
                    else:
                        print(f'Image not found: {exit_image_path}. Retrying...')
                        time.sleep(1)
                except Exception as e:
                    print(f'An error occurred: {e}')
                    time.sleep(1)
            time.sleep(1)
            # 最后点击 360_exit2.png
            eexit_image_path = image_paths['eexit']
            print(f'Checking image path: {eexit_image_path}')
            while True:
                try:
                    position = pg.locateOnScreen(eexit_image_path, grayscale=True, confidence=0.9)
                    
                    if position is not None:
                        point = pg.center(position)
                        print(f'Image found at: {point}')
                        pg.click(point)
                        print(f'Clicked on image at: {point}')
                        break
                    else:
                        print(f'Image not found: {eexit_image_path}. Retrying...')
                        time.sleep(1)
                except Exception as e:
                    print(f'An error occurred: {e}')
                    time.sleep(1)
            # 最后点击 360_always_always_exit.png
            eeexit_image_path = image_paths['eeexit']
            print(f'Checking image path: {eeexit_image_path}')
            while True:
                try:
                    position = pg.locateOnScreen(eeexit_image_path, grayscale=True, confidence=0.9)
                    
                    if position is not None:
                        point = pg.center(position)
                        print(f'Image found at: {point}')
                        pg.click(point)
                        print(f'Clicked on image at: {point}')
                        break
                    else:
                        print(f'Image not found: {eeexit_image_path}. Retrying...')
                        time.sleep(1)
                except Exception as e:
                    print(f'An error occurred: {e}')
                    time.sleep(1)


elif current_version =="Windows Server 2012":
            # 先点击 win10black.png
            win10black = image_paths['win2012']
            print(f'Checking image path: {win10black}')
            while True:
                try:
                    position = pg.locateOnScreen(win10black, grayscale=True, confidence=0.9)
                    
                    if position is not None:
                        point = pg.center(position)
                        print(f'Image found at: {point}')
                        pg.click(point)
                        print(f'Clicked on image at: {point}')
                        break
                    else:
                        print(f'Image not found: {win10black}. Retrying...')
                        time.sleep(1)
                except Exception as e:
                    print(f'An error occurred: {e}')
                    time.sleep(1)
            time.sleep(1)

            # 再点击 360_img.png 并进行右键点击
            hh_image_path = image_paths['hh']
            print(f'Checking image path: {hh_image_path}')
            while True:
                try:
                    position = pg.locateOnScreen(hh_image_path, grayscale=True, confidence=0.9)
                    
                    if position is not None:
                        point = pg.center(position)
                        print(f'Image found at: {point}')
                        pg.rightClick(point)
                        print(f'Right-clicked on image at: {point}')
                        break
                    else:
                        print(f'Image not found: {hh_image_path}. Retrying...')
                        time.sleep(1)
                except Exception as e:
                    print(f'An error occurred: {e}')
                    time.sleep(1)
            time.sleep(1)

            # 点击 360_exit.png
            exit_image_path = image_paths['exit']
            print(f'Checking image path: {exit_image_path}')
            while True:
                try:
                    position = pg.locateOnScreen(exit_image_path, grayscale=True, confidence=0.9)
                    
                    if position is not None:
                        point = pg.center(position)
                        print(f'Image found at: {point}')
                        pg.click(point)
                        print(f'Clicked on image at: {point}')
                        break
                    else:
                        print(f'Image not found: {exit_image_path}. Retrying...')
                        time.sleep(1)
                except Exception as e:
                    print(f'An error occurred: {e}')
                    time.sleep(1)
            time.sleep(1)
            # 最后点击 360_exit2.png
            eexit_image_path = image_paths['eexit']
            print(f'Checking image path: {eexit_image_path}')
            while True:
                try:
                    position = pg.locateOnScreen(eexit_image_path, grayscale=True, confidence=0.9)
                    
                    if position is not None:
                        point = pg.center(position)
                        print(f'Image found at: {point}')
                        pg.click(point)
                        print(f'Clicked on image at: {point}')
                        break
                    else:
                        print(f'Image not found: {eexit_image_path}. Retrying...')
                        time.sleep(1)
                except Exception as e:
                    print(f'An error occurred: {e}')
                    time.sleep(1)
            # 最后点击 360_always_always_exit.png
            eeexit_image_path = image_paths['eeexit']
            print(f'Checking image path: {eeexit_image_path}')
            while True:
                try:
                    position = pg.locateOnScreen(eeexit_image_path, grayscale=True, confidence=0.9)
                    
                    if position is not None:
                        point = pg.center(position)
                        print(f'Image found at: {point}')
                        pg.click(point)
                        print(f'Clicked on image at: {point}')
                        break
                    else:
                        print(f'Image not found: {eeexit_image_path}. Retrying...')
                        time.sleep(1)
                except Exception as e:
                    print(f'An error occurred: {e}')
                    time.sleep(1)


elif current_version =="Windows 11":
            # 先点击 win10black.png
            win10black = image_paths['win11white']
            print(f'Checking image path: {win10black}')
            while True:
                try:
                    position = pg.locateOnScreen(win10black, grayscale=True, confidence=0.9)
                    
                    if position is not None:
                        point = pg.center(position)
                        print(f'Image found at: {point}')
                        pg.click(point)
                        print(f'Clicked on image at: {point}')
                        break
                    else:
                        print(f'Image not found: {win10black}. Retrying...')
                        time.sleep(1)
                except Exception as e:
                    print(f'An error occurred: {e}')
                    time.sleep(1)
            time.sleep(1)

            # 再点击 360_img.png 并进行右键点击
            hh_image_path = image_paths['hh']
            print(f'Checking image path: {hh_image_path}')
            while True:
                try:
                    position = pg.locateOnScreen(hh_image_path, grayscale=True, confidence=0.9)
                    
                    if position is not None:
                        point = pg.center(position)
                        print(f'Image found at: {point}')
                        pg.rightClick(point)
                        print(f'Right-clicked on image at: {point}')
                        break
                    else:
                        print(f'Image not found: {hh_image_path}. Retrying...')
                        time.sleep(1)
                except Exception as e:
                    print(f'An error occurred: {e}')
                    time.sleep(1)
            time.sleep(1)

            # 点击 360_exit.png
            exit_image_path = image_paths['exit']
            print(f'Checking image path: {exit_image_path}')
            while True:
                try:
                    position = pg.locateOnScreen(exit_image_path, grayscale=True, confidence=0.9)
                    
                    if position is not None:
                        point = pg.center(position)
                        print(f'Image found at: {point}')
                        pg.click(point)
                        print(f'Clicked on image at: {point}')
                        break
                    else:
                        print(f'Image not found: {exit_image_path}. Retrying...')
                        time.sleep(1)
                except Exception as e:
                    print(f'An error occurred: {e}')
                    time.sleep(1)
            time.sleep(1)
            # 最后点击 360_exit2.png
            eexit_image_path = image_paths['eexit']
            print(f'Checking image path: {eexit_image_path}')
            while True:
                try:
                    position = pg.locateOnScreen(eexit_image_path, grayscale=True, confidence=0.9)
                    
                    if position is not None:
                        point = pg.center(position)
                        print(f'Image found at: {point}')
                        pg.click(point)
                        print(f'Clicked on image at: {point}')
                        break
                    else:
                        print(f'Image not found: {eexit_image_path}. Retrying...')
                        time.sleep(1)
                except Exception as e:
                    print(f'An error occurred: {e}')
                    time.sleep(1)
            # 最后点击 360_always_always_exit.png
            eeexit_image_path = image_paths['eeexit']
            print(f'Checking image path: {eeexit_image_path}')
            while True:
                try:
                    position = pg.locateOnScreen(eeexit_image_path, grayscale=True, confidence=0.9)
                    
                    if position is not None:
                        point = pg.center(position)
                        print(f'Image found at: {point}')
                        pg.click(point)
                        print(f'Clicked on image at: {point}')
                        break
                    else:
                        print(f'Image not found: {eeexit_image_path}. Retrying...')
                        time.sleep(1)
                except Exception as e:
                    print(f'An error occurred: {e}')
                    time.sleep(1)
