## Contributing

In order to avoid the [running and the screaming](https://www.youtube.com/watch?v=6GEFwiXWieM) in the development of this project 
we will propose a series of basic guidelines:

* :computer: :ok_hand: Check the code is correcly interpreted without errors before pushing and creating a PR
* :memo: :rainbow: State **clearly** at the commit message whatever is happening or solving
* :zap: :heavy_exclamation_mark: Preferably one commit that solves an entire issue than several small commits without a goal or reason
* :twisted_rightwards_arrows: :cop: PR must be checked and approved by assigned members to review

In a new issue a clear goal must be specified and make correct use of labels if required. It is a good practice to provide additional documentation (guides or other assets) that may help
understand whatever the issue is trying to solve.

## Git workflow

- `master` Main branch. This branch can only be accessed through PRs from other branches. Production branch, versioned through tags and GitHub releases.
A esta rama sólo se accede mediante PRs desde`dev` o `bugfix`. 
- `feature` Issue solving branch and enhancements. In this type of branches the main development will be made. 
A PR will be issued when an issue is solved or a development is done in this branch. It is recommended that commits are isolated enough to complete an issue or a feature. It is also recommended that the issue message solves the issue (see Set issues as solved)
- `bugfix` Quicksolving bugs in master. Danger. Do Not Touch.

Some good practices and suggestions:
- [Write a good commit message](https://chris.beams.io/posts/git-commit/)
- [Set issues as solved from commit message](https://help.github.com/articles/closing-issues-using-keywords/)
