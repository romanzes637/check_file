import os

def check_file(path):
    """
    Check path on the existing file in the order:
    1. If file at relative to current working directory path
    2. Else if file at absolute path
    3. Else if file at relative to running script directory path
    4. Else if file at relative to real running script directory path
    (with eliminating all symbolics links)
    5. Else no file
    :param str path:
    :return dict: {'type': str, 'path': str}
    """
    print('path:\t\t\t {}'.format(path))
    # Norm path
    norm_path = os.path.normpath(path)
    print('norm_path:\t\t {}'.format(norm_path))
    # Expand path
    path_expand_vars = os.path.expandvars(path)
    print('path_exp_vars:\t\t {}'.format(path_expand_vars))
    path_expand_vars_user = os.path.expanduser(path_expand_vars)
    print('path_exp_vars_user:\t {}'.format(path_expand_vars_user))
    path_expand_vars_user_norm = os.path.normpath(path_expand_vars_user)
    print('path_exp_vars_user_norm: {}'.format(path_expand_vars_user_norm))
    # Get directories
    cwd_path = os.getcwd()
    print('cwd_path:\t\t {}'.format(cwd_path))
    script_dir_path = os.path.dirname(os.path.abspath(__file__))
    print('script_dir_path:\t {}'.format(script_dir_path))
    # Set paths to file check
    rel_cwd_path = os.path.join(cwd_path, path)
    print('rel_cwd_path:\t\t {}'.format(rel_cwd_path))
    abs_path = os.path.abspath(path_expand_vars_user)  # equal os.normpath(join(os.getcwd(), path))
    print('abs_path:\t\t {}'.format(abs_path))
    rel_script_path = os.path.join(script_dir_path, path_expand_vars_user)
    print('rel_script_path:\t {}'.format(rel_script_path))
    real_rel_script_path = os.path.realpath(rel_script_path)
    print('real_rel_script_path:\t {}'.format(real_rel_script_path))
    # Check on file:
    result = dict()
    if os.path.isfile(rel_cwd_path):
        result['type'] = 'rel_cwd'
        result['path'] = rel_cwd_path
    elif os.path.isfile(abs_path):
        result['type'] = 'abs'
        result['path'] = abs_path
    elif os.path.isfile(rel_script_path):
        result['type'] = 'rel_script'
        result['path'] = rel_script_path
    elif os.path.isfile(real_rel_script_path):
        result['type'] = 'real_rel_script'
        result['path'] = real_rel_script_path
    else:  # No file
        result['type'] = None
        result['path'] = None
    return result

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='file path')
    args = parser.parse_args()
    print(args)
    result = check_file(args.path)
    print(result)
