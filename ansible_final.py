import subprocess

def showrun():
    output_filename = "show_run_66070221_R1-Exam.txt"
    command = ['ansible-playbook', 'playbook.yaml']
    
    result = subprocess.run(command, capture_output=True, text=True)
    result = result.stdout
    
    if 'ok=2' in result:
        return output_filename
    else:
        return 'Error: Ansible'
