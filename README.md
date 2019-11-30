# Polka
A simple framework for setting up your dot-files on new machines. The only fixed dependency is `python3`. Other dependencies depend on the particular config you are installing.

## How to use my configuration
Simply run `./polka.py` to install all of the available configurations.

`./polka.py ls` will list all of the available configurations. You can install a particular configuration with `./polkya.py install <config name>`.

That's all there is to it!

## How to write your own configuration
Each configuration lives in it's own directory; the name of the directory is the identifier of the configuration. For example, the configuration for `zsh` is in the `zsh` directory.

For a directory to count as a configuration, it needs a `config.json`. Below is an example configuration:
``` json
{
  "title": "ZSH Config",
  "prereqs": ["zsh", "git"],
  "repos": {
    "oh-my-zsh": {
      "url": "https://github.com/sgpthomas/oh-my-zsh",
      "dest": "~/.oh-my-zsh"
    },
    "zsh-syntax-highlighting": {
      "url": "https://github.com/zsh-users/zsh-syntax-highlighting.git",
      "dest": "~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting"
    }
  },
  "touch": [
    "~/.zshenv",
    "~/.zshprojects",
    "~/.zshalias",
    "~/.zshlocal"
  ],
  "links": {
    "zshrc": "~/.zshrc"
  },
  "finalize": ["zsh ~/.zshrc"]
}
```

### Configuration sections
#### `title`
This is the only required section. This is just a human readable name for the configuration.

#### `prereqs`
A list of binaries that must be installed for this configuration to be successfully installed.

#### `repos`
This is used for cloning git repositories. It assumes that `git` is installed. The `url` field is the repository url and the `dest` field is the location to clone the repository to.

#### `touch`
Touch takes in a list of files and makes sure that this file exists in the host machine. If it exists already, nothing happens.

#### `links`
Links create a symlink from the json key to the json value. It assumes that a file with the name of the key exists in the current configuration directory. In the above example, we create a symlink from `zshrc` to `~/.zshrc`. This assumes that `zshrc` exists in the `zsh` configuration directory. 

A reason that you might want to use symlinks is to keep the ground truth for your dot files in the repo so that they can be kept in sync across machines simply by updating the repository.

#### `finalize`
Finalize takes a list of strings and executes each of them in order in the shell. This is used to finalize the installation of this configuration using any of the files that were downloaded in the earlier sections.
