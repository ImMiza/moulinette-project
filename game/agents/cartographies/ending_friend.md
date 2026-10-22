# Good ending Friend — Le dernier été

Fichier : `game/arcs/endings/ending_friend.rpy`.
Source narrative : les neuf fiches de `game/agents/friend_ending/`.

## Entrée et structure

`arc_7_jessy_fin_relation` mène à `ending_friend` uniquement si
`arc7_jessy_relation == "amitie"`. L'amour mène à `ending_family`, avec la tente
comme avec le hamac, selon la correction demandée par l'auteur à l'intégration.
Sans réponse enregistrée, une ancienne sauvegarde revient au bivouac pour jouer
l'aveu. La possibilité de choisir Ilonanium reste prioritaire en amont.

`record_ending("friend")` est appelé à l'entrée. Aucun menu, nouveau score ou
flag narratif. Chaque scène rejoint la suivante par `jump` ; le générique se
termine par `return`.

## Déroulement

1. **`ending_friend_distance`** : le soir du retour, Jessy renonce à préparer une
   surprise dans Minecraft. Il accepte ensuite le refus d'une partie sans
   relancer Ilona. Expédition absurde avec Alexandre dans un trou. Ilona dessine
   et lance un petit stream amateur ; les échanges reprennent dans le groupe.
2. **`ending_friend_invitation`** : Ilona propose la plage avant que les nouveaux
   rythmes compliquent les rencontres. Théo rejoint leur correspondance depuis
   Tokyo. Sofiane transporte le matériel en voiture. Rendez-vous à 9 h 10.
3. **`ending_friend_trajet`** : retrouvailles à la gare, sur un quai éclairé par le
   soleil de 9 h, puis dans le train. Le pont
   Minecraft d'Allan et Alexandre, le dîner raté de Théo, un silence confortable
   entre Jessy et Ilona. Sofiane les attend près du parking avec la Trueno.
4. **`ending_friend_chateau`** : provisions démesurées, serviettes oubliées,
   château collectif avec route, cuisine, porte sans mur et restaurant pour
   crabes. Théo demande avant d'aider Alexandre. La marée emporte une partie de
   l'ouvrage ; toutes les affaires sont déplacées avant son arrivée.
5. **`ending_friend_promenade`** : achats de boissons. Ilona évoque sa peine et la
   difficulté de reprendre contact ; Jessy exprime son hésitation sans reprendre
   son refus amoureux. Elle lui raconte ensuite son idée de streams de dessins
   de bâtiments impossibles. Elle boit par distraction dans le citron d'Allan.
6. **`ending_friend_promesse`** : Allan propose un rendez-vous annuel fixe. Les
   contraintes font affleurer sa peur de perdre le groupe. Ils organisent une
   rencontre plus proche, dans trois semaines, chez lui, avec quatre personnes.
7. **`ending_friend_photo`** : Jessy demande une place dans le cadre. Retardateur,
   photo désordonnée des six amis, rangement et départs. Les adieux se font sur
   la promenade, à la bifurcation visible entre la gare et le parking. Sofiane prend la voiture,
   les autres le train de nuit ; Théo reprend ensuite sa correspondance pour Tokyo.
8. **`ending_friend_annees`** : quatre tableaux sur trois ans. La première année,
   café sous la pluie avec Allan, Alexandre et Ilona, puis anniversaire
   d'Alexandre en appel vidéo quelques mois plus tard : Allan, Jessy, Ilona et Théo participent chacun
   depuis chez eux, Sofiane rejoint après son service. Théo rappelle Alexandre
   seul le dimanche après son départ anticipé. La deuxième année, Jessy et
   Ilona jouent une heure. Au printemps de la troisième année, Allan rend à Théo une batterie externe
   dont l'emprunt a été établi au tableau de l'anniversaire ; Sofiane les rejoint.
