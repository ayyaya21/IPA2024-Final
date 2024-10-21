import subprocess

def backup():
    # read https://www.datacamp.com/tutorial/python-subprocess to learn more about subprocess
    command = ['<!!!REPLACEME with ansible command to run playbook!!!>', '<!!!REPLACEME with playbook yaml file!!!>']
    result = subprocess.run(command, capture_output=True, text=True)
    result = result.stdout
    # all two tasks in playbook are ok, return 'ok', if not return 'Error: Ansible'
    if 'ok=2' in result:
        return <!!!REPLACEME!!!>
    else:
        return '<!!!REPLACEME!!!>
