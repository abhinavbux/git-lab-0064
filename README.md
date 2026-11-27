# Git & GitHub Practicals — 0064

**Abhinav Bansal · BCA-AI**

This extends the original five-commit lab repository. Original work is preserved in Git history and [the original README](docs/original-README.md). New operations were performed with assistant assistance in a Linux workspace; actual terminal output is in `evidence/`. No fabricated screenshots or reviews are included.

## Practical index

| Practical | Topic | Status |
|---|---|---|
| 1 | [Install Git, configure identity and SSH](practicals/P01.md) | Existing PDF evidence; local identity verified |
| 2 | [Initialize a repository and basic operations](practicals/P02.md) | Original history and new local evidence |
| 3 | [Staging, history and diff](practicals/P03.md) | Original history and new local evidence |
| 4 | [Clone, history and restoration](practicals/P04.md) | Performed locally |
| 5 | [Branch lifecycle and feature workflow](practicals/P05.md) | Performed locally |
| 6 | [Merge and resolve conflicts](practicals/P06.md) | Performed locally |
| 7 | [GitHub repository and push](practicals/P07.md) | GitHub actions pending |
| 8 | [Pull requests, reviews, push, pull and fetch](practicals/P08.md) | GitHub actions pending |
| 9 | [Rebase compared with merge](practicals/P09.md) | Performed locally |
| 10 | [Stash, tags and releases](practicals/P10.md) | Local evidence; GitHub release pending |
| 11 | [Reset, revert and restore](practicals/P11.md) | Performed locally |
| 12 | [GitHub Actions CI/CD and GitOps](practicals/P12.md) | GitHub actions pending |

## Check locally

```bash
python3 -m unittest discover -s tests -v
python3 scripts/build.py
```

Open `site/index.html` to read the generated report. CI runs tests and builds the report on pushes and pull requests. Deployment is manual on main after GitHub Pages setup.

## Published assignment

[Pull request #1](https://github.com/abhinavbux/git-lab-0064/pull/1) contains the assignment files as a snapshot. Local demonstration branches and their original commit IDs are retained in the downloadable assignment bundle, rather than published as GitHub branches. The terminal logs describe those local operations.

## Remaining external evidence

See [PUBLISH.md](PUBLISH.md) for publication, independent PR review, release, and Actions evidence. The attached rubric screenshot lists titles only, not detailed scoring criteria. The existing PDF covers the earlier six-task lab, not all twelve new practicals.
