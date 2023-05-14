import os
import subprocess

def create_repository():
    repo_name = input("Enter a repository name: ")
    os.mkdir(repo_name)
    os.chdir(repo_name)
    subprocess.run(['git', 'init'])
    print(f"Created repository '{repo_name}'.")

def clone_repository():
    repo_url = input("Enter a repository URL: ")
    subprocess.run(['git', 'clone', repo_url])
    repo_name = os.path.splitext(os.path.basename(repo_url))[0]
    print(f"Cloned repository '{repo_name}'.")

def update_repository():
    repo_path = input("Enter the repository path: ")
    os.chdir(repo_path)
    subprocess.run(['git', 'pull'])
    print(f"Updated repository '{repo_path}'.")

def change_git_profile():
    username = input("Enter your Git username: ")
    email = input("Enter your Git email: ")
    subprocess.run(['git', 'config', '--global', 'user.name', username])
    subprocess.run(['git', 'config', '--global', 'user.email', email])
    print("Git profile information updated.")

def stage_changes():
    subprocess.run(['git', 'add', '.'])
    print("Changes staged.")

def add_vscode_to_linux():
    print("Installing VSCode...")
    subprocess.run(['sudo', 'snap', 'install', 'code', '--classic'])
    print("VSCode installation complete.")

def push_local_repository():
    repo_path = input("Enter the repository path: ")
    os.chdir(repo_path)
    remote_name = input("Enter the remote name (e.g., origin): ")
    branch_name = input("Enter the branch name (e.g., main): ")
    subprocess.run(['git', 'push', remote_name, branch_name])
    print("Local repository pushed to remote.")

def generate_ssh_key():
    email = input("Enter your email: ")
    subprocess.run(['ssh-keygen', '-t', 'rsa', '-b', '4096', '-C', email])
    subprocess.run(['eval', "$(ssh-agent -s)"])
    subprocess.run(['ssh-add', '~/.ssh/id_rsa'])
    print("SSH key generated and added to the Git profile.")

def print_menu():
    print("Menu:")
    print("1. Create Repository")
    print("2. Clone Repository")
    print("3. Update Repository")
    print("4. Change Git Profile information")
    print("5. Stage Changes")
    print("6. Add VSCode to Linux")
    print("7. Push Local Repository to Remote")
    print("8. Generate SSH key and add to Git Profile")
    print("9. Exit")

# Main script
while True:
    os.system('clear' if os.name == 'posix' else 'cls')
    print_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        create_repository()
    elif choice == '2':
        clone_repository()
    elif choice == '3':
        update_repository()
    elif choice == '4':
        change_git_profile()
    elif choice == '5':
        stage_changes()
    elif choice == '6':
        add_vscode_to_linux()
    elif choice == '7':
        push_local_repository()
    elif choice == '8':
        generate_ssh_key()
    elif choice == '9':
        break
    else:
        print("Invalid choice. Please enter a valid option.")

    input("Press Enter to continue...")
