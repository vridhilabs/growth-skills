import json
import os
import argparse
import random
import sys

# Color coding for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class GrowthSkills:
    def __init__(self):
        # Path for templates
        template_path = os.path.join(os.path.dirname(__file__), 'templates', 'templates.json')
        try:
            with open(template_path, 'r') as f:
                self.data = json.load(f)
        except Exception as e:
            print(f"{Colors.FAIL}Error loading templates: {e}{Colors.ENDC}")
            self.data = {"x_templates": [], "linkedin_templates": [], "email_templates": [], "dm_templates": []}

    def list_templates(self):
        print(f"\n{Colors.HEADER}{Colors.BOLD}--- 📈 GROWTH SKILLS: TEMPLATES ---{Colors.ENDC}\n")
        
        def print_category(data, prefix=""):
            for key, val in data.items():
                if isinstance(val, dict):
                    print(f"{prefix}{Colors.OKBLUE}[{key.replace('_', ' ').title()}]{Colors.ENDC}")
                    print_category(val, prefix + "  ")
                elif isinstance(val, list):
                    print(f"{prefix}{Colors.OKBLUE}[{key.replace('_', ' ').title()}]{Colors.ENDC}")
                    for t in val:
                        print(f"{prefix}  • {Colors.BOLD}{t['id']}{Colors.ENDC}: {t['label']} - {t['description']}")
                print("")

        print_category(self.data)
            
    def get_template(self, template_id=None, category='x_templates'):
        templates = self.data.get(category, [])
        if not template_id:
            return random.choice(templates) if templates else None
        
        for t in templates:
            if t['id'] == template_id:
                return t
        return None

def main():
    parser = argparse.ArgumentParser(description="Growth Skills: High-engagement templates for social, email, and DM.")
    parser.add_argument('command', choices=['list', 'get', 'random'], help='The command to execute.')
    parser.add_argument('--id', help='Target template ID.')
    parser.add_argument('--category', choices=['x_templates', 'linkedin_templates', 'email_templates', 'dm_templates'], 
                        default='x_templates', help='Template category.')

    args = parser.parse_args()
    skill = GrowthSkills()

    if args.command == 'list':
        skill.list_templates()
    elif args.command == 'get':
        if not args.id:
            print(f"{Colors.FAIL}Error: --id is required for the 'get' command.{Colors.ENDC}")
            return
        t = skill.get_template(args.id, args.category)
        if t:
            print(f"\n{Colors.OKGREEN}{Colors.BOLD}Template: {t['label']}{Colors.ENDC}")
            print(f"\n{Colors.BOLD}PROMPT:{Colors.ENDC}")
            print(t['prompt'])
        else:
            print(f"{Colors.FAIL}Template '{args.id}' not found in '{args.category}'.{Colors.ENDC}")
    elif args.command == 'random':
        t = skill.get_template(category=args.category)
        if t:
            print(f"\n{Colors.OKGREEN}{Colors.BOLD}Random Template: {t['label']}{Colors.ENDC}")
            print(f"\n{Colors.BOLD}PROMPT:{Colors.ENDC}")
            print(t['prompt'])
        else:
            print(f"{Colors.FAIL}No templates found in '{args.category}'.{Colors.ENDC}")

if __name__ == "__main__":
    main()
