# Claude Orchestration

> Multi-model agent pipeline using Claude as orchestrator with downstream models.

## Goal
Setup Claude orchestration layer with:
- Multiple OpenClaw-derived models downstream
- Recursive multimodal diff (DIF) checker
- Variety of local models on AI server

## Components

### OpenClaw
- Open-source autonomous AI agent sandbox
- Avoids repeated "always allow" permission prompts
- Runs locally, works with Anthropic/OpenAI/local models
- Good base for task agents
- [[Areas/Homelab]] hosts the local model infrastructure

### Local Model Server
- AI server running Ollama/LM Studio-compatible stack
- Download variety of models (partially done ✅)
- Target: MiniMax M2.1 for large context + injection defense

### Recursive Multimodal DIF Checker
- Automated diff/review pipeline across modalities
- TBD architecture

## Status
- [ ] Setup Claude orchestration
- [ ] Wire up multiple OpenClaw models downstream
- [ ] Build recursive multimodal diff checker
- [x] Download variety of models to AI server

## Related
[[Areas/Homelab]] · [[Areas/Home Assistant]] · [[Home]]
