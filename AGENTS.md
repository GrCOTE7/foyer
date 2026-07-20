# Foyer Framework

This is a framework for AI agents in software development, derived from Gilles Maury's work on sustainable, responsible software development.

## Key Files

- `Manifeste-Foyer.md`: Identity and values of the agent (Architect Solution)
- `Methode-Foyer.md`: Operational method for agent work
- `Boucle-de-retroaction.md`: Core feedback loop
- `skills/`: Tools for objective evaluation (cycle-dev, gates, convergence-iac, adoption, etc.)
- `personas/`: Roles that hold the feedback loop (chef-de-projet, scrum-master, lead-developer, etc.)

## Workflow

1. **Conception (BMAD)** - Create backlog with validated "Agent IA Ready" stories
2. **Pilotage** - Project manager coordinates timeline, costs, and choice of methodology
3. **Fabrication** - Lead developer and scrum master execute cycle-dev with gates
4. **Production** - Platform engineer manages convergence-iac
5. **Pilotage continu** - CSI engineer refines estimates; Support engineer evaluates adoption

## Agent Instructions

The framework encourages AI agents to:
- Generate code, but have humans validate
- Work in pairs or mobs to avoid single points of failure
- Focus on sobriety, durability, and transmissibility
- Emphasize the "répondre-de" principle: "Pourrai-je en répondre, et devant qui?"

## Core Principles

- All decisions should be traceable via ADRs (Architectural Decision Records)
- Gate reviews ensure architectural foundations remain solid
- Capacity-based milestones (not arbitrary dates)
- All choices should be justified and presented to humans
- Balance between efficiency and human responsibility

## Cost Considerations

- Tokens: 0.85 €/Mtok in, 2.55 €/Mtok out
- Wall-clock: S=0.5 j / M=0.75 j / L=1 j

## Repository Structure

This is a methodology repository for the Foyer framework. Key directories:
- `bmad/` - Conception phase (TOGAF pipeline)
- `skills/` - Objective evaluation tools (cycle-dev, gates, convergence-iac, adoption)
- `tools/` - Executable counterpart to the skills. Currently `tools/gates/`:
  the consolidated tool list (`ADR-outillage.md`) plus CI templates per stack.
  **Templates carry a `.example` suffix and never run on this repository** —
  they are examples to draw from, reinstantiated per consuming project.
- `personas/` - Roles that hold the feedback loop
- `docs/` - Generated documentation site
- `notebooklm/` - Media assets for educational materials
- `scripts/` - Generation scripts for documentation

## Commands

- Build documentation: `mkdocs build`
- Serve documentation locally: `mkdocs serve`
- Generate supports page: `python scripts/gen_supports.py`
- Generate gates templates page: `python scripts/gen_gates.py`

## Special Notes

- The framework is designed to be portable across agent platforms (OpenCode, Claude, etc.)
- All decisions should be made with human oversight ("répondre-de" principle)
- The core feedback loop follows: Conception → Construction → Result → Evaluation → Improvement
- Documentation is built with MkDocs Material and deployed via GitHub Actions