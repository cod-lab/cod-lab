<h1 align=center>Self Updating README</h1>

### <ins>1. Github Status Cards</ins>
- The image you see on the top right and the bottom can be created for anyone.
- Just add these links in your README (with your username):
- Top Image:
  - `<img align="right" alt="Top Langs" width="33%" src="https://github-readme-stats.vercel.app/api/top-langs/?username="username"&theme=solarized-light" />`
  <br><img align="" width="15%" src="top.jpg" />
- Bottom Image:
  - `<img alt="My Github Stats" src="https://github-readme-stats.vercel.app/api?username="username"&show_icons=true&hide_border=true" />`
  <br><img align="" width="25%" src="bottom.jpg" />
- It is created by [Anurag Hazra](https://github.com/anuraghazra).
- You can follow his [repo](https://github.com/anuraghazra/github-readme-stats) for more info and card configurations.

<br>

### <ins>2. Latest Github Repos</ins>
To display your latest repos which must be updated automatically you need two things:

- `a script which can update your README if there is any update.`
  - i wrote a [python script](https://github.com/cod-lab/cod-lab/blob/master/update_readme.py) to do the job.
  - the script fetches result from gitapi and overwrite it in README file if there's any change.
  - you can write the script in any language.
- `a program which runs automatically and performs the instructions you have written in .yml file.`
  <!-- - the program probably known as CI/CD. -->
  - github provides free/premium CI/CD to do your job for you.
  - you have to create workflow file "reponame"/.github/workflows/"filename".yml.
  - in a workflow file there will be series of instructions which will be performed automatically on occurance of any defined event or at any particular interval of time.  <!-- write to run automatically on occurance of any defined event or at any particular period of time. -->
  - [my workflow](https://github.com/cod-lab/cod-lab/blob/master/.github/workflows/readme-profile.yml) file runs the script at particular time on set days of every month. this workflow will commmit changes only if there will be any updation in the repository.
  <!-- - you can refer my [yml] file. -->
  - you can refer [github documentation](https://docs.github.com/en/actions/configuring-and-managing-workflows/configuring-a-workflow) for more info.

<br>

> Just upload these files and github CI will automatically start working.
