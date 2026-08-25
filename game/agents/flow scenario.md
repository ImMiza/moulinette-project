flowchart TD 

START([Début du visual novel]) 

%% ========================= %% PROLOGUE %% ========================= START --> P0 

subgraph P0["PROLOGUE — Minecraft : Une maison beaucoup trop grande"] direction TB P0A[Jessy construit seul] P0B[Ilona rejoint le serveur par hasard] P0C[Elle détruit une partie de la construction] P0D{Réaction initiale de Jessy} P0E[Réparer ensemble] P0F[Transformer l'accident en blague] P0G[Lancer une guerre de poulets] P0H[Construire la maison absurde] P0I[Premier appel vocal] P0J[Promesse légère : finir la maison un jour] 

P0A --> P0B --> P0C --> P0D P0D --> P0E --> P0H P0D --> P0F --> P0H P0D --> P0G --> P0H P0H --> P0I --> P0J end 

P0J --> A1 

%% ========================= %% ARC I %% ========================= subgraph A1["ARC I — Printemps : La vie hors écran"] direction TB A1A[Découverte : même école ou même train] A1B[Maladresse réelle après l'aisance en ligne] A1C[Scènes de proximité : sakura, toit, bentō, konbini, train] A1D[Ilona prend des initiatives] A1E{Rumeur : Vous sortez ensemble ?} A1F[Jessy répond avec sincérité] A1G[Jessy fait une blague] 

A1H[Jessy nie trop vite] A1I[Jessy laisse Ilona répondre] A1J[Première confidence d'Ilona] A1K[Entrée d'Allan, Alexandre et Sofiane] 

A1A --> A1B --> A1C --> A1D --> A1E A1E --> A1F --> A1J A1E --> A1G --> A1J A1E --> A1H --> A1J A1E --> A1I --> A1J A1J --> A1K end A1 --> A2 

%% ========================= %% ARC II %% ========================= subgraph A2["ARC II — Vacances d'été : La plage"] direction TB A2A[Sortie de groupe à la plage] A2B[Entrée de Théo : observateur, rassurant, ambigu] A2C[Théo aide Ilona et remarque sa fatigue] A2D[Jessy ressent l'incertitude] A2E{Ilona part faire une activité avec Théo} A2F[Jessy fait confiance et propose d'en parler après] A2G[Jessy demande un temps pour se calmer puis revient] A2H[Jessy fait une blague jalouse] A2I[Jessy surveille ou suit le duo] A2J[Jessy s'éloigne sans rien dire] A2K[Ilona confronte Jessy : Pourquoi as-tu fait comme si je n'existais plus ?] A2A --> A2B --> A2C --> A2D --> A2E A2E --> A2F --> A2K A2E --> A2G --> A2K A2E --> A2H --> A2K A2E --> A2I --> A2K A2E --> A2J --> A2K end A2 --> A3 

%% ========================= 

%% ARC III %% ========================= 

subgraph A3["ARC III — Rentrée : Les regards"] direction TB A3A[Conséquences émotionnelles de la plage] A3B[Festival culturel et rumeurs] A3C[Ilona et Théo travaillent ensemble au stand] A3D[Jessy doit choisir sa manière d'être présent] A3E{Choix au festival} A3F[Aider sans réclamer le centre] A3G[Prendre de la distance puis l'expliquer] A3H[Saboter avec une blague] A3I[Demander ce qu'Ilona ressent sans exiger de réponse] A3J[Ilona cherche un espace sans attente] A3K[Première scène symbolique avec Monsieur Laplage] 

A3A --> A3B --> A3C --> A3D --> A3E A3E --> A3F --> A3J A3E --> A3G --> A3J A3E --> A3H --> A3J A3E --> A3I --> A3J A3J --> A3K end 

A3 --> A4 

%% ========================= %% ARC IV %% ========================= subgraph A4["ARC IV — Noël : Le cadeau qui dit trop de choses"] direction TB A4A[Illuminations et rendez-vous d'hiver] A4B[Jessy prépare un cadeau] A4C[Théo offre aussi un objet très personnel] A4D{Sens du geste de Jessy} A4E[Miniature de la maison avec ses erreurs] A4F[Cadeau coûteux mais impersonnel] A4G[Blague interne tendre] A4H[Pas de cadeau : discussion honnête] A4I[Ilona pose une limite] A4J[Phrase pivot : connaître mes goûts ne veut pas dire savoir ce que je veux] 

A4A --> A4B --> A4C --> A4D 

A4D --> A4E --> A4I A4D --> A4F --> A4I A4D --> A4G --> A4I A4D --> A4H --> A4I A4I --> A4J end 

A4 --> A5 

%% ========================= 

%% ARC V %% ========================= 

subgraph A5["ARC V — Examens, Saint-Valentin et White Day : Ce qu'on ne dit pas"] direction TB 

A5A[Fatigue, révisions et incertitude sur l'avenir] A5B[Ilona annule une sortie car elle est épuisée] A5C[Théo propose de gérer des choses à sa place] A5D[Conversation difficile] 

A5E{Question d'Ilona : peur de me perdre ou manque de confiance ?} A5F[Jessy admet sa peur et son apprentissage] A5G[Jessy suppose qu'Ilona devrait déjà savoir] A5H[Jessy désigne Théo comme unique problème] A5I[Jessy reporte la discussion] 

A5J[Deuxième confidence à Monsieur Laplage] 

A5A --> A5B --> A5C --> A5D --> A5E 

A5E --> A5F --> A5J A5E --> A5G --> A5J A5E --> A5H --> A5J A5E --> A5I --> A5J end 

A5 --> A6 

%% ========================= 

%% ARC VI %% ========================= 

subgraph A6["ARC VI — Remise des diplômes : Après aujourd'hui"] direction TB 

A6A[Fin du cadre scolaire] 

A6B[Photos, uniformes signés, promesses de rester proches] 

A6C[Jessy retrouve Ilona à l'écart] 

A6D{Question sur l'après-école} 

A6E[Tu veux continuer avec moi après l'école ?] A6F[Qu'est-ce que tu veux vraiment pour la suite ?] A6G[Éviter la conversation] A6H[Partir avant sa réponse] A6I[Ilona peut enfin formuler projets, peur et besoins] 

A6A --> A6B --> A6C --> A6D 

A6D --> A6E --> A6I A6D --> A6F --> A6I A6D --> A6G --> A6I A6D --> A6H --> A6I end 

A6 --> A7 

%% ========================= 

%% ARC VII %% ========================= subgraph A7["ARC VII — Randonnée : Le chemin sans itinéraire"] direction TB A7A[Bus ou train annulé] A7B[Sofiane révèle son AE86 et résout le transport] A7C[Allan et Alexandre se retirent] A7D[Jessy et Ilona marchent sans public ni réseau] A7E[Fatigue, brouillard, refuge et pause] A7F[Conversation décisive] A7G{Jessy choisit une manière de parler} A7H[Nommer sa peur et écouter] A7I[Accuser Théo] A7J[Exiger une réponse immédiate] A7K[Prétendre que tout va bien] A7L[Laisser Ilona finir sans l'interrompre] 

A7A --> A7B --> A7C --> A7D --> A7E --> A7F --> A7G 

A7G --> A7H A7G --> A7I A7G --> A7J A7G --> A7K A7G --> A7L end 

%% ========================= 

%% EVALUATION 

%% ========================= 

A7H --> CHECK 

A7I --> CHECK A7J --> CHECK A7K --> CHECK A7L --> CHECK 

CHECK{État relationnel accumulé} 

CHECK -->|Confiance + communication + réparations suffisantes| R1 

CHECK -->|Silences répétés, contrôle ou autonomie d'Ilona fragilisée| R2 

%% ========================= 

%% ROUTE ILONA 

%% ========================= 

subgraph R1["ROUTE ILONA — Festival d'été : Les lanternes ne choisissent pas"] direction TB 

R1A[Matsuri : yukata, jeux, takoyaki et lanternes] 

R1B[Ilona choisit le stand et initie des moments] 

R1C[Référence à la maison Minecraft] 

R1D[Jessy échoue à gagner une peluche] 

R1E[Feu d'artifice] 

R1F{Conclusion émotionnelle} 

R1G[Promesse immense mais nuancée] 

R1H[Je veux continuer avec toi] 

R1I[Déclaration imparfaite mais sincère] 

R1J[Prendre la main avec réciprocité visible] 

R1A --> R1B --> R1C --> R1D --> R1E --> R1F 

R1F --> R1G R1F --> R1H R1F --> R1I R1F --> R1J end 

R1G --> END1 R1H --> END2 R1I --> END2 R1J --> END2 

END1([Fin 1 : Ils ont bien grandi, les petits]) END2([Fin 2 : Juste Jessy et Ilona]) 

%% ========================= 

%% ROUTE SEPARATION 

%% ========================= 

subgraph R2["ROUTE SÉPARATION — Streaming : Le monde après la maison"] direction TB 

R2A[Jessy stream seul dans leur ancien monde Minecraft] R2B[Le chat rappelle les private jokes et les blessures] R2C[Ilona poursuit sa propre vie] R2D{État d'Ilona et influence de Théo} R2E[Distance, silence et deuil relationnel] R2F[Ilona choisit un espace libre et créatif] R2G[Théo transforme son aide en dépendance] R2H[Pression du streaming et isolement] 

R2A --> R2B --> R2C --> R2D R2D --> R2E R2D --> R2F R2D --> R2G --> R2H end 

R2E --> END3 R2F --> END4 R2H --> END5 END3([Fin 3 : La maison silencieuse]) END4([Fin 4 : La plage ne répond plus]) END5([Fin 5 : La route de Théo]) 

%% ========================= %% EASTER EGG %% ========================= EGG{6 objets cosmiques mangés par Ilona ?} P0 -.-> EGG A1 -.-> EGG A2 -.-> EGG A3 -.-> EGG A4 -.-> EGG A5 -.-> EGG A6 -.-> EGG 

EGG -->|Oui| END6([Fin 6 : L'Ilonanium]) EGG -->|Non| POST 

END1 --> POST 

END2 --> POST END3 --> POST END4 --> POST END5 --> POST END6 --> POST 

POST([Post-générique : Le prochain, c'est toi]) 

%% ========================= %% FILS INVISIBLES %% ========================= subgraph TRACK["Fils invisibles suivis tout au long du jeu"] direction LR T1[Confiance] T2[Communication] T3[Autonomie d'Ilona] T4[Jalousie de Jessy] T5[Réparations après erreur] T6[Influence de Théo] T7[Pression du streaming] T8[Maison Minecraft respectée] end 

TRACK -. influence narrative .-> CHECK 

classDef good fill:#daf5df,stroke:#2f7d46,color:#111; classDef danger fill:#f8d7da,stroke:#a33,color:#111; classDef neutral fill:#fff3cd,stroke:#a67c00,color:#111; classDef ending fill:#dbeafe,stroke:#2563eb,color:#111; 

class R1,R1A,R1B,R1C,R1D,R1E good; class R2,R2A,R2B,R2C,R2D,R2E,R2F,R2G,R2H danger; class A2E,A3E,A5E,A6D,A7G,CHECK,EGG neutral; class END1,END2,END3,END4,END5,END6,POST ending; 

