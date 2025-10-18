import subprocess
import os

def showrun():
    output_filename = "show_run_66070221_R1-Exam.txt"
    playbook_file = 'playbook.yaml'

    current_dir = os.getcwd()
    
    command = f'ansible-playbook {playbook_file}'

    try:
        # ใช้ os.chdir เพื่อย้ายไปยังไดเร็กทอรีที่ถูกต้องก่อนรัน (ถ้าจำเป็น)
        # หากไฟล์ Playbook อยู่ใน CWD อยู่แล้ว ไม่จำเป็นต้องใช้ os.chdir
        
        # ลองรันด้วย shell=True เพื่อให้ Windows shell จัดการการเรียก exe
        result = subprocess.run(
            command, 
            capture_output=True, 
            text=True, 
            check=True,
            shell=True 
        )
        
        # แสดงผลลัพธ์ทั้งหมดเพื่อ Debug
        print("--- Ansible Playbook Output (STDOUT) ---")
        print(result.stdout)
        print("--------------------------------------")
        
        # ตรวจสอบความสำเร็จ (ok=2 คือ 2 tasks สำเร็จ)
        if 'ok=2' in result.stdout:
            return output_filename
        else:
            return 'Error: Ansible'
            
    except subprocess.CalledProcessError as e:
        # จับข้อผิดพลาดที่เกิดขึ้นเมื่อ ansible-playbook ล้มเหลว
        print("--- Ansible Playbook Error (STDERR) ---")
        print(e.stderr) 
        print("---------------------------------------")
        return 'Error: Ansible'
    except FileNotFoundError:
        print("Error: Could not find 'ansible-playbook' command. Check your PATH.")
        return 'Error: Ansible'
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 'Error: Ansible'
