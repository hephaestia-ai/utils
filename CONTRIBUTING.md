# Contributing

We @ Cowgirl AI are big open source people. We srsly love contributions and try to empower each other to do more of it. So if you're happy about this evolving file-management project, and want to help us out, throw down a line of code or two.

Whether you're fixing a bug, adding a new feature, or improving the documentation,
your contributions are greatly appreciated.


## Getting Started

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.

```zsh
git clone https://github.com/your-username/file-management.git
```

3. Create a new branch for your changes.
```
git checkout -b my-new-feature

```

4. Make your changes and commit them with descriptive commit messages.
```
git add .
git commit -m "Add new feature: xyz"

```

5. Push your changes to your forked repository.

```
git push origin my-new-feature
```

6. Open a pull request on the main repository, describing your changes and their purpose.




## Reporting Issues

If you encounter any bugs or have feature requests, please open an issue on the GitHub repository. Please provide as much detail as possible, including steps to reproduce the issue and any relevant error messages or logs.



## Linting

1. First run pylint src/
```zsh
pylint src/
```

2. Then use autopep to recursively lint directory src/ 
```zsh
autopep8 --in-place --aggressive --recursive src/
```

3. Black is also an autoformatter included in this package
```zsh

black --line-length=120 .
```