9. **`ending_friend_retrouvailles`** : l'été de cette troisième année, les six se
   retrouvent à la plage. Théo arrive par les marches de la promenade de jour ;
   Allan l'accueille sous le parasol même s'il doit repartir tôt. Le
   château reprend, une nouvelle photo est prise avant son départ, puis montrée
   en alternance avec l'ancienne. Ils reviennent avec six glaces ; une tour
   s'affaisse sans qu'Alexandre quitte le groupe pour la reconstruire. La photo
   envoyée à tous ferme la scène sur Jessy, qui rejoint les autres autour des glaces.

## Continuité

- Cadre japonais ; région d'origine non nommée. Aucune date scolaire ajoutée.
- Le refus amoureux a des conséquences et n'est jamais transformé en promesse
  de couple. Les deux protagonistes ont des activités et projets personnels.
- Ilona garde ses streams amateurs. Aucun studio professionnel ni couple avec
  Théo emprunté à l'autre route.
- Théo conserve sa vie à Tokyo. Les liens reviennent progressivement, sans
  déclaration de pardon collectif. Son rapprochement avec Allan prolonge l'arc 7.
- La photo rappelle la place de Jessy au bord du cadre dans l'arc 2, sans nier
  l'éventuelle seconde photo choisie par le joueur à l'époque.
- Aucun cadeau optionnel, secret du maid café, mariage ou enfant imposé. La
  possession de la Trueno n'est pas supposée trois ans plus tard.
- Nouveaux détails : formation puis travail de Jessy, ses recherches de logement ;
  dessins, travail et affiche d'atelier d'Ilona ; déménagement d'Alexandre ; frère
  d'Allan et ancien groupe d'amis. Aucun métier précis n'est fixé.

## Mise en scène et vérification

Treize décors dédiés ont été générés avec imagegen le 17 octobre 2026. Les chambres
de Jessy et d'Ilona ont chacune leur image ; `bg friend appel` montre le bureau
d'Alexandre. Deux vues de l'appel Discord montrent d'abord cinq participants,
puis les six après l'arrivée de Sofiane. L'appartement d'Allan existe avant et
après l'arrivée du repas (`bg friend appartement`, puis `bg friend appartement repas`).
Ces onze images sont dans `images/scenes/backgrounds/friend/`. Quatre vues
supplémentaires y montrent le quai de gare au soleil le matin, le train du
retour de nuit, la promenade au coucher du soleil pour les adieux et ses marches
en plein jour pour l'arrivée de Théo. Le trou Minecraft remplace aussi
son fond uni : versions `bg friend minecraft ouvert` et `ferme`, dans
`images/scenes/backgrounds/minecraft/`, avec bascule lorsque le ciel disparaît.
Les PNG sont opaques et affichés en 1920 × 1080 avec `Transform(..., fit="cover")`.
Le style des quatre intérieurs a été harmonisé avec les décors de la maison
Family et du café de l'arc 5. Les consignes exactes figurent dans le README du
dossier `backgrounds/friend/`.

Les photos `cg friend premier ete` et `cg friend retrouvailles` sont des
compositions fixes des six sprites existants, sans suivi de locuteur ; prévoir
des illustrations dédiées pour rendre les gestes racontés. Les tenues existantes
servent aussi aux ellipses de trois ans. La scène de
Jessy dans sa chambre utilise une variante d'intérieur légère dans
`images/personnages/Jessy/home/`. Alexandre utilise lui aussi une variante
d'intérieur dans `images/personnages/Alexandre/home/` pour l'appel d'anniversaire.
Les portraits dans les trois chambres ont une échelle locale plus grande que
dans les scènes de groupe, afin de correspondre aux proportions des meubles.

La mise en scène ordinaire affiche au maximum trois portraits ; les cases vidéo
de Discord font exception. Chaque CG possède un texte et un arrêt sans durée
imposée, que le joueur quitte d'un clic. Musiques du jeu, ambiance de mer,
effets de photo et de train ; aucune ressource externe nécessaire.

Une version antérieure a été compilée avec Ren'Py 8.5.3 sans diagnostic dans
cette fin. Les modifications récentes ont été vérifiées statiquement ; une
lecture complète en jeu reste nécessaire pour confirmer l'échelle des portraits,
le rythme et les transitions. Des références audio non résolues préexistent
dans les arcs 5 et 7, ainsi que les avertissements `im.Scale`.
