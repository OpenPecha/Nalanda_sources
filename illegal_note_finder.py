import re

from pathlib import Path

def has_illegal_note(text):
    illegal_signs = ['«', '<', '>', '[0-9]', "»"]
    illegal_signs_in_text = ''
    for sign in illegal_signs:
        if re.search(sign, text):
            illegal_signs_in_text += f'{sign}/'
    if illegal_signs_in_text:
        return True, illegal_signs_in_text
    return False, None

if __name__ == "__main__":
    text_with_issues = []
    philo_dirs = list(Path('nalanda_works').iterdir())
    philo_dirs.sort()
    for philo_dir in philo_dirs:
        philo_work_dirs = list((philo_dir / 'works').iterdir())
        philo_work_dirs.sort()
        for philo_work_dir in philo_work_dirs:
            instance_paths = list(philo_work_dir.iterdir())
            instance_paths.sort()
            for instance_path in instance_paths:
                if  instance_path.stem in ['01chone', '02derge', '03narthang', '04peking']:
                    instance_text = instance_path.read_text()
                    has_illegal_notes, sign = has_illegal_note(instance_text)
                    if has_illegal_notes:
                        text_with_issues.append(f'{philo_dir.stem}/{philo_work_dir.name}/{sign}')
    text_with_issues = list(set(text_with_issues))
    text_with_issues.sort()
    Path('./text_with_reconstruction_issues.txt').write_text('\n'.join(text_with_issues), encoding='utf-8')

