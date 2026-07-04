# Rapport de Validation croisée — [PROJET]

*Livrable du Validateur · TOGAF Phase F. Verdict objectivé : on ne sort de BMAD qu'au PASS.*

## Statut global : **PASS / CONCERNS / FAIL**

**Fidelity score** : [X]/100 — score de traçabilité Brief→PRD→Architecture→Stories. **PASS uniquement si ≥ 80.**

> Calcul : (capacités Brief couvertes en PRD / total capacités) × 25 + (FRs couvertes en Architecture / total FRs) × 25 + (FRs couvertes en Stories / total FRs) × 25 + (4 classes couvertes / total 4×N) × 25

## 1. Cohérence DDD
- Glossaire (ubiquitous language) cohérent Brief→PRD→Archi : ☐
- Bounded contexts stables : ☐
- Invariants métier présents et codables : ☐

## 2. Couverture SOLID
[Chaque couche respecte les principes annoncés : ☐]

## 3. Traçabilité
- Brief → PRD (toute capacité a ses exigences) : ☐
- PRD → Architecture (toute exigence a sa couche) : ☐
- PRD → Stories (toute exigence a ses stories) : ☐

## 4. Architecture hexagonale
- Backend : dépendances vers l'intérieur : ☐
- Frontend (hexagonale light) : ☐

## 5. Glossaire → code (mapping présent) : ☐
## 6. BDD + Documentation Vivante (flux critiques couverts) : ☐

## 7. TDD (stratégie de tests + couverture cible) : ☐

## 7bis. Classes de tests 4×N (mécanisé)
- Matrice 4×N par FR présente dans le PRD (`@happy` + `@negative` + `@edge` + `@security`) : ☐
- 4 classes listées dans chaque story : ☐
- Aucune FR orpheline d'une classe : ☐

## 8. Readiness organisationnelle
- Scrum : ☐ · Nexus (si applicable) : ☐ · SAFe (si applicable) : ☐ · ITIL (pré-prod) : ☐

## 9. « Agent IA Ready »
- Specs assez précises pour qu'un agent boucle sans deviner : ☐
- Critères d'acceptation testables : ☐
- Points irréversibles identifiés et marqués « validation humaine » : ☐

## 10. Incohérences détectées
[Liste — chacune renvoyée au persona concerné.]

## 11. Recommandations
[Avant passage en Phase 2.]

---
**Si FAIL/CONCERNS** : reboucler vers le(s) persona(s) concerné(s). **Si PASS** : le superviseur valide le passage au chef de projet (Phase 2).
