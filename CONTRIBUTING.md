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

## Releases

Semantic Versioning: Use semantic versioning (SemVer) to tag releases. This involves incrementing version numbers in the format MAJOR.MINOR.PATCH (e.g., 1.0.0).
+ MAJOR version for incompatible API changes.
+ MINOR version for adding functionality in a backwards-compatible manner.
+ PATCH version for backwards-compatible bug fixes.

1.	Feature Development:
    + Create a feature branch from develop.
    + Opens a PR to merge the feature branch into develop.
    + PR is reviewed, tested, and merged into develop.
2.	Preparing a Release:
    + Create a release branch from develop (release/1.0.0).
	+ Perform final testing and apply any bug fixes.
	+ Merge release/1.0.0 into main and tag the release (v1.0.0).
	+ Merge release/1.0.0 back into develop.
3.	Hotfix:
    + Create a hotfix branch from main (hotfix/1.0.1).
	+ Apply the fix, test, and merge back into main and develop.
    + Tag the release (v1.0.1).



Branching Strategy

+ Main Branch: The main (or master) branch should always reflect a production-ready state.
+ Develop Branch: A develop branch where ongoing development occurs. Features and fixes are integrated here.
+ Feature Branches: Create branches from develop for new features (feature/feature-name).
+ Release Branches: Create branches from develop when preparing a new release (release/x.y.z). This allows final testing and bug fixes.
+ Hotfix Branches: Create branches from main for critical fixes that need to be released immediately (hotfix/x.y.z).


## Linting

1. First run pylint
```zsh
pylint src --rcfile=.pylintrc 
```

2. Then use autopep to recursively lint directory src/ 
```zsh
autopep8 --in-place --aggressive --recursive src/
```

3. Black is also an autoformatter included in this package
```zsh

black --line-length=120 .
```


```
git checkout -b release/1.0.0

git tag -a v1.0.0 -m "Release 1.0.0"
git push origin v1.0.0
gh release create v1.0.0

git push --follow-tags origin main
gh release create $(git describe --tags `git rev-list --tags --max-count=1`) -F CHANGELOG.md
```