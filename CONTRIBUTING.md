# Contributing to Awesome Mac AI

Thank you for considering contributing to **Awesome Mac AI**!

## Inclusion Guidelines

1. **macOS First**: The tool or application must run on macOS (with strong preference for native Apple Silicon / Metal support).
2. **Quality & Utility**: We prioritize actively maintained, high-quality tools that enhance AI workflows.
3. **Structured Attribution**:
   - Provide accurate `Primary Type`, `Surface`, `Capabilities`, and `Status`.
   - Distinguish the interface (e.g. CLI vs Desktop) from the underlying architecture (e.g. Harness vs IDE).
4. **No Direct Promotion / Spam**: Submissions must provide verifiable value to the community.

## How to Submit

1. Fork the repository.
2. Update `README.md` and `README.en.md` with your suggested tool.
3. Add the structured entry to `data/apps.json`.
4. Run validation:
   ```bash
   python3 scripts/validate.py
   ```
5. Open a Pull Request with a clear description of why this tool is recommended.
