#!/usr/bin/env python3
"""
Matt Murphy Production Linter & Static Codebase Auditor
Scans projects for critical production anti-patterns based on 321 Matt Murphy masterclasses.

Usage:
    python audit_codebase.py [path_to_project] [--json]
"""

import os
import sys

# Delegate directly to the production guardrails audit script
script_dir = os.path.dirname(os.path.abspath(__file__))
guardrail_script = os.path.join(script_dir, '..', 'skills', 'matt-murphy-production-engineer', 'scripts', 'audit_guardrails.py')

if __name__ == '__main__':
    if os.path.exists(guardrail_script):
        with open(guardrail_script, 'r', encoding='utf-8') as f:
            code = f.read()
        exec(compile(code, guardrail_script, 'exec'))
    else:
        print(f"Error: Could not locate guardrail script at {guardrail_script}")
        sys.exit(1)
