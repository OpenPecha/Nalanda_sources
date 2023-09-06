import re

from pathlib import Path

def has_illegal_note(text):
    illegal_signs = ['«', '<', '>', '\d']
    for sign in illegal_signs:
        if re.search(sign, text):
            return True

if __name__ == "__main__":
    text_with_issues = []
    philo_dirs = list(Path('nalanda_works').iterdir())
    philo_dirs.sort()
    for philo_dir in philo_dirs:
        philo_work_dirs = list((philo_dir / 'works').iterdir())
        for philo_work_dir in philo_work_dirs:
            philo_work_dirs.sort()
            instance_paths = list(philo_work_dir.iterdir())
            for instance_path in instance_paths:
                if  instance_path.stem in ['01chone', '02derge', '03narthang', '04peking']:
                    instance_text = instance_path.read_text()
                    if philo_work_dir.name == '25DD4388':
                        if has_illegal_note(instance_text):
                            text_with_issues.append(f'{philo_dir.stem}/{philo_work_dir.name}')
    text_with_issues = list(set(text_with_issues))
    text_with_issues.sort()
    Path('./text_with_reconstruction_issues.txt').write_text('\n'.join(text_with_issues), encoding='utf-8')

