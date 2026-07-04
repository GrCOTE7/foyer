# Product Brief — [PROJET]

*Livrable de l'Analyste · TOGAF Phase A (Vision). À remplir ; les champs non renseignés par le superviseur sont marqués `[hypothèse à valider]`.*

## 1. Vision
[Une phrase : pour qui, quel changement.]

## 2. Stakeholders
[Qui est concerné, qui décide, qui subit, qui finance.]

## 3. Drivers business
[Les forces réelles qui justifient le projet — pas les fonctionnalités.]

## 4. Problème
[Le problème vécu, formulé sans la solution.]

## 5. Proposition de valeur
[Ce que le projet apporte que l'existant n'apporte pas.]

## 6. Personas
[Par persona : rôle · objectifs · frustrations actuelles.]

## 7. Capacités métier requises
[Les capacités, pas les écrans. Ordonnées par réversibilité quand c'est possible.]

## 8. Glossaire métier (ubiquitous language DDD)
[Terme → définition. Le vocabulaire qui fera loi dans le code.]

## 9. Bounded contexts pressentis (DDD)
[Les frontières de sens. Provisoires, affinées en Phase C.]

## 10. Invariants métier critiques
[Les règles qui ne doivent jamais être violées — candidates à coder dans les constructeurs.]

## 10bis. Flux multi-acteurs
| Capacité | Initiateur | Validateur | Consommateur | Workflow |
[Pour chaque capacité impliquant 2+ personas, décrire le flux.]

## 11. Fonctionnalités MVP
[Le strict nécessaire pour valider la proposition de valeur.]

## 12. Fonctionnalités post-MVP
[Ce qui attend un jalon de capacité ultérieur.]

## 13. Dimensionnement projet
| Dimension | Valeur estimée |
| Bounded Contexts | [nombre] |
| Entités domain estimées | [nombre — ~4-5 par BC] |
| Endpoints API estimés | [nombre — ~10-15 par BC] |
| Catégorie projet | Micro (1-3 BC) / Petit (3-5 BC) / Moyen (5-10 BC) / Grand (10+ BC) |

## 14. Contraintes
[Conformité (RGPD, ISO 27001, NIS2) · souveraineté/hébergement · multilingue · stack imposée.]

## 15. Risques
| Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|
| | | | |

## 16. Principes d'architecture
[Les non-négociables : hexagonale, DDD au centre, AGPL si applicable, etc.]

## 17. Métriques de succès
[Comment on saura que ça marche — mesurable.]

## 18. Estimation budgétaire préliminaire (point 0)
- **Échelle visée** : Scrum / Nexus / SAFe
- **Coût superviseur** : [jours-homme × taux] — fourchette large assumée
- **Coût modèle** : [tours estimés → tokens → € à 0,85 €/Mtok in, 2,55 €/Mtok out]
- **Seed** : [hérité de quel projet à stack égale, ou « à froid »]
- **Target de challenge** : [enveloppe à tenir]

> Estimation = prior incertain, resserré story après story par le CSI.
