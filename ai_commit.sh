# AI Commit Message
ai_commit() {
 diff=$(git diff --cached)
 ollama run mistral:7b-instruct "Diff: $diff. Suggest 3 commit messages for the diff provided above in a list format. commit messages should follow conventional commit style, and the format should be <type>[scope]: <description>. Example: fix(authentication): add password regex pattern."
}