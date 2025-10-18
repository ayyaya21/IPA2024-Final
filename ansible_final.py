import subprocess

STUDENT_ID = "66070221"

def showrun():
    playbook_file = "playbook.yaml"
    command = ["ansible-playbook", playbook_file]
    result = subprocess.run(command, capture_output=True, text=True)
    output = result.stdout + result.stderr
    if "FAILED=0" in output:
        router_name = "R1-Exam"
        filename = f"show_run_{STUDENT_ID}_{router_name}.txt"
        return filename
    else:
        return "Error: Ansible"
