# Git Commands Cheatsheet for Team Development

## Initial Setup (One-time only)

### Clone Repository
```bash
# Clone the repository to your local machine
git clone <repository-url>
cd <repository-name>

# Set up your identity (if not done globally)
git config user.name "Your Name"
git config user.email "your.email@company.com"
```

## Daily Workflow Commands

### 1. Getting Latest Changes from Main Branch

```bash
# Switch to main branch
git checkout main

# Pull latest changes from remote main branch
git pull origin main

# Alternative: Fetch and merge separately
git fetch origin
git merge origin/main
```

### 2. Creating and Working on Your Feature Branch

```bash
# Create a new branch from main and switch to it
git checkout -b feature/your-feature-name

# Alternative: Create branch first, then switch
git branch feature/your-feature-name
git checkout feature/your-feature-name

# Verify you're on the correct branch
git branch
# or
git status
```

### 3. Making Changes and Commits

```bash
# Check status of your changes
git status

# Add specific files to staging area
git add filename.js
git add folder/

# Add all changes to staging area
git add .

# Commit your changes with a descriptive message
git commit -m "Add user authentication feature"

# Push your branch to remote repository
git push origin feature/your-feature-name

# For first push of new branch
git push -u origin feature/your-feature-name
```

### 4. Creating Pull Request

```bash
# After pushing your branch, create PR via:
# - GitHub: Go to repository → "Compare & pull request"
# - GitLab: Go to repository → "Create merge request"
# - Command line (GitHub CLI):
gh pr create --title "Your PR Title" --body "Description of changes"
```

### 5. Git Stash Operations

```bash
# Save current changes to stash (temporary storage)
git stash

# Save with a descriptive message
git stash save "Work in progress on login feature"

# List all stashes
git stash list

# Apply the most recent stash (keeps stash in list)
git stash apply

# Apply a specific stash
git stash apply stash@{1}

# Pop the most recent stash (applies and removes from stash list)
git stash pop

# Drop/delete a specific stash
git stash drop stash@{1}

# Clear all stashes
git stash clear

# Show what's in a stash
git stash show stash@{0}
git stash show -p stash@{0}  # Show full diff
```

## Advanced Scenarios

### Updating Your Branch with Latest Main Changes

```bash
# Switch to main and pull latest changes
git checkout main
git pull origin main

# Switch back to your feature branch
git checkout feature/your-feature-name

# Merge main into your branch (or use rebase)
git merge main
# or
git rebase main
```

### Handling Merge Conflicts

```bash
# After merge conflict occurs:
# 1. Open conflicted files and resolve conflicts manually
# 2. Add resolved files
git add conflicted-file.js

# 3. Complete the merge
git commit

# For rebase conflicts:
git rebase --continue
# or abort if needed
git rebase --abort
```

### Branch Management

```bash
# List all branches (local)
git branch

# List all branches (local and remote)
git branch -a

# Delete a local branch (after PR is merged)
git branch -d feature/your-feature-name

# Force delete a branch
git branch -D feature/your-feature-name

# Delete remote branch
git push origin --delete feature/your-feature-name
```

### Undoing Changes

```bash
# Discard changes in working directory
git checkout -- filename.js

# Unstage a file (opposite of git add)
git reset HEAD filename.js

# Undo last commit (keeps changes in working dir)
git reset --soft HEAD~1

# Undo last commit and discard changes
git reset --hard HEAD~1

# Revert a commit (creates new commit that undoes changes)
git revert <commit-hash>
```

## Useful Information Commands

```bash
# View commit history
git log
git log --oneline
git log --graph --oneline --all

# See differences
git diff                    # Working dir vs staged
git diff --staged          # Staged vs last commit
git diff HEAD              # Working dir vs last commit
git diff main..feature     # Compare branches

# Check remote repositories
git remote -v

# See which files are tracked/untracked
git status
git ls-files
```

## Common Workflow Example

```bash
# 1. Start of day - get latest main
git checkout main
git pull origin main

# 2. Create feature branch
git checkout -b feature/add-user-profile

# 3. Work on your code...
# ... make changes to files ...

# 4. Save work temporarily if needed
git stash save "Half-way through user profile component"

# 5. Switch to different task if needed
git checkout feature/bug-fix-123
# ... work on bug fix ...

# 6. Go back to original work
git checkout feature/add-user-profile
git stash pop

# 7. Complete your work and commit
git add .
git commit -m "Complete user profile feature with avatar upload"

# 8. Push and create PR
git push -u origin feature/add-user-profile
# Create PR via web interface

# 9. After PR is approved and merged, cleanup
git checkout main
git pull origin main
git branch -d feature/add-user-profile
```

## Best Practices

- Always pull from main before creating a new branch
- Use descriptive branch names: `feature/user-auth`, `bugfix/login-error`, `hotfix/security-patch`
- Write clear, descriptive commit messages
- Commit frequently with small, logical changes
- Test your code before pushing
- Use git stash when you need to quickly switch contexts
- Keep your branches up to date with main branch
- Delete branches after they're merged to keep repo clean

## Emergency Commands

```bash
# If you accidentally commit to main instead of feature branch:
git reset --soft HEAD~1        # Undo commit, keep changes
git stash                      # Stash the changes
git checkout -b feature/new-branch  # Create proper branch
git stash pop                  # Apply your changes

# If you need to abandon all local changes:
git reset --hard HEAD
git clean -fd  # Remove untracked files and directories
```

Remember: When in doubt, use `git status` to see what's happening!