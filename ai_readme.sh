# AI Readme Generation
ai_readme () {
  local dir=$(pwd)
  echo "Generating readme for directory: $dir"
  readmeai --repository $dir --api ollama --model mistral:7b-instruct --emojis --badge-style flat-square
}