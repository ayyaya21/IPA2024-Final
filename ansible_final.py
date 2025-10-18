import subprocess
import os # ต้อง import os เพื่อจัดการพาธ

def showrun():
    output_filename = "show_run_66070221_R1-Exam.txt"
    playbook_file = 'playbook.yaml'
    
    command = ['ansible-playbook', playbook_file]
    
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        result = subprocess.run(
            command, 
            capture_output=True, 
            text=True, 
            check=True, 
            cwd=current_dir
        )
        
        print("--- Ansible Playbook Output (STDOUT) ---")
        print(result.stdout)
        print("--------------------------------------")
        
        if 'ok=2' in result.stdout:
            return output_filename
        else:
            return 'Error: Ansible'
            
    except subprocess.CalledProcessError as e:
        print("--- Ansible Playbook Error (STDERR) ---")
        print(e.stderr)
        print("---------------------------------------")
        return 'Error: Ansible'
    except FileNotFoundError:
        print("Error: Could not find 'ansible-playbook' command or 'playbook.yaml' file.")
        return 'Error: Ansible'
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 'Error: Ansible'
