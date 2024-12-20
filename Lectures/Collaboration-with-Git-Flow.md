In TID we use a collaboration model that's a modified version of a popular one named Git Flow. 

Git Flow is a way of choreographing collaboration with Git that is designed around multiple types of branches as you can see in the following image: 

![The Git Flow Model](images/The%20Git%20Flow%20Model.png)


In the course we make use of the following branches: 
- **main** branch for releases / deliverables
- **Feature branches** for individual work
- Group integration on **development**

## The `main` branch

- Contains releases 
- Only modified by PR from develop
- Protected = only admins can accept PRs to it (TID staff are admins)

## The `development` branch

- Contains the latest version of the team code 
- Always ready for demo
- Point of integration of feature branches

## Feature branches

- Are forked from `development`
- For independent / subgroup work
- Finished features are pushed to develop via Pull Request & tagging a team-member
	- Benefit 1: you get feedback
	- Benefit 2: everybody knows the code



## The `.gitignore` file

- Specifies files that you don’t want tracked
- Make sure that your node_modules folder is in `.gitignore` 
- And that `.gitignore` is in the root of your repo folder
