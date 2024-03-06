# AI PR Review
ai_pr () {
  diff=$(gh pr diff "$1")
  ollama run mistral:7b-instruct "Provide a brief summary of this PR, and highlight any violations of security and coding best practices in the following git changes diff: $diff"
}