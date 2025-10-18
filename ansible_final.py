import subprocess

def showrun():
    # read https://www.datacamp.com/tutorial/python-subprocess to learn more about subprocess
    command = ['ansible-playbook', 'playbook.yaml']
    result = subprocess.run(command, capture_output=True, text=True)
    result = result.stdout
    if 'ok=2' in result:
        filename = f"show_run_66070221_R1-Exam.txt"
        return filename
    else:
        return "Error: Ansible"
