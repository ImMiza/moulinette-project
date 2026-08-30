# Diagramme de flux - Arcs et Endings

```mermaid
flowchart TD
    A[Arc 1 à 5] --> B[Arc 6]
    B --> C{calcul<br/>choix et<br/>points}
    
    C --> D[arc 7 théo]
    C --> E[arc 7 jessy]
    
    D --> F{selon<br/>choix<br/>dans<br/>arc 7C}
    E --> G{selon<br/>choix<br/>dans<br/>arc 7}
    
    F -->|gauche| H[ending neutre]
    F -->|droite| I[bad ending]
    
    G -->|gauche| J[ending ami]
    G -->|centre| K[ending illonanium]
    G -->|droite| L[ending romance]
```

## Structure

- **Arcs 1-5** → **Arc 6** : Progression linéaire
- **Calcul choix et points** : Point de décision basé sur les choix précédents
- **Arc 7** : Deux branches possibles
  - **Arc 7 théo** → 2 endings possibles
  - **Arc 7 jessy** → 3 endings possibles

## Endings

### Branche Théo
- Ending neutre
- Bad ending

### Branche Jessy
- Ending ami
- Ending illonanium
- Ending romance
