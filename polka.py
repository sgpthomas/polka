#!/usr/bin/env python3

import argparse
import os
import json
from pathlib import Path
import contextlib
import sys

class CommandParser():
    def __init__(self, description=''):
        self.parser = argparse.ArgumentParser(description=description)
        self.subparsers = self.parser.add_subparsers(help='Sub-commands')

    def run(self):
        args = self.parser.parse_args()
        if "action" in args:
            args.action(args)
        elif self.default != None:
            self.default(args)
        else:
            raise Exception("[Dev] You need to specify a default command")

    def sub_command(self, aliases=[], args=None, default=False):
        def sub_command_dec(func):
            # configure subparser
            sp = self.subparsers.add_parser(func.__name__, aliases=aliases, help=func.__doc__)
            sp.set_defaults(action=func)

            if args != None:
                sp.add_argument(args, nargs='*')

            # set default
            if default:
                self.default = func

        return sub_command_dec

class Enter():
    def __init__(self, path):
        self.path = Path(path)
        self.current = Path.cwd()

    def __enter__(self):
        os.chdir(self.path.expanduser())

    def __exit__(self, *args):
        print(args)
        os.chdir(self.current)

class DummyFile(object):
    def write(self, *args, **kwargs): pass
    def flush(self, *args, **kwargs): pass

@contextlib.contextmanager
def nostdout():
    print("Starting...", end='', flush=True)
    save_stdout = sys.stdout
    sys.stdout = DummyFile()
    save_stderr = sys.stderr
    sys.stderr = DummyFile()
    yield
    sys.stdout = save_stdout
    sys.stderr = save_stderr
    print("Done")

def gather_configs():
    for path in Path('.').iterdir():
        for config in path.glob('config.json'):
            with open(config) as f:
                data = json.load(f)
                yield str(path), data
                # yield data
    # for config in Path('.').glob('*/config.json'):
    #     with open(config) as f:
    #         data = json.load(f)
    #         print(f.parts)
    #         yield data

def install_repos(name, repos):
    for name, config in repos.items():
        if Path(config['dest']).expanduser().exists():
            with Enter(config['dest']):
                os.system('git pull -r')
        else:
            url = config['url']
            dest = config['dest']
            os.system(f'git clone {url} {dest}')

def install_dirs(name, dirs):
    for d in dirs:
        Path(d).expanduser().mkdir(parents=True, exist_ok=True)

def install_touch(name, touch):
    for fil in touch:
        Path(fil).resolve().touch()

def install_links(name, links):
    for ln, dest in links.items():
        resolve = Path(dest).expanduser()
        ln_path = Path.cwd() / name / ln
        if resolve != ln_path:
            resolve.unlink(missing_ok=True)
            resolve.symlink_to(ln_path)

def finalize(name, script):
    for scr in script:
        os.system(scr)

def commit_config(name, config):
    with nostdout():
        if 'repos' in config:
            install_repos(name, config['repos'])
    with nostdout():
        if 'dirs' in config:
            install_dirs(name, config['dirs'])
    with nostdout():
        if 'touch' in config:
            install_touch(name, config['touch'])
    with nostdout():
        if 'links' in config:
            install_links(name, config['links'])
    with nostdout():
        if 'finalize' in config:
            finalize(name, config['finalize'])


###### Command Line Parsing #######

parser = CommandParser(description='Install dot files')

@parser.sub_command(aliases=['list'])
def ls(args):
    """Lists available configurations to install"""
    for name, config in gather_configs():
        print(name, config['title'])

@parser.sub_command(default=True, args='configs')
def install(args):
    """Install configurations"""
    configs = dict(gather_configs())
    if 'configs' in args:
        for key in args.configs:
            if key not in configs:
                raise Exception("Error")
            commit_config(key, configs[key])
    else:
        for key, config in configs.items():
            commit_config(key, config)

parser.run()
