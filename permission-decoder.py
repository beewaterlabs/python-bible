#!/usr/bin/env python3

import os
import stat
import argparse
from pathlib import Path

def decode_permission_to_chmod(perm: str) -> str:
    """Convert permission string to chmod octal value.
    
    Args:
        perm (str): Permission string (e.g., 'rwxr-xr--')
        
    Returns:
        str: Chmod octal value
    """
    if len(perm) != 9:
        raise ValueError("Permission string must be exactly 9 characters long")
    
    # Initialize values for each permission category
    owner = group = others = 0
    
    # Calculate owner permissions
    if perm[0] == 'r': owner += 4
    if perm[1] == 'w': owner += 2
    if perm[2] == 'x': owner += 1
    
    # Calculate group permissions
    if perm[3] == 'r': group += 4
    if perm[4] == 'w': group += 2
    if perm[5] == 'x': group += 1
    
    # Calculate others permissions
    if perm[6] == 'r': others += 4
    if perm[7] == 'w': others += 2
    if perm[8] == 'x': others += 1
    
    return f"{owner}{group}{others}"

def decode_file_permission(file_path: str) -> tuple[str, str]:
    """Get permission details from a file.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        tuple: (permission_string, chmod_value)
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File '{file_path}' not found")
    
    # Get file mode
    mode = path.stat().st_mode
    
    # Convert mode to permission string
    perm_string = ''
    for who in ['USR', 'GRP', 'OTH']:
        for what in ['R', 'W', 'X']:
            perm_string += (
                getattr(stat, f'S_I{what}{who}') & mode and what.lower() or '-'
            )
    
    # Get octal representation
    chmod_value = oct(mode & 0o777)[-3:]  # Get last 3 digits
    
    return perm_string, chmod_value

def decode_ls_output(ls_output: str) -> tuple[str, str]:
    """Decode permissions from ls -l output.
    
    Args:
        ls_output (str): Output from ls -l command
        
    Returns:
        tuple: (permission_string, chmod_value)
    """
    # Extract permission string (skip first character which is file type)
    parts = ls_output.split()
    if not parts or len(parts[0]) != 10:  # Including file type character
        raise ValueError("Invalid ls -l output format")
    
    perm_string = parts[0][1:]  # Skip first character (file type)
    chmod_value = decode_permission_to_chmod(perm_string)
    
    return perm_string, chmod_value

def main():
    parser = argparse.ArgumentParser(description='Decode file permissions')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', help='Decode permissions of FILE')
    group.add_argument('-p', '--permission', help='Decode PERMISSION_STRING (e.g., rwxr-xr--)')
    group.add_argument('-l', '--ls-output', help='Decode permissions from ls -l output')
    
    args = parser.parse_args()
    
    try:
        if args.file:
            perm_string, chmod_value = decode_file_permission(args.file)
            print(f"File: {args.file}")
            print(f"Permissions: {perm_string}")
            print(f"Chmod value: {chmod_value}")
            
        elif args.permission:
            if len(args.permission) != 9:
                raise ValueError("Permission string must be exactly 9 characters long")
            chmod_value = decode_permission_to_chmod(args.permission)
            print(f"Permissions: {args.permission}")
            print(f"Chmod value: {chmod_value}")
            
        elif args.ls_output:
            perm_string, chmod_value = decode_ls_output(args.ls_output)
            print(f"Permissions: {perm_string}")
            print(f"Chmod value: {chmod_value}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == '__main__':
    main()
